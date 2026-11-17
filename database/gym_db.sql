-- ============================================================
-- Gym Management System — Database Schema
-- File : gym_db.sql
-- Engine : MySQL 8.x
-- ============================================================

-- ---------------------------------------------------------
-- 1. Create & select the database
-- ---------------------------------------------------------
CREATE DATABASE IF NOT EXISTS gym_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE gym_db;

-- ---------------------------------------------------------
-- 2. Tables
-- ---------------------------------------------------------

-- 2a. Users (admin / staff login accounts)
CREATE TABLE IF NOT EXISTS users (
    id              INT             AUTO_INCREMENT PRIMARY KEY,
    username        VARCHAR(80)     UNIQUE NOT NULL,
    email           VARCHAR(120)    UNIQUE NOT NULL,
    password_hash   VARCHAR(256)    NOT NULL,
    role            ENUM('admin', 'staff') DEFAULT 'admin',
    created_at      TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2b. Membership Plans
CREATE TABLE IF NOT EXISTS membership_plans (
    id              INT             AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(100)    NOT NULL,
    description     TEXT,
    duration_months INT             NOT NULL,
    price           DECIMAL(10, 2)  NOT NULL,
    features        TEXT,
    status          ENUM('active', 'inactive') DEFAULT 'active',
    created_at      TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2c. Members
CREATE TABLE IF NOT EXISTS members (
    id                  INT             AUTO_INCREMENT PRIMARY KEY,
    first_name          VARCHAR(80)     NOT NULL,
    last_name           VARCHAR(80)     NOT NULL,
    email               VARCHAR(120)    UNIQUE NOT NULL,
    phone               VARCHAR(15),
    address             TEXT,
    gender              ENUM('male', 'female', 'other'),
    date_of_birth       DATE,
    join_date           DATE,
    photo               VARCHAR(256),
    emergency_contact   VARCHAR(100),
    emergency_phone     VARCHAR(15),
    status              ENUM('active', 'inactive', 'expired') DEFAULT 'active',
    membership_plan_id  INT,
    created_at          TIMESTAMP       DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP       DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_members_plan
        FOREIGN KEY (membership_plan_id) REFERENCES membership_plans(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- 2d. Trainers
CREATE TABLE IF NOT EXISTS trainers (
    id               INT             AUTO_INCREMENT PRIMARY KEY,
    first_name       VARCHAR(80)     NOT NULL,
    last_name        VARCHAR(80)     NOT NULL,
    email            VARCHAR(120)    UNIQUE NOT NULL,
    phone            VARCHAR(15),
    specialization   VARCHAR(150),
    experience_years INT,
    salary           DECIMAL(10, 2),
    hire_date        DATE,
    status           ENUM('active', 'inactive') DEFAULT 'active',
    created_at       TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2e. Payments
CREATE TABLE IF NOT EXISTS payments (
    id              INT             AUTO_INCREMENT PRIMARY KEY,
    member_id       INT             NOT NULL,
    amount          DECIMAL(10, 2)  NOT NULL,
    payment_date    DATE            NOT NULL,
    payment_method  ENUM('cash', 'card', 'upi', 'online') NOT NULL,
    transaction_id  VARCHAR(100),
    status          ENUM('completed', 'pending', 'failed') DEFAULT 'completed',
    notes           TEXT,
    created_at      TIMESTAMP       DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_payments_member
        FOREIGN KEY (member_id) REFERENCES members(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- 2f. Attendance
CREATE TABLE IF NOT EXISTS attendance (
    id          INT         AUTO_INCREMENT PRIMARY KEY,
    member_id   INT         NOT NULL,
    check_in    DATETIME    NOT NULL,
    check_out   DATETIME    NULL,
    created_at  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_attendance_member
        FOREIGN KEY (member_id) REFERENCES members(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------------------------
-- 3. Sample Data
-- ---------------------------------------------------------

-- 3a. Admin user  (username: admin / password: admin123)
--     Hash generated with: werkzeug.security.generate_password_hash('admin123')
INSERT INTO users (username, email, password_hash, role) VALUES
('admin', 'admin@gymapp.com',
 'pbkdf2:sha256:600000$XrLZKQpM8kVYJB1N$e3a0c68a1f4b2d9357f06b015e8c7435bfc8a19d6e72c5a438d19e2b7f5c0812',
 'admin');

-- 3b. Membership Plans
INSERT INTO membership_plans (name, description, duration_months, price, features, status) VALUES
('Basic Monthly',
 'Access to gym floor and basic equipment during regular hours.',
 1, 500.00,
 'Gym floor access, Locker facility, Basic equipment',
 'active'),

('Standard Quarterly',
 'Full gym access with group classes for three months.',
 3, 1200.00,
 'Full gym access, Group classes, Locker facility, Diet consultation',
 'active'),

('Premium Yearly',
 'All-inclusive annual membership with personal training sessions.',
 12, 4000.00,
 'Full gym access, Personal trainer, Group classes, Steam & Sauna, Diet plan, Locker facility, Guest passes (2/month)',
 'active');

-- 3c. Members
INSERT INTO members (first_name, last_name, email, phone, address, gender, date_of_birth, join_date, emergency_contact, emergency_phone, status, membership_plan_id) VALUES
('Rahul',   'Sharma',   'rahul.sharma@email.com',   '9876543210', '12 MG Road, Bengaluru',       'male',   '1995-04-12', '2026-01-10', 'Priya Sharma',   '9876543200', 'active',  2),
('Ananya',  'Patel',    'ananya.patel@email.com',    '9123456789', '45 Park Street, Mumbai',      'female', '1998-08-25', '2026-02-15', 'Vikram Patel',   '9123456780', 'active',  3),
('Vikram',  'Singh',    'vikram.singh@email.com',    '9988776655', '78 Civil Lines, Delhi',       'male',   '1992-11-03', '2026-03-01', 'Meera Singh',    '9988776600', 'active',  1),
('Priya',   'Reddy',    'priya.reddy@email.com',     '9871234567', '23 Jubilee Hills, Hyderabad', 'female', '2000-01-17', '2026-05-20', 'Suresh Reddy',   '9871234500', 'active',  2),
('Arjun',   'Nair',     'arjun.nair@email.com',      '9845678901', '9 Marine Drive, Kochi',       'male',   '1997-06-30', '2026-06-01', 'Lakshmi Nair',   '9845678900', 'expired', 1);

-- 3d. Trainers
INSERT INTO trainers (first_name, last_name, email, phone, specialization, experience_years, salary, hire_date, status) VALUES
('Deepak',  'Chauhan', 'deepak.chauhan@gym.com',  '9000000001', 'Weight Training & Strength',  8, 35000.00, '2023-06-15', 'active'),
('Sneha',   'Kapoor',  'sneha.kapoor@gym.com',    '9000000002', 'Yoga & Flexibility',          5, 28000.00, '2024-01-10', 'active'),
('Rohan',   'Mehta',   'rohan.mehta@gym.com',     '9000000003', 'Cardio & HIIT',               6, 30000.00, '2023-11-01', 'active');

-- 3e. Payments
INSERT INTO payments (member_id, amount, payment_date, payment_method, transaction_id, status, notes) VALUES
(1, 1200.00, '2026-01-10', 'upi',    'TXN20260110001', 'completed', 'Standard Quarterly — Q1 2026'),
(2, 4000.00, '2026-02-15', 'card',   'TXN20260215002', 'completed', 'Premium Yearly — full year'),
(3,  500.00, '2026-03-01', 'cash',   NULL,              'completed', 'Basic Monthly — March 2026'),
(4, 1200.00, '2026-05-20', 'online', 'TXN20260520004', 'completed', 'Standard Quarterly — Q2 2026'),
(5,  500.00, '2026-06-01', 'upi',    'TXN20260601005', 'completed', 'Basic Monthly — June 2026'),
(1, 1200.00, '2026-04-10', 'upi',    'TXN20260410006', 'completed', 'Standard Quarterly — Q2 2026 renewal'),
(3,  500.00, '2026-04-01', 'cash',   NULL,              'pending',   'Basic Monthly — April 2026 (pending)');

-- 3f. Attendance
INSERT INTO attendance (member_id, check_in, check_out) VALUES
(1, '2026-11-15 06:30:00', '2026-11-15 08:00:00'),
(2, '2026-11-15 07:00:00', '2026-11-15 08:30:00'),
(3, '2026-11-15 17:00:00', '2026-11-15 18:15:00'),
(1, '2026-11-16 06:45:00', '2026-11-16 08:10:00'),
(4, '2026-11-16 08:00:00', '2026-11-16 09:30:00'),
(2, '2026-11-16 07:15:00', '2026-11-16 08:45:00'),
(1, '2026-11-17 06:30:00', NULL),
(3, '2026-11-17 17:30:00', NULL),
(5, '2026-11-14 10:00:00', '2026-11-14 11:00:00'),
(4, '2026-11-17 08:15:00', '2026-11-17 09:45:00');

-- ============================================================
-- Done. Schema created with sample data.
-- ============================================================
