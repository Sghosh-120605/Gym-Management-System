# 🏋️ Gym Management System

A comprehensive web-based **Gym Management System** built with Python Flask for managing gym operations including member management, trainer management, membership plans, payments, attendance tracking, and reporting.

---

## ✨ Features

- 🔐 **Secure Admin Authentication** — Login/logout with hashed passwords
- 👥 **Member Management** — Add, edit, view, search, and delete gym members
- 🏃 **Trainer Management** — Manage trainers with specialization and salary tracking
- 📋 **Membership Plans** — Create flexible plans (monthly, quarterly, yearly)
- 💰 **Payment & Billing** — Record payments, generate printable receipts
- 📅 **Attendance Tracking** — Quick check-in/check-out with daily logs
- 📊 **Reports & Analytics** — Revenue, membership, and attendance reports with charts
- 📱 **Responsive Design** — Works on desktop, tablet, and mobile

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.x, Flask |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Database** | MySQL / SQLite (fallback) |
| **ORM** | Flask-SQLAlchemy |
| **Auth** | Flask-Login |
| **Forms** | Flask-WTF / WTForms |
| **Charts** | Chart.js 4 |
| **Tables** | DataTables |
| **Icons** | Font Awesome 6 |

---

## 📂 Project Structure

```
Gym-Management-System/
├── app.py                  # Application entry point
├── config.py               # Flask configuration
├── models.py               # SQLAlchemy database models
├── routes.py               # All Flask routes
├── forms.py                # WTForms form classes
├── requirements.txt        # Python dependencies
├── .gitignore
│
├── database/
│   └── gym_db.sql          # MySQL schema + sample data
│
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   ├── js/
│   │   └── main.js         # Custom JavaScript
│   └── images/
│
├── templates/
│   ├── base.html           # Base layout (sidebar + navbar)
│   ├── login.html          # Login page
│   ├── dashboard.html      # Dashboard with stats & charts
│   ├── members/
│   │   ├── list.html       # Members list
│   │   ├── form.html       # Add/Edit member
│   │   └── view.html       # Member profile
│   ├── trainers/
│   │   ├── list.html       # Trainers list
│   │   └── form.html       # Add/Edit trainer
│   ├── plans/
│   │   ├── list.html       # Plans (card layout)
│   │   └── form.html       # Add/Edit plan
│   ├── payments/
│   │   ├── list.html       # Payments list
│   │   ├── form.html       # Add payment
│   │   └── receipt.html    # Printable receipt
│   ├── attendance/
│   │   └── list.html       # Attendance + check-in
│   └── reports/
│       ├── dashboard.html  # Reports overview
│       ├── revenue.html    # Revenue report
│       ├── membership.html # Membership report
│       └── attendance.html # Attendance report
│
└── documentation/
    └── Gym_Management_System_Report.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server (optional — SQLite works as fallback)
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Sghosh-120605/Gym-Management-System.git
cd Gym-Management-System

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. (Optional) Set up MySQL database
# Run the SQL file in MySQL:
mysql -u root -p < database/gym_db.sql
# Then update SQLALCHEMY_DATABASE_URI in config.py

# 6. Run the application
python app.py

# 7. Open browser
# Navigate to http://localhost:5000
```

### Default Login Credentials

| Username | Password |
|----------|----------|
| `admin` | `admin123` |

---

## 📸 Screenshots

| Page | Description |
|------|-------------|
| **Login** | Clean login page with gradient background |
| **Dashboard** | Stat cards, charts, recent members & payments |
| **Members** | Searchable, sortable member list with CRUD |
| **Trainers** | Trainer list with specialization & salary |
| **Plans** | Card-based pricing layout |
| **Payments** | Date-filterable payment list with totals |
| **Receipt** | Printable payment receipt |
| **Attendance** | Quick check-in/out with daily log |
| **Reports** | Revenue, membership & attendance analytics |

---

## 🗃️ Database Schema

| Table | Description |
|-------|-------------|
| `users` | Admin/staff authentication |
| `members` | Gym member profiles |
| `trainers` | Trainer information |
| `membership_plans` | Plan definitions (name, price, duration) |
| `payments` | Payment transaction records |
| `attendance` | Check-in/check-out logs |

---

## 🔮 Future Enhancements

- 📱 Mobile app integration
- 📧 Email/SMS notifications for expiry & dues
- 🌐 Online membership registration portal
- 💳 Payment gateway integration (Razorpay/Stripe)
- 🔒 Biometric attendance integration
- 🍎 Diet & workout plan management
- 👨‍🏫 Trainer-member assignment system
- 🏢 Multi-branch support
- 👮 Role-based access control (admin/staff/trainer)
- 📈 Advanced analytics with ML predictions

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

**Made with ❤️ using Flask**
