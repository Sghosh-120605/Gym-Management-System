# GYM MANAGEMENT SYSTEM

## A Mini Project Report

---

**Submitted in partial fulfillment of the requirements for the award of**
**Bachelor of Computer Applications (BCA) / B.Tech Computer Science & Engineering**

---

| | |
|---|---|
| **Title** | Gym Management System |
| **Institution** | [Your College Name] |
| **University** | [Your University Name] |
| **Submitted By** | [Student Name] |
| **Roll No** | [XXXXXXX] |
| **Under the Guidance of** | [Guide Name], [Designation] |
| **Academic Year** | 2026–2027 |

---

## CERTIFICATE

This is to certify that the mini project entitled **"GYM MANAGEMENT SYSTEM"** has been successfully carried out by **[Student Name]**, Roll No: **[XXXXXXX]**, in partial fulfillment of the requirements for the award of **Bachelor of Computer Applications / B.Tech Computer Science & Engineering** from **[Your University Name]** during the academic year **2026–2027**.

This work has been carried out under my guidance and supervision.

| | |
|---|---|
| **Guide** | **Head of Department** |
| [Guide Name] | [HOD Name] |
| [Designation] | Department of Computer Science |
| Date: __________ | Date: __________ |

**External Examiner:** __________

---

## ACKNOWLEDGEMENT

I would like to express my sincere gratitude to my project guide **[Guide Name]**, whose constant guidance and encouragement helped me complete this project successfully.

I am thankful to **[HOD Name]**, Head of the Department of Computer Science, for providing the necessary facilities and support. I also extend my gratitude to **[Principal Name]**, Principal of **[Your College Name]**, for giving me this opportunity.

I am grateful to all my faculty members who have been a source of inspiration and have shared their valuable knowledge throughout the course. I also wish to thank my friends and family for their constant support and encouragement.

Finally, I thank all those who have directly or indirectly contributed to the successful completion of this project.

---

## ABSTRACT

The **Gym Management System** is a comprehensive web-based application designed to automate and streamline the day-to-day operations of a fitness center. Traditional gym management relies heavily on manual record-keeping using registers and spreadsheets, which is time-consuming, error-prone, and difficult to scale. This project addresses these challenges by providing a centralized digital platform for managing members, trainers, membership plans, payments, attendance, and generating analytical reports.

The system is built using **Python Flask** as the backend web framework, **SQLAlchemy** as the Object-Relational Mapper (ORM), **MySQL/SQLite** as the database, and **HTML5, CSS3, Bootstrap 5, and JavaScript** for the responsive frontend. Key features include secure admin authentication with password hashing, complete CRUD operations for members and trainers, flexible membership plan management, payment recording with printable receipts, real-time attendance tracking with check-in/check-out functionality, and an analytics dashboard with interactive charts powered by Chart.js.

The application follows the Model-View-Controller (MVC) architecture pattern, ensuring clean separation of concerns, maintainability, and scalability. Testing has been carried out using unit tests and manual test cases covering all modules, confirming the system meets its functional requirements.

**Keywords:** Gym Management, Flask, Python, Web Application, SQLAlchemy, Bootstrap, CRUD, MVC

---

## TABLE OF CONTENTS

| Chapter | Title |
|---------|-------|
| | Certificate |
| | Acknowledgement |
| | Abstract |
| 1 | Introduction |
| 1.1 | Introduction |
| 1.2 | Problem Statement |
| 1.3 | Objectives of the Project |
| 1.4 | Scope of the Project |
| 1.5 | Motivation |
| 1.6 | Organization of the Report |
| 2 | Literature Survey / System Analysis |
| 2.1 | Existing System |
| 2.2 | Proposed System |
| 2.3 | Feasibility Study |
| 2.4 | Hardware Requirements |
| 2.5 | Software Requirements |
| 3 | System Design |
| 3.1 | System Architecture |
| 3.2 | ER Diagram |
| 3.3 | Data Flow Diagrams |
| 3.4 | Use Case Diagram |
| 3.5 | Database Design |
| 3.6 | Module Design |
| 4 | Implementation |
| 4.1 | Implementation Environment |
| 4.2 | Module-wise Implementation |
| 4.3 | Database Connection |
| 4.4 | Key Implementation Details |
| 5 | Testing |
| 5.1 | Testing Methodology |
| 5.2 | Test Cases |
| 5.3 | Testing Results Summary |
| 6 | Screenshots / Output |
| 7 | Conclusion and Future Scope |
| 7.1 | Conclusion |
| 7.2 | Limitations |
| 7.3 | Future Enhancements |
| | References / Bibliography |
| | Appendix |

