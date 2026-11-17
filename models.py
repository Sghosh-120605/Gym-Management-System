"""SQLAlchemy database models for the Gym Management System."""

from datetime import datetime, date

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


# ---------------------------------------------------------------------------
# User (authentication & authorisation)
# ---------------------------------------------------------------------------

class User(UserMixin, db.Model):
    """Application user (admin / staff)."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="staff")  # admin / staff
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # --- helper methods ---

    def set_password(self, password: str) -> None:
        """Hash and store *password*."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Return ``True`` if *password* matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self) -> bool:
        return self.role == "admin"

    def __repr__(self) -> str:
        return f"<User {self.username!r} ({self.role})>"


# ---------------------------------------------------------------------------
# Member
# ---------------------------------------------------------------------------

class Member(db.Model):
    """Gym member."""

    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text)
    gender = db.Column(db.String(10))
    date_of_birth = db.Column(db.Date)
    join_date = db.Column(db.Date, default=date.today)
    photo = db.Column(db.String(256))  # file-path / URL
    emergency_contact = db.Column(db.String(100))
    emergency_phone = db.Column(db.String(20))
    status = db.Column(
        db.String(20), nullable=False, default="active"
    )  # active / inactive / expired

    membership_plan_id = db.Column(
        db.Integer, db.ForeignKey("membership_plans.id"), nullable=True
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # --- relationships ---
    membership_plan = db.relationship("MembershipPlan", backref="members", lazy=True)
    payments = db.relationship("Payment", backref="member", lazy=True, cascade="all, delete-orphan")
    attendances = db.relationship("Attendance", backref="member", lazy=True, cascade="all, delete-orphan")

    # --- helpers ---

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"<Member {self.full_name!r} ({self.status})>"


# ---------------------------------------------------------------------------
# Trainer
# ---------------------------------------------------------------------------

class Trainer(db.Model):
    """Gym trainer / instructor."""

    __tablename__ = "trainers"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False)
    specialization = db.Column(db.String(100))
    experience_years = db.Column(db.Integer, default=0)
    salary = db.Column(db.Float, default=0.0)
    hire_date = db.Column(db.Date, default=date.today)
    status = db.Column(
        db.String(20), nullable=False, default="active"
    )  # active / inactive
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"<Trainer {self.full_name!r} — {self.specialization}>"


# ---------------------------------------------------------------------------
# MembershipPlan
# ---------------------------------------------------------------------------

class MembershipPlan(db.Model):
    """Available membership plans."""

    __tablename__ = "membership_plans"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    duration_months = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    features = db.Column(db.Text)  # comma-separated or JSON string
    status = db.Column(
        db.String(20), nullable=False, default="active"
    )  # active / inactive
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<MembershipPlan {self.name!r} — {self.duration_months}mo @ {self.price}>"


# ---------------------------------------------------------------------------
# Payment
# ---------------------------------------------------------------------------

class Payment(db.Model):
    """Payment records for members."""

    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(
        db.Integer, db.ForeignKey("members.id"), nullable=False, index=True
    )
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_method = db.Column(
        db.String(20), nullable=False, default="cash"
    )  # cash / card / upi / online
    transaction_id = db.Column(db.String(100))
    status = db.Column(
        db.String(20), nullable=False, default="completed"
    )  # completed / pending / failed
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Payment #{self.id} — ₹{self.amount} ({self.status})>"


# ---------------------------------------------------------------------------
# Attendance
# ---------------------------------------------------------------------------

class Attendance(db.Model):
    """Daily attendance tracking for members."""

    __tablename__ = "attendances"

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(
        db.Integer, db.ForeignKey("members.id"), nullable=False, index=True
    )
    check_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    check_out = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def duration(self):
        """Return session duration if both check-in and check-out are set."""
        if self.check_in and self.check_out:
            return self.check_out - self.check_in
        return None

    def __repr__(self) -> str:
        return f"<Attendance member={self.member_id} in={self.check_in}>"
