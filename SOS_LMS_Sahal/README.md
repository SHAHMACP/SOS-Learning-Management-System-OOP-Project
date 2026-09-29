# 🏫 SOS - School Of Skills
### Enterprise Academic Governance & Vocational Management System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![UI-Theme](https://img.shields.io/badge/Theme-Red%20%26%20White-DC2626.svg)](#-design-system--brand-identity)
[![Architecture](https://img.shields.io/badge/Architecture-Clean%20OOP-success.svg)](#-system-architecture)

---

## 📌 Overview

**SOS - School Of Skills** is an enterprise-grade educational management web application crafted for vocational academies, tech skill hubs, and training institutes. It centralizes student admissions, multi-batch scheduling, rapid class attendance logging, fee ledger accounting with digital receipt issuance, campus announcements, and live visual analytics into a unified, high-performance portal.

Built with a strict **Separation of Concerns (SoC)**, the project pairs a pure Object-Oriented domain business engine in Python with a bespoke, accessible **Red & White** modern web dashboard powered by Streamlit.

---

## ✨ Key Features & Modules

### 1. 📊 Centralized Dashboard & Live KPIs
- **Hero App Bar**: Branded top banner with institution logo, clean heading, and live session status indicator (`🟢 2026 SESSION LIVE`).
- **4 Floating Metric Cards**: Real-time aggregated stats for Total Enrolled Students, Faculty & Staff, Active Programs, and Fees Collected.
- **Active Programs Grid**: High-elevation cards displaying program faculty lead, capacity, duration, and tuition.
- **Campus Notice Board**: Live stream of campus announcements with category badges (`Event`, `Urgent`, `General`, `Exam`).

### 2. 🎓 Academic Programs & Curriculum
- Comprehensive catalog tracking duration, syllabus department, fees, and assigned mentors.
- **Current Live Curriculums**:
  - `DSA - Data Scientist And Analyst` (6 months • ₹70,000/-) — Mentor: **Vyshak**
  - `HR - Human Resource` (4 months • ₹50,000/-) — Mentor: **Diya**
  - `FAD - Fashion Design` (6 months • ₹80,000/-) — Mentor: **Shahma C.P**
  - `AI - Agent K` (6 months • ₹80,000/-) — Mentor: **Rinshin**
  - `Spoken English` (3 months • ₹25,000/-) — Mentor: **Ashraf**

### 3. 👥 Faculty & Operations Directory
- Multi-role directory covering Teachers, Student Coordinators, Media Team, and Accountants.
- Search and filter staff by name and department role.
- Employee onboarding with unique credential verification and attendance history.
- **Staff Team**: Vyshak, Shahma C.P, Rinshin, Ashraf, Diya, Soniya, Rahul Nair, Fathima K, Suresh Babu.

### 4. 👨‍🎓 Student Admissions & Roster
- Complete student registry filterable by Program, Section/Cohort (`Batch A`, `Batch B`), and Status (`Active`, `Not Enrolled`).
- Registration & admission flow with automatic course fee assignment.
- Detailed learner profile inspection (contact details, academic records, fee ledger, and attendance rate).

### 5. 📅 High-Efficiency Attendance Hub
- **1-Click Class Roster Attendance**: Select Program and Batch to instantly populate the full class roster with interactive checkboxes for one-click bulk saving.
- **Individual Student & Staff Loggers**: Date-validated logging with strict duplicate-date prevention.
- **Health Indicators**: Real-time percentage badges highlighting Good Standing ($\ge 75\%$) vs Academic Alert ($< 75\%$).

### 6. 💳 Fee Management & Digital Receipt Generation
- Live tuition accounting: instant computation of total contracted fee, paid revenue, and outstanding dues.
- Support for multiple payment methods: `UPI / GPay`, `Cash`, `Net Banking`, `Debit / Credit Card`.
- Overpayment prevention and validation against negative or zero entries.
- **Official Digital Payment Receipts**: Printable invoice-styled receipt cards featuring unique receipt IDs (e.g., `REC-2026-XXXX`), transaction timestamps, student metadata, payment mode tags, and remaining balances.

### 7. 📈 Visual Analytics & Interactive Insights
- **Financial Realization**: 4 KPI cards and comparative bar chart tracking **Collected (₹)** vs **Pending Dues (₹)** per program.
- **Class Attendance Comparison**: Interactive bar chart comparing average attendance rates across sections and batches.
- **Curriculum Density**: Enrollment distribution bar chart visualizing student density across all offered subjects.

### 8. ♻️ Recycle Bin & Soft Deletion
- Safety repository storing soft-deleted Staff, Programs, and Students.
- Instant 1-click **Restore** to active registries or permanent database purge.

---

## 🏗️ System Architecture

The project strictly follows clean architectural boundaries:

```
┌────────────────────────────────────────────────────────┐
│                   STREAMLIT WEB UI                     │
│                       (app.py)                         │
│  - Presentation layer, layout & viewport controls      │
│  - Red & White CSS stylesheet & selection bubble logic │
│  - Interactive forms, charts, tables, & digital badges │
└───────────────────────────┬────────────────────────────┘
                            │ Calls methods / reads data
                            ▼
┌────────────────────────────────────────────────────────┐
│               OOP BUSINESS DOMAIN LAYER                │
│                        (sos.py)                        │
│  - Pure Python (Zero UI dependencies)                  │
│  - Abstract Base Class: SOS                            │
│  - Entities: Staff, Teacher, Student, Program, Notice  │
│  - Activity Controller: SOSActivities                  │
│  - In-memory state, invariants & validation rules     │
└────────────────────────────────────────────────────────┘
```

---

## 🎨 Design System & Brand Identity

The application is styled with the institution's official **Red & White** branding:
- **Primary Brand Accent**: Crimson Red (`#DC2626` / `#B91C1C`)
- **Secondary Accents**: Ruby Red (`#E11D48`), Pure White (`#FFFFFF`), Soft Slate
- **Sidebar & Bubbles**: Deep crimson slate (`#170707`) with custom circular radio selection bubbles (`18px`) that glow on hover and turn into a solid red orb with an inner **6px pure white dot** when selected.
- **Buttons & Tabs**: Vibrant red gradient capsules with smooth elevation and tactile feedback.
- **Typography**: Clean *Plus Jakarta Sans* font stack with safeguarded Material Symbols glyphs.

---

## 📁 Repository Structure

```
.
├── .streamlit/
│   └── config.toml          # Streamlit theme configuration (Red & White palette)
├── app.py                   # Streamlit web app, routing, styling & line-by-line comments
├── sos.py                   # Pure Python OOP domain logic, entities & business rules
├── logo.png                 # Official SOS logo asset
├── requirements.txt         # Python package dependencies
├── DOCUMENTATION.md         # Full technical architectural specification
└── README.md                # Project overview and quickstart guide
```

---

## 🚀 Getting Started

### Prerequisites
- Python **3.10** or higher
- `pip` package manager

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create and Activate Virtual Environment (Recommended)

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Codebase Compilation
```bash
python -m py_compile app.py sos.py
```

### 5. Launch the Web Application
```bash
streamlit run app.py
```

Open your browser and navigate to:
```
http://localhost:8501
```

---

## 📖 Code Transparency Standard

Every line of production code in [`app.py`](app.py) is accompanied by a **line-by-line educational comment** explaining:
1. **What** the instruction does technically.
2. **Why** it exists at that specific step.
3. **What** happens to application state upon execution.

This ensures seamless onboarding, code reviews, and maintainability for developers of all experience levels.

---

## 🛠️ Built With

- **[Python](https://www.python.org/)** — Core programming language & OOP models
- **[Streamlit](https://streamlit.io/)** — Reactive web dashboard & components framework
- **[Pandas](https://pandas.pydata.org/)** — Data analysis, grouping, and tabular structures

---

## 📄 License & Attribution

Developed for **School of Skills (SOS)**, Calicut Campus (Established 2026).  
Licensed under the [MIT License](LICENSE).