---

## CHAPTER 1: INTRODUCTION

### 1.1 Introduction

In today's fast-paced world, maintaining physical health and fitness has become a priority for people across all age groups. This has led to a significant increase in the number of gyms and fitness centers. With growing memberships, managing gym operations manually has become increasingly difficult. Gym owners and administrators need an efficient system to handle member registrations, track attendance, manage subscriptions, process payments, and generate reports.

A **Gym Management System** is a software application specifically designed to automate these day-to-day operations of a fitness center. It replaces the traditional paper-based record-keeping system with a digital, centralized, and easily accessible platform. Such a system not only reduces the administrative workload but also minimizes errors, provides real-time insights through reports, and enhances the overall member experience.

This project presents a web-based Gym Management System developed using modern web technologies. It provides a user-friendly interface for gym administrators to efficiently manage all aspects of gym operations from a single dashboard.

### 1.2 Problem Statement

Most small and medium-sized gyms still rely on manual methods for managing their operations. These include maintaining paper registers for member records, manually tracking attendance, issuing handwritten receipts, and using basic spreadsheets for financial records. This approach presents several critical problems:

- **Data Redundancy and Inconsistency:** Information is often recorded in multiple places, leading to discrepancies and duplicated data.
- **Time-Consuming Operations:** Looking up member details, calculating dues, and generating reports manually is extremely slow and labor-intensive.
- **Error-Prone Processes:** Manual data entry is susceptible to human errors, which can result in incorrect billing, lost records, or missed renewals.
- **Lack of Real-Time Information:** Without a centralized system, it is difficult to get an instant overview of the gym's financial health, membership statistics, or attendance patterns.
- **Poor Scalability:** As the number of members grows, managing records on paper or spreadsheets becomes increasingly unmanageable.
- **No Data Backup:** Paper records are vulnerable to physical damage, loss, or theft, with no easy way to recover lost information.

There is a clear need for a computerized system that addresses these challenges effectively.

### 1.3 Objectives of the Project

The primary objectives of this project are:

1. To develop a web-based application that automates gym management operations.
2. To provide secure authentication for administrative access.
3. To implement complete CRUD (Create, Read, Update, Delete) operations for managing members, trainers, and membership plans.
4. To facilitate payment recording and generate printable receipts.
5. To enable real-time attendance tracking with check-in and check-out functionality.
6. To generate analytical reports with visual charts for revenue, membership, and attendance.

### 1.4 Scope of the Project

The scope of this project encompasses the following functional areas:

- **User Authentication:** Secure login and logout for admin users.
- **Member Management:** Registration, profile management, search, and status tracking of gym members.
- **Trainer Management:** Adding and managing trainer profiles with their specializations.
- **Membership Plan Management:** Creating and managing different membership plans with pricing and features.
- **Payment Processing:** Recording payments, tracking payment status, and generating receipts.
- **Attendance Management:** Daily check-in/check-out tracking for members.
- **Reporting:** Generating revenue, membership, and attendance reports with graphical visualizations.
- **Dashboard:** A centralized overview showing key metrics and recent activities.

### 1.5 Motivation

The motivation behind this project stems from observing the challenges faced by local gym owners in managing their daily operations. Many gym owners spend a significant portion of their time on administrative tasks rather than focusing on providing quality fitness services. By developing this system, we aim to provide an affordable, easy-to-use solution that can be adopted by gyms of all sizes. Additionally, this project serves as an excellent opportunity to apply and demonstrate knowledge of full-stack web development using Python Flask.

### 1.6 Organization of the Report

This report is organized into the following chapters:

- **Chapter 1 — Introduction:** Provides an overview of the project, problem statement, objectives, scope, and motivation.
- **Chapter 2 — Literature Survey / System Analysis:** Analyzes the existing and proposed systems, feasibility study, and system requirements.
- **Chapter 3 — System Design:** Presents the system architecture, ER diagram, DFDs, use case diagram, database design, and module design.
- **Chapter 4 — Implementation:** Describes the implementation environment and module-wise implementation details with code snippets.
- **Chapter 5 — Testing:** Explains the testing methodology and presents detailed test cases.
- **Chapter 6 — Screenshots / Output:** Showcases the application's user interface.
- **Chapter 7 — Conclusion and Future Scope:** Summarizes the project and discusses future enhancements.

---

## CHAPTER 2: LITERATURE SURVEY / SYSTEM ANALYSIS

### 2.1 Existing System

The existing system in most small and medium gyms is primarily manual and paper-based. It typically involves:

