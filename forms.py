"""WTForms form classes for the Gym Management System."""

from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DateTimeLocalField,
    DecimalField,
    FloatField,
    IntegerField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    NumberRange,
    Optional,
    ValidationError,
)


# ---------------------------------------------------------------------------
# LoginForm
# ---------------------------------------------------------------------------

class LoginForm(FlaskForm):
    """User login form."""

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=80)],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6, max=128)],
    )
    submit = SubmitField("Log In")


# ---------------------------------------------------------------------------
# MemberForm
# ---------------------------------------------------------------------------

class MemberForm(FlaskForm):
    """Add / edit gym member."""

    first_name = StringField(
        "First Name",
        validators=[DataRequired(), Length(max=50)],
    )
    last_name = StringField(
        "Last Name",
        validators=[DataRequired(), Length(max=50)],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=120)],
    )
    phone = StringField(
        "Phone",
        validators=[DataRequired(), Length(max=20)],
    )
    address = TextAreaField("Address", validators=[Optional()])
    gender = SelectField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        validators=[DataRequired()],
    )
    date_of_birth = DateField(
        "Date of Birth",
        format="%Y-%m-%d",
        validators=[Optional()],
    )
    join_date = DateField(
        "Join Date",
        format="%Y-%m-%d",
        validators=[Optional()],
    )
    emergency_contact = StringField(
        "Emergency Contact Name",
        validators=[Optional(), Length(max=100)],
    )
    emergency_phone = StringField(
        "Emergency Phone",
        validators=[Optional(), Length(max=20)],
    )
    status = SelectField(
        "Status",
        choices=[
            ("active", "Active"),
            ("inactive", "Inactive"),
            ("expired", "Expired"),
        ],
        validators=[DataRequired()],
    )
    membership_plan_id = SelectField(
        "Membership Plan",
        coerce=int,
        validators=[Optional()],
    )
    submit = SubmitField("Save Member")


# ---------------------------------------------------------------------------
# TrainerForm
# ---------------------------------------------------------------------------

class TrainerForm(FlaskForm):
    """Add / edit trainer."""

    first_name = StringField(
        "First Name",
        validators=[DataRequired(), Length(max=50)],
    )
    last_name = StringField(
        "Last Name",
        validators=[DataRequired(), Length(max=50)],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=120)],
    )
    phone = StringField(
        "Phone",
        validators=[DataRequired(), Length(max=20)],
    )
    specialization = StringField(
        "Specialization",
        validators=[Optional(), Length(max=100)],
    )
    experience_years = IntegerField(
        "Experience (years)",
        validators=[Optional(), NumberRange(min=0)],
    )
    salary = FloatField(
        "Salary",
        validators=[Optional(), NumberRange(min=0)],
    )
    hire_date = DateField(
        "Hire Date",
        format="%Y-%m-%d",
        validators=[Optional()],
    )
    status = SelectField(
        "Status",
        choices=[("active", "Active"), ("inactive", "Inactive")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Save Trainer")


# ---------------------------------------------------------------------------
# MembershipPlanForm
# ---------------------------------------------------------------------------

class MembershipPlanForm(FlaskForm):
    """Add / edit membership plan."""

    name = StringField(
        "Plan Name",
        validators=[DataRequired(), Length(max=100)],
    )
    description = TextAreaField("Description", validators=[Optional()])
    duration_months = IntegerField(
        "Duration (months)",
        validators=[DataRequired(), NumberRange(min=1)],
    )
    price = DecimalField(
        "Price",
        places=2,
        validators=[DataRequired(), NumberRange(min=0)],
    )
    features = TextAreaField(
        "Features",
        validators=[Optional()],
    )
    status = SelectField(
        "Status",
        choices=[("active", "Active"), ("inactive", "Inactive")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Save Plan")


# ---------------------------------------------------------------------------
# PaymentForm
# ---------------------------------------------------------------------------

class PaymentForm(FlaskForm):
    """Record a payment."""

    member_id = SelectField(
        "Member",
        coerce=int,
        validators=[DataRequired()],
    )
    amount = DecimalField(
        "Amount",
        places=2,
        validators=[DataRequired(), NumberRange(min=0)],
    )
    payment_date = DateField(
        "Payment Date",
        format="%Y-%m-%d",
        validators=[Optional()],
    )
    payment_method = SelectField(
        "Payment Method",
        choices=[
            ("cash", "Cash"),
            ("card", "Card"),
            ("upi", "UPI"),
            ("online", "Online"),
        ],
        validators=[DataRequired()],
    )
    transaction_id = StringField(
        "Transaction ID",
        validators=[Optional(), Length(max=100)],
    )
    status = SelectField(
        "Status",
        choices=[
            ("completed", "Completed"),
            ("pending", "Pending"),
            ("failed", "Failed"),
        ],
        validators=[DataRequired()],
    )
    notes = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField("Save Payment")


# ---------------------------------------------------------------------------
# AttendanceForm
# ---------------------------------------------------------------------------

class AttendanceForm(FlaskForm):
    """Record attendance check-in / check-out."""

    member_id = SelectField(
        "Member",
        coerce=int,
        validators=[DataRequired()],
    )
    check_in = DateTimeLocalField(
        "Check In",
        format="%Y-%m-%dT%H:%M",
        validators=[DataRequired()],
    )
    check_out = DateTimeLocalField(
        "Check Out",
        format="%Y-%m-%dT%H:%M",
        validators=[Optional()],
    )
    submit = SubmitField("Save Attendance")
