"""Flask routes for the Gym Management System."""

from datetime import date, datetime, timedelta

from flask import (
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from sqlalchemy import func

from forms import (
    AttendanceForm,
    LoginForm,
    MemberForm,
    MembershipPlanForm,
    PaymentForm,
    TrainerForm,
)
from models import (
    Attendance,
    Member,
    MembershipPlan,
    Payment,
    Trainer,
    User,
    db,
)


# ═══════════════════════════════════════════════════════════════════════════════
# Helper utilities
# ═══════════════════════════════════════════════════════════════════════════════

def _populate_plan_choices(form):
    """Fill the membership_plan_id dropdown with active plans."""
    plans = MembershipPlan.query.filter_by(status="active").order_by(
        MembershipPlan.name
    ).all()
    form.membership_plan_id.choices = [(0, "— Select Plan —")] + [
        (p.id, f"{p.name} ({p.duration_months}mo – ₹{p.price})") for p in plans
    ]


def _populate_member_choices(form):
    """Fill the member_id dropdown with active members."""
    members = Member.query.filter_by(status="active").order_by(
        Member.first_name
    ).all()
    form.member_id.choices = [(0, "— Select Member —")] + [
        (m.id, f"{m.full_name} ({m.email})") for m in members
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# Route registration
# ═══════════════════════════════════════════════════════════════════════════════

def register_routes(app):
    """Register all application routes on *app*."""

    # ───────────────────────────────────────────────────────────────────────
    # AUTH ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash("Logged in successfully.", "success")
                next_page = request.args.get("next")
                return redirect(next_page or url_for("dashboard"))
            flash("Invalid username or password.", "danger")
        return render_template("login.html", form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.", "info")
        return redirect(url_for("login"))

    # ───────────────────────────────────────────────────────────────────────
    # DASHBOARD ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/")
    @login_required
    def index():
        return redirect(url_for("dashboard"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        try:
            today = date.today()
            first_of_month = today.replace(day=1)

            # --- summary cards ---
            total_members = Member.query.count()
            active_members = Member.query.filter_by(status="active").count()

            revenue_this_month = (
                db.session.query(func.coalesce(func.sum(Payment.amount), 0))
                .filter(
                    Payment.status == "completed",
                    Payment.payment_date >= datetime.combine(first_of_month, datetime.min.time()),
                )
                .scalar()
            )

            today_attendance = (
                Attendance.query.filter(
                    func.date(Attendance.check_in) == today
                ).count()
            )

            # --- recent activity ---
            recent_payments = (
                Payment.query.order_by(Payment.created_at.desc()).limit(5).all()
            )
            recent_members = (
                Member.query.order_by(Member.created_at.desc()).limit(5).all()
            )

            # --- chart data: membership distribution by plan ---
            plan_stats = (
                db.session.query(
                    MembershipPlan.name,
                    func.count(Member.id),
                )
                .outerjoin(Member, Member.membership_plan_id == MembershipPlan.id)
                .group_by(MembershipPlan.name)
                .all()
            )
            membership_chart = {
                "labels": [row[0] for row in plan_stats],
                "data": [row[1] for row in plan_stats],
            }

            # --- chart data: revenue trend (last 6 months) ---
            revenue_trend_labels = []
            revenue_trend_data = []
            for i in range(5, -1, -1):
                # walk backwards from current month
                ref = today.replace(day=1) - timedelta(days=i * 30)
                month_start = ref.replace(day=1)
                if month_start.month == 12:
                    month_end = month_start.replace(year=month_start.year + 1, month=1)
                else:
                    month_end = month_start.replace(month=month_start.month + 1)

                total = (
                    db.session.query(func.coalesce(func.sum(Payment.amount), 0))
                    .filter(
                        Payment.status == "completed",
                        Payment.payment_date >= datetime.combine(month_start, datetime.min.time()),
                        Payment.payment_date < datetime.combine(month_end, datetime.min.time()),
                    )
                    .scalar()
                )
                revenue_trend_labels.append(month_start.strftime("%b %Y"))
                revenue_trend_data.append(float(total))

            revenue_chart = {
                "labels": revenue_trend_labels,
                "data": revenue_trend_data,
            }

            # --- chart data: attendance (last 7 days) ---
            attendance_labels = []
            attendance_data = []
            for i in range(6, -1, -1):
                day = today - timedelta(days=i)
                count = Attendance.query.filter(
                    func.date(Attendance.check_in) == day
                ).count()
                attendance_labels.append(day.strftime("%a %d"))
                attendance_data.append(count)

            attendance_chart = {
                "labels": attendance_labels,
                "data": attendance_data,
            }

            return render_template(
                "dashboard.html",
                total_members=total_members,
                active_members=active_members,
                revenue_this_month=revenue_this_month,
                today_attendance=today_attendance,
                recent_payments=recent_payments,
                recent_members=recent_members,
                membership_chart=membership_chart,
                revenue_chart=revenue_chart,
                attendance_chart=attendance_chart,
            )

        except Exception as e:
            flash(f"Error loading dashboard: {e}", "danger")
            return render_template("dashboard.html")

    # ───────────────────────────────────────────────────────────────────────
    # MEMBER ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/members")
    @login_required
    def members_list():
        try:
            q = request.args.get("q", "").strip()
            query = Member.query

            if q:
                like = f"%{q}%"
                query = query.filter(
                    db.or_(
                        Member.first_name.ilike(like),
                        Member.last_name.ilike(like),
                        Member.email.ilike(like),
                        Member.phone.ilike(like),
                    )
                )

            members = query.order_by(Member.created_at.desc()).all()
            return render_template("members/list.html", members=members, q=q)

        except Exception as e:
            flash(f"Error loading members: {e}", "danger")
            return render_template("members/list.html", members=[], q="")

    @app.route("/members/add", methods=["GET", "POST"])
    @login_required
    def member_add():
        form = MemberForm()
        _populate_plan_choices(form)

        if form.validate_on_submit():
            try:
                member = Member(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    phone=form.phone.data,
                    address=form.address.data,
                    gender=form.gender.data,
                    date_of_birth=form.date_of_birth.data,
                    join_date=form.join_date.data or date.today(),
                    emergency_contact=form.emergency_contact.data,
                    emergency_phone=form.emergency_phone.data,
                    status=form.status.data,
                    membership_plan_id=(
                        form.membership_plan_id.data
                        if form.membership_plan_id.data
                        else None
                    ),
                )
                db.session.add(member)
                db.session.commit()
                flash("Member added successfully.", "success")
                return redirect(url_for("members_list"))
            except Exception as e:
                db.session.rollback()
                flash(f"Error adding member: {e}", "danger")

        return render_template("members/form.html", form=form, title="Add Member")

    @app.route("/members/edit/<int:id>", methods=["GET", "POST"])
    @login_required
    def member_edit(id):
        member = Member.query.get_or_404(id)
        form = MemberForm(obj=member)
        _populate_plan_choices(form)

        if form.validate_on_submit():
            try:
                form.populate_obj(member)
                member.membership_plan_id = (
                    form.membership_plan_id.data
                    if form.membership_plan_id.data
                    else None
                )
                db.session.commit()
                flash("Member updated successfully.", "success")
                return redirect(url_for("member_view", id=member.id))
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating member: {e}", "danger")

        return render_template(
            "members/form.html", form=form, title="Edit Member", member=member
        )

    @app.route("/members/view/<int:id>")
    @login_required
    def member_view(id):
        try:
            member = Member.query.get_or_404(id)
            payments = (
                Payment.query.filter_by(member_id=id)
                .order_by(Payment.payment_date.desc())
                .all()
            )
            attendances = (
                Attendance.query.filter_by(member_id=id)
                .order_by(Attendance.check_in.desc())
                .all()
            )
            return render_template(
                "members/view.html",
                member=member,
                payments=payments,
                attendances=attendances,
            )
        except Exception as e:
            flash(f"Error loading member profile: {e}", "danger")
            return redirect(url_for("members_list"))

    @app.route("/members/delete/<int:id>", methods=["POST"])
    @login_required
    def member_delete(id):
        try:
            member = Member.query.get_or_404(id)
            db.session.delete(member)
            db.session.commit()
            flash("Member deleted successfully.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error deleting member: {e}", "danger")
        return redirect(url_for("members_list"))

    # ───────────────────────────────────────────────────────────────────────
    # TRAINER ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/trainers")
    @login_required
    def trainers_list():
        try:
            trainers = Trainer.query.order_by(Trainer.created_at.desc()).all()
            return render_template("trainers/list.html", trainers=trainers)
        except Exception as e:
            flash(f"Error loading trainers: {e}", "danger")
            return render_template("trainers/list.html", trainers=[])

    @app.route("/trainers/add", methods=["GET", "POST"])
    @login_required
    def trainer_add():
        form = TrainerForm()
        if form.validate_on_submit():
            try:
                trainer = Trainer(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    phone=form.phone.data,
                    specialization=form.specialization.data,
                    experience_years=form.experience_years.data or 0,
                    salary=form.salary.data or 0.0,
                    hire_date=form.hire_date.data or date.today(),
                    status=form.status.data,
                )
                db.session.add(trainer)
                db.session.commit()
                flash("Trainer added successfully.", "success")
                return redirect(url_for("trainers_list"))
            except Exception as e:
                db.session.rollback()
                flash(f"Error adding trainer: {e}", "danger")

        return render_template("trainers/form.html", form=form, title="Add Trainer")

    @app.route("/trainers/edit/<int:id>", methods=["GET", "POST"])
    @login_required
    def trainer_edit(id):
        trainer = Trainer.query.get_or_404(id)
        form = TrainerForm(obj=trainer)

        if form.validate_on_submit():
            try:
                form.populate_obj(trainer)
                db.session.commit()
                flash("Trainer updated successfully.", "success")
                return redirect(url_for("trainers_list"))
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating trainer: {e}", "danger")

        return render_template(
            "trainers/form.html", form=form, title="Edit Trainer", trainer=trainer
        )

    @app.route("/trainers/delete/<int:id>", methods=["POST"])
    @login_required
    def trainer_delete(id):
        try:
            trainer = Trainer.query.get_or_404(id)
            db.session.delete(trainer)
            db.session.commit()
            flash("Trainer deleted successfully.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error deleting trainer: {e}", "danger")
        return redirect(url_for("trainers_list"))

    # ───────────────────────────────────────────────────────────────────────
    # MEMBERSHIP PLAN ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/plans")
    @login_required
    def plans_list():
        try:
            plans = (
                db.session.query(
                    MembershipPlan,
                    func.count(Member.id).label("member_count"),
                )
                .outerjoin(Member, Member.membership_plan_id == MembershipPlan.id)
                .group_by(MembershipPlan.id)
                .order_by(MembershipPlan.created_at.desc())
                .all()
            )
            return render_template("plans/list.html", plans=plans)
        except Exception as e:
            flash(f"Error loading plans: {e}", "danger")
            return render_template("plans/list.html", plans=[])

    @app.route("/plans/add", methods=["GET", "POST"])
    @login_required
    def plan_add():
        form = MembershipPlanForm()
        if form.validate_on_submit():
            try:
                plan = MembershipPlan(
                    name=form.name.data,
                    description=form.description.data,
                    duration_months=form.duration_months.data,
                    price=float(form.price.data),
                    features=form.features.data,
                    status=form.status.data,
                )
                db.session.add(plan)
                db.session.commit()
                flash("Membership plan added successfully.", "success")
                return redirect(url_for("plans_list"))
            except Exception as e:
                db.session.rollback()
                flash(f"Error adding plan: {e}", "danger")

        return render_template("plans/form.html", form=form, title="Add Plan")

    @app.route("/plans/edit/<int:id>", methods=["GET", "POST"])
    @login_required
    def plan_edit(id):
        plan = MembershipPlan.query.get_or_404(id)
        form = MembershipPlanForm(obj=plan)

        if form.validate_on_submit():
            try:
                form.populate_obj(plan)
                plan.price = float(form.price.data)
                db.session.commit()
                flash("Membership plan updated successfully.", "success")
                return redirect(url_for("plans_list"))
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating plan: {e}", "danger")

        return render_template(
            "plans/form.html", form=form, title="Edit Plan", plan=plan
        )

    @app.route("/plans/delete/<int:id>", methods=["POST"])
    @login_required
    def plan_delete(id):
        try:
            plan = MembershipPlan.query.get_or_404(id)
            if plan.members:
                flash(
                    "Cannot delete plan — it still has members assigned.", "warning"
                )
            else:
                db.session.delete(plan)
                db.session.commit()
                flash("Membership plan deleted successfully.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error deleting plan: {e}", "danger")
        return redirect(url_for("plans_list"))

    # ───────────────────────────────────────────────────────────────────────
    # PAYMENT ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/payments")
    @login_required
    def payments_list():
        try:
            query = Payment.query

            start_date = request.args.get("start_date")
            end_date = request.args.get("end_date")

            if start_date:
                try:
                    sd = datetime.strptime(start_date, "%Y-%m-%d")
                    query = query.filter(Payment.payment_date >= sd)
                except ValueError:
                    flash("Invalid start date format.", "warning")

            if end_date:
                try:
                    ed = datetime.strptime(end_date, "%Y-%m-%d")
                    # include the entire end day
                    query = query.filter(
                        Payment.payment_date < ed + timedelta(days=1)
                    )
                except ValueError:
                    flash("Invalid end date format.", "warning")

            payments = query.order_by(Payment.payment_date.desc()).all()
            return render_template(
                "payments/list.html",
                payments=payments,
                start_date=start_date or "",
                end_date=end_date or "",
            )

        except Exception as e:
            flash(f"Error loading payments: {e}", "danger")
            return render_template(
                "payments/list.html", payments=[], start_date="", end_date=""
            )

    @app.route("/payments/add", methods=["GET", "POST"])
    @login_required
    def payment_add():
        form = PaymentForm()
        _populate_member_choices(form)

        if form.validate_on_submit():
            try:
                payment = Payment(
                    member_id=form.member_id.data,
                    amount=float(form.amount.data),
                    payment_date=(
                        datetime.combine(form.payment_date.data, datetime.min.time())
                        if form.payment_date.data
                        else datetime.utcnow()
                    ),
                    payment_method=form.payment_method.data,
                    transaction_id=form.transaction_id.data,
                    status=form.status.data,
                    notes=form.notes.data,
                )
                db.session.add(payment)
                db.session.commit()
                flash("Payment recorded successfully.", "success")
                return redirect(url_for("payments_list"))
            except Exception as e:
                db.session.rollback()
                flash(f"Error recording payment: {e}", "danger")

        return render_template("payments/form.html", form=form, title="Add Payment")

    @app.route("/payments/receipt/<int:id>")
    @login_required
    def payment_receipt(id):
        try:
            payment = Payment.query.get_or_404(id)
            return render_template("payments/receipt.html", payment=payment)
        except Exception as e:
            flash(f"Error loading receipt: {e}", "danger")
            return redirect(url_for("payments_list"))

    @app.route("/payments/delete/<int:id>", methods=["POST"])
    @login_required
    def payment_delete(id):
        try:
            payment = Payment.query.get_or_404(id)
            db.session.delete(payment)
            db.session.commit()
            flash("Payment deleted successfully.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error deleting payment: {e}", "danger")
        return redirect(url_for("payments_list"))

    # ───────────────────────────────────────────────────────────────────────
    # ATTENDANCE ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/attendance")
    @login_required
    def attendance_list():
        try:
            filter_date_str = request.args.get("date", "")
            if filter_date_str:
                try:
                    filter_date = datetime.strptime(filter_date_str, "%Y-%m-%d").date()
                except ValueError:
                    filter_date = date.today()
                    flash("Invalid date format; showing today.", "warning")
            else:
                filter_date = date.today()

            attendances = (
                Attendance.query.filter(
                    func.date(Attendance.check_in) == filter_date
                )
                .order_by(Attendance.check_in.desc())
                .all()
            )

            # supply members for the check-in dropdown
            members = (
                Member.query.filter_by(status="active")
                .order_by(Member.first_name)
                .all()
            )

            return render_template(
                "attendance/list.html",
                attendances=attendances,
                filter_date=filter_date.isoformat(),
                members=members,
            )

        except Exception as e:
            flash(f"Error loading attendance: {e}", "danger")
            return render_template(
                "attendance/list.html",
                attendances=[],
                filter_date=date.today().isoformat(),
                members=[],
            )

    @app.route("/attendance/checkin", methods=["POST"])
    @login_required
    def attendance_checkin():
        try:
            member_id = request.form.get("member_id", type=int)
            if not member_id:
                flash("Please select a member.", "warning")
                return redirect(url_for("attendance_list"))

            member = Member.query.get_or_404(member_id)

            # prevent duplicate check-in (same member, same day, no checkout)
            existing = Attendance.query.filter(
                Attendance.member_id == member_id,
                func.date(Attendance.check_in) == date.today(),
                Attendance.check_out.is_(None),
            ).first()

            if existing:
                flash(
                    f"{member.full_name} is already checked in today.", "warning"
                )
            else:
                record = Attendance(
                    member_id=member_id,
                    check_in=datetime.utcnow(),
                )
                db.session.add(record)
                db.session.commit()
                flash(f"{member.full_name} checked in successfully.", "success")

        except Exception as e:
            db.session.rollback()
            flash(f"Error during check-in: {e}", "danger")

        return redirect(url_for("attendance_list"))

    @app.route("/attendance/checkout/<int:id>", methods=["POST"])
    @login_required
    def attendance_checkout(id):
        try:
            record = Attendance.query.get_or_404(id)
            if record.check_out:
                flash("This member has already checked out.", "warning")
            else:
                record.check_out = datetime.utcnow()
                db.session.commit()
                flash("Member checked out successfully.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error during check-out: {e}", "danger")
        return redirect(url_for("attendance_list"))

    # ───────────────────────────────────────────────────────────────────────
    # REPORT ROUTES
    # ───────────────────────────────────────────────────────────────────────

    @app.route("/reports")
    @login_required
    def reports_dashboard():
        try:
            today = date.today()

            # optional date range filter
            start_date_str = request.args.get("start_date", "")
            end_date_str = request.args.get("end_date", "")

            start_dt = None
            end_dt = None
            if start_date_str:
                try:
                    start_dt = datetime.strptime(start_date_str, "%Y-%m-%d")
                except ValueError:
                    pass
            if end_date_str:
                try:
                    end_dt = datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1)
                except ValueError:
                    pass

            # --- summary stats ---
            total_members = Member.query.count()
            active_members = Member.query.filter_by(status="active").count()
            total_trainers = Trainer.query.count()

            revenue_query = db.session.query(
                func.coalesce(func.sum(Payment.amount), 0)
            ).filter(Payment.status == "completed")
            if start_dt:
                revenue_query = revenue_query.filter(Payment.payment_date >= start_dt)
            if end_dt:
                revenue_query = revenue_query.filter(Payment.payment_date < end_dt)
            total_revenue = revenue_query.scalar()

            total_plans = MembershipPlan.query.count()

            return render_template(
                "reports/dashboard.html",
                total_members=total_members,
                active_members=active_members,
                total_trainers=total_trainers,
                total_revenue=total_revenue,
                total_plans=total_plans,
                start_date=start_date_str,
                end_date=end_date_str,
            )

        except Exception as e:
            flash(f"Error loading reports: {e}", "danger")
            return render_template("reports/dashboard.html")

    @app.route("/reports/revenue")
    @login_required
    def report_revenue():
        try:
            start_date_str = request.args.get("start_date", "")
            end_date_str = request.args.get("end_date", "")

            query = Payment.query.filter_by(status="completed")

            if start_date_str:
                try:
                    sd = datetime.strptime(start_date_str, "%Y-%m-%d")
                    query = query.filter(Payment.payment_date >= sd)
                except ValueError:
                    pass
            if end_date_str:
                try:
                    ed = datetime.strptime(end_date_str, "%Y-%m-%d")
                    query = query.filter(Payment.payment_date < ed + timedelta(days=1))
                except ValueError:
                    pass

            payments = query.order_by(Payment.payment_date.desc()).all()
            total_revenue = sum(p.amount for p in payments)

            # monthly breakdown using Python grouping
            monthly = {}
            for p in payments:
                key = p.payment_date.strftime("%Y-%m")
                monthly[key] = monthly.get(key, 0) + p.amount
            # sort chronologically
            monthly_breakdown = sorted(monthly.items())

            return render_template(
                "reports/revenue.html",
                payments=payments,
                total_revenue=total_revenue,
                monthly_breakdown=monthly_breakdown,
                start_date=start_date_str,
                end_date=end_date_str,
            )

        except Exception as e:
            flash(f"Error loading revenue report: {e}", "danger")
            return render_template(
                "reports/revenue.html",
                payments=[],
                total_revenue=0,
                monthly_breakdown=[],
                start_date="",
                end_date="",
            )

    @app.route("/reports/membership")
    @login_required
    def report_membership():
        try:
            # members per plan
            plan_distribution = (
                db.session.query(
                    MembershipPlan.name,
                    func.count(Member.id).label("count"),
                )
                .outerjoin(Member, Member.membership_plan_id == MembershipPlan.id)
                .group_by(MembershipPlan.name)
                .all()
            )

            # status breakdown
            status_breakdown = (
                db.session.query(
                    Member.status,
                    func.count(Member.id),
                )
                .group_by(Member.status)
                .all()
            )

            # gender breakdown
            gender_breakdown = (
                db.session.query(
                    Member.gender,
                    func.count(Member.id),
                )
                .group_by(Member.gender)
                .all()
            )

            total_members = Member.query.count()

            return render_template(
                "reports/membership.html",
                plan_distribution=plan_distribution,
                status_breakdown=status_breakdown,
                gender_breakdown=gender_breakdown,
                total_members=total_members,
            )

        except Exception as e:
            flash(f"Error loading membership report: {e}", "danger")
            return render_template(
                "reports/membership.html",
                plan_distribution=[],
                status_breakdown=[],
                gender_breakdown=[],
                total_members=0,
            )

    @app.route("/reports/attendance")
    @login_required
    def report_attendance():
        try:
            start_date_str = request.args.get("start_date", "")
            end_date_str = request.args.get("end_date", "")

            query = Attendance.query

            if start_date_str:
                try:
                    sd = datetime.strptime(start_date_str, "%Y-%m-%d")
                    query = query.filter(Attendance.check_in >= sd)
                except ValueError:
                    pass
            if end_date_str:
                try:
                    ed = datetime.strptime(end_date_str, "%Y-%m-%d")
                    query = query.filter(
                        Attendance.check_in < ed + timedelta(days=1)
                    )
                except ValueError:
                    pass

            records = query.order_by(Attendance.check_in.desc()).all()
            total_checkins = len(records)

            # daily attendance counts
            daily_counts = {}
            for r in records:
                day = r.check_in.strftime("%Y-%m-%d")
                daily_counts[day] = daily_counts.get(day, 0) + 1
            daily_breakdown = sorted(daily_counts.items())

            # top attending members
            member_counts = {}
            for r in records:
                member_counts[r.member_id] = member_counts.get(r.member_id, 0) + 1
            top_members_ids = sorted(
                member_counts, key=member_counts.get, reverse=True
            )[:10]
            top_members = []
            for mid in top_members_ids:
                m = Member.query.get(mid)
                if m:
                    top_members.append(
                        {"member": m, "count": member_counts[mid]}
                    )

            return render_template(
                "reports/attendance.html",
                records=records,
                total_checkins=total_checkins,
                daily_breakdown=daily_breakdown,
                top_members=top_members,
                start_date=start_date_str,
                end_date=end_date_str,
            )

        except Exception as e:
            flash(f"Error loading attendance report: {e}", "danger")
            return render_template(
                "reports/attendance.html",
                records=[],
                total_checkins=0,
                daily_breakdown=[],
                top_members=[],
                start_date="",
                end_date="",
            )