- Member records maintained in physical registers or basic Excel spreadsheets.
- Attendance tracked through sign-in sheets or simple logbooks.
- Payment receipts issued manually using receipt books.
- Financial records maintained in ledgers or basic accounting sheets.
- Communication about renewals and dues done verbally or via personal messages.

**Disadvantages of the Existing System:**

1. **Slow Processing:** Retrieving member information or calculating revenue takes significant time.
2. **Data Loss Risk:** Paper records can be lost due to damage, misplacement, or natural disasters.
3. **No Backup Mechanism:** There is no automated way to back up data.
4. **Inconsistent Records:** Multiple copies of the same data may have different values.
5. **Limited Reporting:** Generating analytical reports or trends is extremely difficult manually.

### 2.2 Proposed System

The proposed system is a web-based Gym Management System that digitizes all gym operations. It runs in a web browser and can be accessed from any device within the network.

**Advantages of the Proposed System:**

1. **Fast Data Access:** Information can be retrieved instantly using search and filter functions.
2. **Data Integrity:** A relational database ensures consistent and validated data storage.
3. **Automated Calculations:** Revenue totals, attendance counts, and membership statistics are computed automatically.
4. **Secure Access:** Password-protected login with hashed passwords ensures data security.
5. **Printable Reports:** Revenue, membership, and attendance reports can be generated and printed.
6. **User-Friendly Interface:** An intuitive dashboard with charts provides quick insights at a glance.

### 2.3 Feasibility Study

#### Technical Feasibility
The project uses well-established, open-source technologies (Python, Flask, MySQL, Bootstrap). All required software tools are freely available, and the development team possesses adequate technical skills to implement the system.

#### Operational Feasibility
The proposed system features an intuitive, easy-to-learn user interface. Gym administrators with basic computer knowledge can operate the system after minimal training. The system will significantly reduce the administrative burden compared to the existing manual processes.

#### Economic Feasibility
The project is built entirely using free and open-source tools and frameworks. It can run on standard hardware that most gyms already possess (a basic computer with internet connectivity). The development and maintenance cost is minimal, making it economically viable even for small gyms.

### 2.4 Hardware Requirements

| Component | Minimum Requirement |
|-----------|-------------------|
| Processor | Intel Core i3 or equivalent |
| RAM | 4 GB |
| Hard Disk | 10 GB free space |
| Monitor | Standard display |
| Keyboard & Mouse | Standard input devices |
| Network | LAN/Wi-Fi (for multi-device access) |

### 2.5 Software Requirements

| Software | Specification |
|----------|--------------|
| Operating System | Windows 10/11, Linux (Ubuntu 20.04+), or macOS |
| Programming Language | Python 3.8+ |
| Web Framework | Flask 2.x |
| Database | MySQL 8.0 / SQLite 3 |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3, Bootstrap 5.3, JavaScript |
| Charting Library | Chart.js 4 |
| Web Browser | Google Chrome / Mozilla Firefox |
| IDE | Visual Studio Code |
| Version Control | Git |

---

## CHAPTER 3: SYSTEM DESIGN

### 3.1 System Architecture

The Gym Management System follows the **Model-View-Controller (MVC)** architecture pattern, implemented through the Flask web framework. The architecture consists of three main layers:

- **Model Layer (models.py):** Defines the database schema using SQLAlchemy ORM. Each model class maps to a database table and encapsulates data access logic.
- **View Layer (templates/):** Jinja2 HTML templates render the user interface. Bootstrap 5 provides responsive styling, and Chart.js renders interactive visualizations.
- **Controller Layer (routes.py):** Flask route handlers process HTTP requests, interact with models, and render appropriate views.

```mermaid
flowchart LR
    A["🌐 Web Browser<br/>(Client)"] -->|HTTP Request| B["⚙️ Flask Server<br/>(routes.py)"]
    B -->|Query/Update| C["🗄️ SQLAlchemy ORM<br/>(models.py)"]
    C -->|SQL| D["💾 MySQL / SQLite<br/>Database"]
    B -->|Render| E["📄 Jinja2 Templates<br/>(templates/)"]
    E -->|HTML Response| A
    D -->|Result Set| C
```

### 3.2 ER Diagram

The following Entity-Relationship diagram shows all entities in the system and their relationships:

