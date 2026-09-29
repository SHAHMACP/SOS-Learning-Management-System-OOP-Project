# ============================================================
#           SOS - SCHOOL OF SKILLS
#         LEARNING MANAGEMENT SYSTEM (LMS)
#                  demo_data.py
# ============================================================
#
# Fills the LMS with sample students, attendance, grades,
# fee installments, course syllabi and certificates so the
# analytics dashboard has data to show during a demo.
#
# Triggered by the "Load Demo Data" button in the sidebar.
# All names below are fictional.
# ============================================================

import random
from datetime import date, timedelta

from sos import Course, Faculty, Student, PAYMENT_MODES


# {course_id: [(module title, [(lesson, type, description, minutes)])]}
SAMPLE_CONTENT = {
    "C001": [
        ("Python for Data Science", [
            ("Setting up Python and Jupyter", "Video", "Install tools and run your first notebook.", 20),
            ("Variables, loops and functions", "Reading", "Core Python syntax with worked examples.", 30),
            ("Warm-up exercises", "Assignment", "Ten short problems to practise the basics.", 45),
        ]),
        ("Data Analysis with Pandas", [
            ("Loading and cleaning data", "Video", "Read CSV files and fix missing values.", 25),
            ("Grouping and summarising", "Reading", "groupby, pivot tables and aggregation.", 30),
            ("Module quiz", "Quiz", "Ten questions on Pandas.", 15),
        ]),
    ],
    "C002": [
        ("Design Fundamentals", [
            ("Elements of fashion design", "Video", "Line, shape, colour and texture.", 25),
            ("Colour theory", "Reading", "Palettes, contrast and seasonal colours.", 20),
            ("Mood board", "Assignment", "Create a mood board for a capsule collection.", 60),
        ]),
        ("Pattern Making", [
            ("Taking measurements", "Video", "Body measurement and size charts.", 20),
            ("Drafting a basic bodice", "Reading", "Step-by-step drafting guide.", 40),
            ("Module quiz", "Quiz", "Terminology and measurement check.", 15),
        ]),
    ],
    "C003": [
        ("HR Foundations", [
            ("Role of HR in an organisation", "Video", "Functions and structure of HR.", 20),
            ("Recruitment and selection", "Reading", "Sourcing, screening and interviews.", 30),
            ("Job description exercise", "Assignment", "Write a job description for a real role.", 40),
        ]),
        ("Employee Relations", [
            ("Performance management", "Video", "Appraisals and feedback cycles.", 25),
            ("Labour law basics", "Reading", "Key acts every HR executive should know.", 35),
            ("Module quiz", "Quiz", "Ten scenario-based questions.", 15),
        ]),
    ],
}

# (id, name, phone, age, [(course_id, fraction of fee paid, attendance
#  probability, grade)])
SAMPLE_STUDENTS = [
    ("DSA01", "MUHAMMED ROSHAN P", "8606333217", 21, [("C001", 0.5, 0.95, "A")]),
    ("DSA02", "ANJALI S", "9847012345", 22, [("C001", 1.0, 1.0, "A+"), ("C003", 0.5, 0.9, "B+")]),
    ("DSA03", "RAHUL KRISHNAN", "9946123456", 24, [("C001", 0.0, 0.7, None)]),
    ("FSH01", "MEERA PILLAI", "9895234567", 21, [("C002", 1.0, 1.0, "A")]),
    ("FSH02", "FATHIMA NAZRIN", "9633345678", 20, [("C002", 0.4, 0.85, "B")]),
    ("FSH03", "ADIL HASSAN", "9048678901", 25, [("C002", 0.0, 0.9, "B+")]),
    ("HRM01", "ARUN KUMAR", "9744456789", 26, [("C003", 1.0, 0.9, "A"), ("C001", 0.3, 0.8, "B")]),
    ("HRM02", "SNEHA MENON", "9526567890", 23, [("C003", 0.6, 0.65, "C")]),
]


def _ensure_faculty(activities):
    """Add one more faculty member and give every course a teacher."""

    known_ids = {f.faculty_id for f in Faculty.faculty_list}

    if "F003" not in known_ids:
        Faculty("F003", "Mr. ARJUN NAIR", "FASHION DESIGNING", "M.Des", 5)

    by_id = {f.faculty_id: f for f in Faculty.faculty_list}

    for faculty_id, course_id in (("F001", "C001"),
                                  ("F003", "C002"),
                                  ("F002", "C003")):
        faculty = by_id.get(faculty_id)
        course = Course.get_by_id(course_id)

        if faculty and course and course.assigned_faculty is None:
            activities.assign_faculty(faculty, course)


def _ensure_content():
    """Give each sample course a syllabus if it has none."""

    for course_id, modules in SAMPLE_CONTENT.items():
        course = Course.get_by_id(course_id)

        if course is None or course.total_lessons() > 0:
            continue

        for module_title, lessons in modules:
            module = course.add_module(module_title)

            for title, lesson_type, content, minutes in lessons:
                course.add_lesson(
                    module["id"], title, lesson_type, content, minutes
                )


def load_demo_data(students, activities):
    """Populate the LMS. `students` is the app's student list."""

    rng = random.Random(2026)
    today = date.today()

    # Ten class sessions, about six days apart (spans 2+ months)
    sessions = [today - timedelta(days=6 * k) for k in range(10)]

    _ensure_faculty(activities)
    _ensure_content()

    # ---------- Faculty attendance ----------
    faculty_presence = {"F001": 0.95, "F002": 0.85, "F003": 0.9}

    for faculty in Faculty.faculty_list:
        chance = faculty_presence.get(faculty.faculty_id, 0.9)

        for day in sessions:
            faculty.mark_attendance(str(day), rng.random() < chance)

    # ---------- Students ----------
    existing = {s.student_id: s for s in students}

    for student_id, name, phone, age, enrollments in SAMPLE_STUDENTS:

        student = existing.get(student_id)

        if student is None:
            student = Student(student_id, name, phone, age)
            students.append(student)
            existing[student_id] = student

        for index, (course_id, fee_fraction, attendance_chance, grade) \
                in enumerate(enrollments):

            course = Course.get_by_id(course_id)

            if course is None:
                continue

            # ----- Enrollment + fee installments -----
            total_paid = int(course.fee * fee_fraction)
            first_part = int(total_paid * 0.6)
            mode = PAYMENT_MODES[(sum(map(ord, student_id)) + index) % len(PAYMENT_MODES)]
            first_date = today - timedelta(days=rng.randint(40, 55))

            success, _ = activities.enroll_student(
                student, course, first_part, mode, first_date
            )

            if not success:
                continue

            if total_paid - first_part > 0:
                activities.pay_fee(
                    student,
                    course,
                    total_paid - first_part,
                    rng.choice(PAYMENT_MODES),
                    today - timedelta(days=rng.randint(1, 30))
                )

            # ----- Attendance -----
            for day in sessions:
                activities.mark_attendance(
                    student, course, str(day),
                    rng.random() < attendance_chance
                )

            # ----- Grade + certificate -----
            if grade:
                activities.record_grade(student, course, grade)

                if attendance_chance == 1.0:
                    activities.issue_certificate(student, course)
