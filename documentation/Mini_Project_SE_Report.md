# MINI PROJECT SE

---

## Project Title

**Gym Management System**

---

## Student Details

- **Student Name(s):** __________
- **Enrollment Number(s):** __________
- **Course / Semester:** __________
- **Subject:** Software Engineering

---

## Abstract (100–120 words)

Managing gym operations manually using paper registers and spreadsheets leads to data inconsistency, delayed record retrieval, and error-prone billing. This project presents a **Gym Management System** — a web-based application built using **Python Flask**, **SQLAlchemy ORM**, and **MySQL/SQLite** database, with a responsive frontend using **Bootstrap 5** and **Chart.js**. The system automates member registration, trainer management, membership plan creation, payment processing with printable receipts, real-time attendance tracking (check-in/check-out), and analytical report generation with interactive charts. It follows the **MVC architecture** pattern, ensuring clean separation of concerns. The application provides a secure admin dashboard with hashed password authentication, enabling gym administrators to efficiently manage all operations from a single centralized platform.

---

## Problem Statement

Most small and medium-sized gyms rely on manual, paper-based record-keeping for managing memberships, payments, attendance, and trainer information. This approach is time-consuming, error-prone, lacks real-time insights, and does not scale as membership grows. There is no centralized system for tracking dues, generating revenue reports, or monitoring attendance patterns. The project aims to solve these problems by developing a comprehensive, web-based Gym Management System that digitizes and automates all core gym operations.

---

## Objectives

- To develop a secure, web-based application for automating gym management operations.
- To implement CRUD operations for managing members, trainers, and membership plans.
- To build a payment and billing module with printable receipt generation.
- To enable real-time attendance tracking with check-in/check-out functionality.
- To generate analytical reports (revenue, membership, attendance) with interactive Chart.js visualizations.
- To provide a responsive admin dashboard summarizing key gym metrics at a glance.

---

## Methodology / Approach

The system follows the **Model-View-Controller (MVC)** architecture using the Flask web framework.

### System Architecture

```
Client (Browser) → Flask Server (routes.py) → SQLAlchemy ORM (models.py) → MySQL/SQLite Database
                                             → Jinja2 Templates (templates/) → HTML Response
```

### ER Diagram

The database consists of **6 entities** with the following relationships:

```
MEMBERSHIP_PLAN ||--o{ MEMBER : "subscribes to"
MEMBER ||--o{ PAYMENT : "makes"
MEMBER ||--o{ ATTENDANCE : "records"
```

**Entities:** User (admin authentication), Member (gym members with personal details, plan, status), Trainer (specialization, salary), MembershipPlan (name, duration, price, features), Payment (amount, method, transaction ID, status), Attendance (check-in/check-out timestamps).

### Data Flow Diagram (Level 0 — Context Diagram)

```
Admin → [Login credentials, Member/Payment/Plan data] → GYM MANAGEMENT SYSTEM
GYM MANAGEMENT SYSTEM → [Dashboard, Reports, Receipts, Lists] → Admin
GYM MANAGEMENT SYSTEM ↔ [Read/Write] ↔ Database
```

### Level 1 DFD — Key Processes

| Process | Description |
|---------|-------------|
| 1.0 Authentication | Verifies admin credentials using hashed passwords (Werkzeug) |
| 2.0 Member Management | CRUD operations with search/filter on members |
| 3.0 Trainer Management | CRUD operations on trainer records |
| 4.0 Plan Management | Create/edit membership plans with pricing |
| 5.0 Payment Management | Record payments, generate receipts |
| 6.0 Attendance Management | Check-in/check-out with duplicate prevention |
| 7.0 Report Generation | Revenue, membership & attendance analytics with charts |

### Use Case Diagram

**Actor:** Admin → Use Cases: Login/Logout, View Dashboard, Manage Members, Manage Trainers, Manage Plans, Process Payments, Track Attendance, Generate Reports, Print Receipt.

### Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Flask, Flask-Login, Flask-WTF |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript, Chart.js |
| Database | MySQL 8.0 / SQLite 3 |
| ORM | Flask-SQLAlchemy |

---

## Implementation & Output

### Key Features

- **Secure Admin Login** — Password hashing with Werkzeug, session-based auth via Flask-Login
- **Member Management** — Add, edit, view profile, search, delete members with plan assignment
- **Trainer Management** — Manage trainers with specialization, experience, and salary tracking
- **Membership Plans** — Card-based pricing layout with plan features and member count
- **Payment & Billing** — Record payments (Cash/Card/UPI/Online), printable receipts
- **Attendance Tracking** — Quick check-in/check-out, duplicate prevention, daily logs
- **Dashboard** — 4 stat cards (Total Members, Active Members, Revenue, Check-ins) + Chart.js bar & line charts
- **Reports** — Revenue report (monthly breakdown), Membership report (plan/status/gender distribution), Attendance report (daily trends, top members)
- **Responsive UI** — Dark sidebar admin theme, works on desktop & mobile

### Screenshots

| Page | Description |
|------|-------------|
| Login | Centered card with gradient background, dumbbell icon |
| Dashboard | Stat cards + membership bar chart + revenue line chart + recent tables |
| Members | Searchable DataTable with status badges, view/edit/delete actions |
| Plans | Card-based pricing layout with features checklist |
| Payments | Date-filterable list with total, receipt generation |
| Attendance | Quick check-in dropdown + daily log with check-out buttons |
| Reports | Revenue/Membership/Attendance analytics with Chart.js |

---

## Results

- Successfully developed a fully functional Gym Management System with **29 routes** and **15 HTML templates**.
- All **13 major pages** tested and verified — **13/13 passed** (HTTP 200).
- System handles **6 database entities** with proper relationships and cascading deletes.
- Dashboard provides real-time statistics and interactive charts.
- Payment receipts are printable directly from the browser.
- Attendance module prevents duplicate check-ins for the same member on the same day.

---

## Conclusion

- **Learning Outcomes:** Gained practical experience in full-stack web development using Flask, SQLAlchemy ORM, Jinja2 templating, Bootstrap responsive design, Chart.js data visualization, and secure authentication with password hashing.
- **Summary:** The Gym Management System successfully automates member registration, trainer management, plan management, payment processing, attendance tracking, and report generation. It replaces error-prone manual processes with a centralized, efficient digital platform accessible via any web browser.

---

## Future Scope

- Online membership registration portal for members
- Payment gateway integration (Razorpay/Stripe)
- Email/SMS notifications for expiry & dues reminders
- Mobile app using Flutter/React Native
- Biometric attendance integration
- Diet & workout plan management module
- Multi-branch gym support
- Role-based access control (Admin/Staff/Trainer)

---

## Mapped SDG

**SDG 3: Good Health and Well-being** — The system promotes fitness center management efficiency, enabling gyms to serve more members effectively and contribute to community health and well-being.

---

## GitHub Repository

- **Project Link:** https://github.com/Sghosh-120605/Gym-Management-System

---

## 📱 QR Code (Scanner for GitHub)

*[Insert QR Code here — Generate using any QR generator for your GitHub repository link]*

---