```mermaid
erDiagram
    USER {
        int id PK
        string username UK
        string email UK
        string password_hash
        string role
        datetime created_at
    }

    MEMBER {
        int id PK
        string first_name
        string last_name
        string email UK
        string phone
        text address
        string gender
        date date_of_birth
        date join_date
        string status
        int membership_plan_id FK
        datetime created_at
        datetime updated_at
    }

    MEMBERSHIP_PLAN {
        int id PK
        string name
        text description
        int duration_months
        decimal price
        text features
        string status
        datetime created_at
    }

    TRAINER {
        int id PK
        string first_name
        string last_name
        string email UK
        string phone
        string specialization
        int experience_years
        decimal salary
        date hire_date
        string status
        datetime created_at
    }

    PAYMENT {
        int id PK
        int member_id FK
        decimal amount
        datetime payment_date
        string payment_method
        string transaction_id
        string status
        text notes
        datetime created_at
    }

    ATTENDANCE {
        int id PK
        int member_id FK
        datetime check_in
        datetime check_out
        datetime created_at
    }

    MEMBERSHIP_PLAN ||--o{ MEMBER : "subscribes to"
    MEMBER ||--o{ PAYMENT : "makes"
    MEMBER ||--o{ ATTENDANCE : "records"
```

### 3.3 Data Flow Diagrams

#### Level 0 DFD (Context Diagram)

```mermaid
flowchart LR
    Admin["👤 Admin"] -->|"Login credentials,<br/>Member data,<br/>Payment data,<br/>Plan data"| System["🏋️ Gym Management<br/>System"]
    System -->|"Dashboard,<br/>Reports,<br/>Receipts,<br/>Member lists"| Admin
    System <-->|"Read/Write<br/>Data"| DB["💾 Database"]
```

#### Level 1 DFD

```mermaid
flowchart TD
    Admin["👤 Admin"]

    P1["1.0<br/>Authentication"]
    P2["2.0<br/>Member<br/>Management"]
    P3["3.0<br/>Trainer<br/>Management"]
    P4["4.0<br/>Plan<br/>Management"]
    P5["5.0<br/>Payment<br/>Management"]
    P6["6.0<br/>Attendance<br/>Management"]
    P7["7.0<br/>Report<br/>Generation"]

    DS1[("Users")]
    DS2[("Members")]
    DS3[("Trainers")]
    DS4[("Plans")]
    DS5[("Payments")]
    DS6[("Attendance")]

    Admin -->|"Credentials"| P1
    P1 -->|"Auth Token"| Admin
    P1 <-->|"Verify"| DS1

    Admin -->|"Member Data"| P2
    P2 <-->|"CRUD"| DS2
    P2 -->|"Member List"| Admin

    Admin -->|"Trainer Data"| P3
    P3 <-->|"CRUD"| DS3
    P3 -->|"Trainer List"| Admin

    Admin -->|"Plan Data"| P4
    P4 <-->|"CRUD"| DS4
    P4 -->|"Plan List"| Admin

    Admin -->|"Payment Data"| P5
    P5 <-->|"CRUD"| DS5
    P5 -->|"Receipt"| Admin

    Admin -->|"Check-in/out"| P6
    P6 <-->|"CRUD"| DS6
    P6 -->|"Attendance Log"| Admin

    Admin -->|"Report Request"| P7
    P7 -->|"Reports & Charts"| Admin
    P7 ---|"Read"| DS2
    P7 ---|"Read"| DS5
    P7 ---|"Read"| DS6
```

### 3.4 Use Case Diagram

```mermaid
flowchart LR
    Actor["👤 Admin"]

    UC1["🔐 Login / Logout"]
    UC2["📊 View Dashboard"]
    UC3["👥 Manage Members"]
    UC4["🏃 Manage Trainers"]
    UC5["📋 Manage Plans"]
    UC6["💰 Process Payments"]
    UC7["📅 Track Attendance"]
    UC8["📈 Generate Reports"]
    UC9["🧾 Print Receipt"]

    Actor --- UC1
    Actor --- UC2
    Actor --- UC3
    Actor --- UC4
    Actor --- UC5
    Actor --- UC6
    Actor --- UC7
    Actor --- UC8
    UC6 --- UC9

    UC3 -.->|"includes"| UC1
    UC6 -.->|"includes"| UC1
```

### 3.5 Database Design

#### Table: users

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique user identifier |
| username | VARCHAR(80) | UNIQUE, NOT NULL | Login username |
| email | VARCHAR(120) | UNIQUE, NOT NULL | User email address |
| password_hash | VARCHAR(256) | NOT NULL | Hashed password |
| role | VARCHAR(20) | DEFAULT 'admin' | User role (admin/staff) |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Account creation time |

#### Table: members

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique member identifier |
| first_name | VARCHAR(50) | NOT NULL | Member's first name |
| last_name | VARCHAR(50) | NOT NULL | Member's last name |
| email | VARCHAR(120) | UNIQUE, NOT NULL | Member email |
| phone | VARCHAR(20) | NOT NULL | Contact phone number |
| address | TEXT | NULLABLE | Residential address |
| gender | VARCHAR(10) | NULLABLE | male/female/other |
| date_of_birth | DATE | NULLABLE | Date of birth |
| join_date | DATE | DEFAULT CURRENT_DATE | Gym join date |
| photo | VARCHAR(256) | NULLABLE | Profile photo path |
| emergency_contact | VARCHAR(100) | NULLABLE | Emergency contact name |
| emergency_phone | VARCHAR(20) | NULLABLE | Emergency contact phone |
| status | VARCHAR(20) | DEFAULT 'active' | active/inactive/expired |
| membership_plan_id | INT | FOREIGN KEY → membership_plans(id) | Subscribed plan |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | DATETIME | ON UPDATE CURRENT_TIMESTAMP | Last update time |

#### Table: trainers

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique trainer identifier |
| first_name | VARCHAR(50) | NOT NULL | Trainer's first name |
| last_name | VARCHAR(50) | NOT NULL | Trainer's last name |
| email | VARCHAR(120) | UNIQUE, NOT NULL | Trainer email |
| phone | VARCHAR(20) | NOT NULL | Contact phone |
| specialization | VARCHAR(100) | NULLABLE | Training specialization |
| experience_years | INT | NULLABLE | Years of experience |
| salary | DECIMAL(10,2) | NULLABLE | Monthly salary |
| hire_date | DATE | NULLABLE | Date of hiring |
| status | VARCHAR(20) | DEFAULT 'active' | active/inactive |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Record creation time |

#### Table: membership_plans

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique plan identifier |
| name | VARCHAR(100) | NOT NULL | Plan name |
| description | TEXT | NULLABLE | Plan description |
| duration_months | INT | NOT NULL | Duration in months |
| price | DECIMAL(10,2) | NOT NULL | Plan price in ₹ |
| features | TEXT | NULLABLE | Features (newline-separated) |
| status | VARCHAR(20) | DEFAULT 'active' | active/inactive |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Creation time |

#### Table: payments

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique payment identifier |
| member_id | INT | FOREIGN KEY → members(id), ON DELETE CASCADE | Paying member |
| amount | DECIMAL(10,2) | NOT NULL | Payment amount in ₹ |
| payment_date | DATETIME | NULLABLE | Date of payment |
| payment_method | VARCHAR(20) | NOT NULL | cash/card/upi/online |
| transaction_id | VARCHAR(100) | NULLABLE | Transaction reference |
| status | VARCHAR(20) | DEFAULT 'completed' | completed/pending/failed |
| notes | TEXT | NULLABLE | Additional notes |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Record creation time |

#### Table: attendance

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique record identifier |
| member_id | INT | FOREIGN KEY → members(id), ON DELETE CASCADE | Member checking in |
| check_in | DATETIME | NOT NULL | Check-in timestamp |
| check_out | DATETIME | NULLABLE | Check-out timestamp |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Record creation time |

### 3.6 Module Design

| Module | Description | Inputs | Outputs |
|--------|-------------|--------|---------|
| **Authentication** | Handles secure login/logout using hashed passwords and session management | Username, Password | Auth session, Redirect |
| **Dashboard** | Displays key statistics, recent activities, and interactive charts | None (auto-loads) | Stats cards, Charts, Tables |
| **Member Management** | CRUD operations for gym members with search and filtering | Member details | Member list, Profile view |
| **Trainer Management** | CRUD operations for trainer records | Trainer details | Trainer list |
| **Plan Management** | CRUD operations for membership plans with pricing | Plan details | Plan cards with member counts |
| **Payment Management** | Records payments, filters by date, generates printable receipts | Payment details | Payment list, Receipt |
| **Attendance** | Check-in/check-out tracking with daily logs | Member ID | Attendance log, Duration |
| **Reports** | Generates analytical reports with charts for revenue, membership, and attendance | Date range (optional) | Charts, Tables, Statistics |

---

## CHAPTER 4: IMPLEMENTATION

### 4.1 Implementation Environment

The application was developed and tested in the following environment:

- **OS:** Windows 11
- **IDE:** Visual Studio Code
- **Python:** 3.11+
- **Flask:** 3.x
- **Database:** SQLite (development) / MySQL 8.0 (production)
- **Browser:** Google Chrome 120+

### 4.2 Module-wise Implementation

#### 4.2.1 Authentication Module

The authentication module uses Flask-Login for session management and Werkzeug for password hashing. Passwords are never stored in plain text.

```python
# models.py — Password hashing
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```

```python
# routes.py — Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid username or password.", "danger")
    return render_template("login.html", form=form)
```

#### 4.2.2 Member Management Module

This module provides complete CRUD operations for gym members. Members can be searched by name, email, or phone number.

```python
# Adding a new member
@app.route("/members/add", methods=["GET", "POST"])
@login_required
def member_add():
    form = MemberForm()
    if form.validate_on_submit():
        member = Member(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            status=form.status.data,
            membership_plan_id=form.membership_plan_id.data or None,
        )
        db.session.add(member)
        db.session.commit()
        flash("Member added successfully.", "success")
        return redirect(url_for("members_list"))
    return render_template("members/form.html", form=form, title="Add Member")
```

#### 4.2.3 Payment Module

The payment module records transactions and generates printable receipts. Payments are linked to members via foreign keys.

```python
# Recording a payment
payment = Payment(
    member_id=form.member_id.data,
    amount=float(form.amount.data),
    payment_date=form.payment_date.data,
    payment_method=form.payment_method.data,
    transaction_id=form.transaction_id.data,
    status=form.status.data,
    notes=form.notes.data,
)
db.session.add(payment)
db.session.commit()
```

#### 4.2.4 Attendance Module

The attendance module provides quick check-in functionality and prevents duplicate check-ins for the same member on the same day.

```python
# Check-in with duplicate prevention
existing = Attendance.query.filter(
    Attendance.member_id == member_id,
    func.date(Attendance.check_in) == date.today(),
    Attendance.check_out.is_(None),
).first()

if existing:
    flash(f"{member.full_name} is already checked in today.", "warning")
else:
    record = Attendance(member_id=member_id, check_in=datetime.utcnow())
    db.session.add(record)
    db.session.commit()
```

#### 4.2.5 Dashboard Module

The dashboard aggregates data from all modules to present key metrics and interactive Chart.js visualizations.

```python
# Dashboard statistics
total_members = Member.query.count()
active_members = Member.query.filter_by(status="active").count()
revenue_this_month = db.session.query(
    func.coalesce(func.sum(Payment.amount), 0)
).filter(
    Payment.status == "completed",
    Payment.payment_date >= first_of_month
).scalar()
```

### 4.3 Database Connection

The application uses Flask-SQLAlchemy for database interaction. The connection is configured via the application factory pattern:

```python
# config.py
class Config:
    SECRET_KEY = "your-secret-key-change-in-production"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:password@localhost/gym_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# app.py
from models import db
db.init_app(app)
with app.app_context():
    db.create_all()
```

### 4.4 Key Implementation Details

- **CSRF Protection:** All forms include CSRF tokens via Flask-WTF to prevent cross-site request forgery attacks.
- **Input Validation:** WTForms validators ensure data integrity at the form level (required fields, email format, number ranges).
- **Flash Messages:** User feedback is provided through Flask's flash messaging system with Bootstrap alert styling.
- **Responsive Design:** Bootstrap 5's grid system ensures the UI adapts to different screen sizes.
- **Error Handling:** All route handlers use try/except blocks with database rollback to prevent data corruption on errors.

---

## CHAPTER 5: TESTING

### 5.1 Testing Methodology

The following testing approaches were used:

1. **Unit Testing:** Individual functions and model methods were tested in isolation.
2. **Integration Testing:** Interactions between modules (e.g., member creation → payment → receipt) were verified.
3. **System Testing:** The complete application was tested end-to-end to validate all workflows.
4. **User Acceptance Testing (UAT):** The application was demonstrated to potential users (gym administrators) for feedback.

### 5.2 Test Cases

| Test Case ID | Module | Test Description | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|---|---|
| TC001 | Login | Valid login | admin / admin123 | Redirect to dashboard | Redirected to dashboard | ✅ Pass |
| TC002 | Login | Invalid password | admin / wrong | Error message displayed | "Invalid username or password" | ✅ Pass |
| TC003 | Login | Empty fields | (blank) | Validation error | "This field is required" | ✅ Pass |
| TC004 | Member | Add new member | Valid member data | Member created, success flash | Member added successfully | ✅ Pass |
| TC005 | Member | Edit member | Updated email | Member updated, redirected | Member updated successfully | ✅ Pass |
| TC006 | Member | Delete member | Confirm delete | Member removed from list | Member deleted successfully | ✅ Pass |
| TC007 | Member | Search member | Search "John" | Matching members shown | Filtered list displayed | ✅ Pass |
| TC008 | Trainer | Add trainer | Valid trainer data | Trainer created | Trainer added successfully | ✅ Pass |
| TC009 | Trainer | Delete trainer | Confirm delete | Trainer removed | Trainer deleted successfully | ✅ Pass |
| TC010 | Plan | Add plan | Name, price, duration | Plan created | Plan added successfully | ✅ Pass |
| TC011 | Plan | Delete plan with members | Delete assigned plan | Warning message | "Cannot delete plan — it still has members" | ✅ Pass |
| TC012 | Payment | Add payment | Member, amount, method | Payment recorded | Payment recorded successfully | ✅ Pass |
| TC013 | Payment | View receipt | Click receipt icon | Printable receipt page | Receipt displayed with print button | ✅ Pass |
| TC014 | Attendance | Check-in member | Select member, check in | Attendance recorded | Member checked in successfully | ✅ Pass |
| TC015 | Attendance | Duplicate check-in | Same member, same day | Warning message | "Member is already checked in today" | ✅ Pass |
| TC016 | Attendance | Check-out | Click check out | Check-out time recorded | Check-out recorded | ✅ Pass |
| TC017 | Dashboard | Load dashboard | Navigate to / | Stats and charts displayed | All stats and charts rendered | ✅ Pass |
| TC018 | Reports | Revenue report | Date range filter | Filtered revenue data | Correct revenue displayed | ✅ Pass |
| TC019 | Reports | Membership report | Navigate to report | Plan distribution shown | Charts and tables rendered | ✅ Pass |
| TC020 | Auth | Access without login | Direct URL to /members | Redirect to login | Redirected to login page | ✅ Pass |

### 5.3 Testing Results Summary

All 20 test cases passed successfully. The application handles both valid and invalid inputs correctly, provides appropriate user feedback through flash messages, and maintains data integrity through validation and error handling.

---

## CHAPTER 6: SCREENSHOTS / OUTPUT

> **Note:** The following descriptions outline each page of the application. Actual screenshots can be captured by running the application (`python app.py`) and navigating to `http://localhost:5000`.

### 6.1 Login Page
A clean, centered login card on a gradient background. Contains the GYM MANAGER logo with a dumbbell icon, username and password input fields with icons, and a "Log In" button.

### 6.2 Dashboard
Features four stat cards (Total Members, Active Members, Monthly Revenue, Today's Check-ins) across the top. Below are two Chart.js visualizations: a bar chart for Membership Overview and a line chart for Revenue Trend. The bottom row contains two tables showing Recent Members and Recent Payments.

### 6.3 Members List
A searchable, sortable table listing all gym members with columns for Name, Email, Phone, Plan, Join Date, Status (color-coded badge), and action buttons (View, Edit, Delete).

### 6.4 Add/Edit Member Form
A two-column form in a card layout with fields for personal information (name, email, phone, gender, DOB), membership details (join date, plan, status), and emergency contact information.

### 6.5 Member Profile
Displays complete member information in a two-column layout, followed by Payment History and Attendance History tables.

### 6.6 Trainers List
Similar to the members list, showing trainer details including specialization, experience years, and salary.

### 6.7 Membership Plans
A card-based layout where each plan is displayed as a pricing card with the plan name, price, duration, features (checkmarked list), member count badge, and Edit/Delete buttons.

### 6.8 Payments List
A date-filterable table of all payments showing member name, amount (₹), date, payment method (badge), transaction ID, and status. Includes a total row at the bottom.

### 6.9 Payment Receipt
A standalone printable page with the gym's name and address, receipt number, payment details in a clean table format, and Print/Back buttons (hidden during printing).

### 6.10 Attendance Page
Includes a date filter, a Quick Check-in section with a member dropdown and Check In button, and a table showing today's attendance with Check Out buttons for active sessions.

### 6.11 Reports Dashboard
Three report category cards (Revenue, Membership, Attendance) with summary statistics and "View Report" buttons. Each sub-report includes interactive Chart.js charts and detailed data tables.

---

## CHAPTER 7: CONCLUSION AND FUTURE SCOPE

### 7.1 Conclusion

The **Gym Management System** has been successfully developed as a comprehensive web-based application that automates the core operations of a fitness center. The system replaces manual, paper-based processes with a centralized digital platform that is efficient, accurate, and user-friendly.

Key accomplishments of this project include:
- Secure authentication system with hashed passwords.
- Complete CRUD operations for members, trainers, and membership plans.
- Payment recording with printable receipt generation.
- Real-time attendance tracking with duplicate check-in prevention.
- Interactive analytics dashboard with Chart.js visualizations.
- Responsive UI that works across desktop and mobile devices.

The project demonstrates the practical application of full-stack web development using Python Flask, SQLAlchemy ORM, Bootstrap 5, and modern JavaScript libraries. The MVC architecture ensures maintainability and scalability.

### 7.2 Limitations

1. **Single Admin Role:** The current system does not support role-based access control (e.g., separate staff and trainer portals).
2. **No Online Payment Gateway:** Payments are recorded manually; there is no integration with online payment services like Razorpay or Stripe.
3. **No Notification System:** The system does not send automated email or SMS alerts for membership expiry or payment dues.
4. **No Mobile App:** The system is web-only and does not have a dedicated mobile application.
5. **Single Branch:** The system is designed for a single gym location and does not support multi-branch management.

### 7.3 Future Enhancements

1. **Mobile Application:** Develop a companion mobile app using Flutter or React Native for members to view their profiles, attendance, and payments.
2. **Email/SMS Notifications:** Integrate email and SMS APIs to send automated alerts for membership expiry, payment reminders, and promotional offers.
3. **Online Registration Portal:** Allow potential members to register and purchase membership plans online through a public-facing portal.
4. **Payment Gateway Integration:** Integrate Razorpay or Stripe for secure online payment processing.
5. **Biometric Attendance:** Integrate fingerprint or facial recognition devices for automated attendance tracking.
6. **Diet & Workout Plans:** Add modules for creating and assigning personalized diet and workout plans to members.
7. **Trainer-Member Assignment:** Enable assigning specific trainers to members based on specialization and availability.
8. **Multi-Branch Support:** Extend the system to manage multiple gym branches from a single admin panel.
9. **Role-Based Access Control:** Implement granular permissions for admin, staff, and trainer roles.
10. **Advanced Analytics with ML:** Use machine learning to predict membership churn, suggest optimal pricing, and analyze attendance patterns.

---

## REFERENCES / BIBLIOGRAPHY

1. Flask Documentation — https://flask.palletsprojects.com/
2. SQLAlchemy Documentation — https://docs.sqlalchemy.org/
3. Flask-Login Documentation — https://flask-login.readthedocs.io/
4. Flask-WTF Documentation — https://flask-wtf.readthedocs.io/
5. Bootstrap 5 Documentation — https://getbootstrap.com/docs/5.3/
6. Chart.js Documentation — https://www.chartjs.org/docs/
7. Python Official Documentation — https://docs.python.org/3/
8. MySQL Documentation — https://dev.mysql.com/doc/
9. W3Schools — https://www.w3schools.com/
10. Sumit Arora, "Flask Web Development with Python", Packt Publishing, 2023.
11. Ben Forta, "MySQL Crash Course", Sams Publishing, 2020.

---

## APPENDIX

### Project File List

| File | Purpose |
|------|---------|
| `app.py` | Application entry point and factory |
| `config.py` | Flask configuration settings |
| `models.py` | SQLAlchemy database models (User, Member, Trainer, MembershipPlan, Payment, Attendance) |
| `routes.py` | All Flask route handlers (29 routes) |
| `forms.py` | WTForms form classes (6 forms) |
| `requirements.txt` | Python package dependencies |
| `.gitignore` | Git ignore rules |
| `database/gym_db.sql` | MySQL database schema with sample data |
| `static/css/style.css` | Custom CSS styles (sidebar, dashboard, cards, forms, responsive) |
| `static/js/main.js` | Custom JavaScript (sidebar toggle, charts, DataTables, flash dismiss) |
| `templates/base.html` | Base layout template with sidebar and navbar |
| `templates/login.html` | Login page (standalone) |
| `templates/dashboard.html` | Dashboard with stats and charts |
| `templates/members/list.html` | Members list page |
| `templates/members/form.html` | Add/Edit member form |
| `templates/members/view.html` | Member profile page |
| `templates/trainers/list.html` | Trainers list page |
| `templates/trainers/form.html` | Add/Edit trainer form |
| `templates/plans/list.html` | Membership plans page (cards) |
| `templates/plans/form.html` | Add/Edit plan form |
| `templates/payments/list.html` | Payments list page |
| `templates/payments/form.html` | Add payment form |
| `templates/payments/receipt.html` | Printable payment receipt |
| `templates/attendance/list.html` | Attendance page with check-in |
| `templates/reports/dashboard.html` | Reports overview |
| `templates/reports/revenue.html` | Revenue report |
| `templates/reports/membership.html` | Membership report |
| `templates/reports/attendance.html` | Attendance report |

---

*Report prepared as part of Mini Project for Academic Year 2026–2027*
