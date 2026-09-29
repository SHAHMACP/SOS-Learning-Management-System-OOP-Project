# ============================================================
#           SOS - SCHOOL OF SKILLS
#         LEARNING MANAGEMENT SYSTEM (LMS)
#                    sos.py
# ============================================================

from abc import ABC
from datetime import date


# ============================================================
#                    SHARED CONSTANTS
# ============================================================

GRADES = ["A+", "A", "B+", "B", "C", "Fail"]

PAYMENT_MODES = ["Cash", "UPI", "Card", "Bank Transfer"]

LESSON_TYPES = ["Video", "Reading", "Assignment", "Quiz"]

MIN_ATTENDANCE_FOR_CERTIFICATE = 75


# ============================================================
#                 1. INSTITUTION CLASS
# ============================================================

class Institution(ABC):

    # CLASS VARIABLES
    institution_name = "SOS - School of Skills"
    location = "Calicut"
    established_year = 2026
    Founder = "GOVINDH PADHMASURYA"
    contact_number = "1234567891"
    email = "info@sos-skills.edu"

    # INSTANCE METHOD - Display Institution Details
    def institution_details(self):

        return {
            "Institution Name": self.institution_name,
            "Location": self.location,
            "Established Year": self.established_year,
            "Founder": self.Founder,
            "Contact Number": self.contact_number,
            "Email": self.email
        }


# ============================================================
#                    2. COURSE CLASS
# ============================================================

class Course(Institution):

    # CLASS VARIABLE
    # Stores all Course objects
    courses_list = []

    def __init__(self, course_id, title, category,
                 duration_weeks, fee, max_seats):

        # INSTANCE VARIABLES
        self.course_id = course_id
        self.title = title
        self.category = category
        self.duration_weeks = duration_weeks
        self.fee = fee
        self.max_seats = max_seats

        # Seats left for enrollment
        self.available_seats = max_seats

        # List of student_ids enrolled in this course
        self.enrolled_students = []

        # Faculty object assigned to teach this course
        self.assigned_faculty = None

        # Course is active by default
        self.is_active = True

        # COURSE CONTENT
        # [{"id": "M1", "title": "...", "lessons": [
        #     {"id": "L1", "title": "...", "type": "Video",
        #      "content": "...", "duration_min": 20}, ...]}, ...]
        self.modules = []
        self._module_counter = 0
        self._lesson_counter = 0

        # Automatically add the complete Course object
        # to the list
        Course.courses_list.append(self)


    # ========================================================
    # CLASS METHOD - Display Available Courses
    # ========================================================

    @classmethod
    def display_available_courses(cls):

        available_courses = []

        for course in cls.courses_list:
            if course.is_active and course.available_seats > 0:
                available_courses.append(course)
        return available_courses


    # ========================================================
    # CLASS METHOD - Search Course by Title or Category
    # ========================================================

    @classmethod
    def search_course(cls, keyword):

        found_courses = []

        for course in cls.courses_list:
            if course.is_active:
                if (keyword.lower() in course.title.lower() or
                        keyword.lower() in course.category.lower()):
                    found_courses.append(course)
        return found_courses


    # ========================================================
    # CLASS METHOD - Find a Course by its ID
    # ========================================================

    @classmethod
    def get_by_id(cls, course_id):

        for course in cls.courses_list:
            if course.course_id == course_id:
                return course
        return None


    # ========================================================
    # INSTANCE METHODS - Course Content (modules and lessons)
    # ========================================================

    def add_module(self, title):
        self._module_counter += 1
        module = {
            "id": f"M{self._module_counter}",
            "title": title,
            "lessons": []
        }
        self.modules.append(module)
        return module

    def add_lesson(self, module_id, title, lesson_type,
                   content="", duration_min=0):
        for module in self.modules:
            if module["id"] == module_id:
                self._lesson_counter += 1
                lesson = {
                    "id": f"L{self._lesson_counter}",
                    "title": title,
                    "type": lesson_type,
                    "content": content,
                    "duration_min": int(duration_min)
                }
                module["lessons"].append(lesson)
                return lesson
        return None

    def remove_module(self, module_id):
        for module in self.modules:
            if module["id"] == module_id:
                self.modules.remove(module)
                return True
        return False

    def remove_lesson(self, lesson_id):
        for module in self.modules:
            for lesson in module["lessons"]:
                if lesson["id"] == lesson_id:
                    module["lessons"].remove(lesson)
                    return True
        return False

    def get_all_lessons(self):
        return [
            lesson
            for module in self.modules
            for lesson in module["lessons"]
        ]

    def total_lessons(self):
        return len(self.get_all_lessons())

    def total_duration_min(self):
        return sum(
            lesson["duration_min"] for lesson in self.get_all_lessons()
        )


    # ========================================================
    # INSTANCE METHOD - Display Course Details
    # ========================================================

    def course_details(self):

        if self.assigned_faculty:
            faculty_name = self.assigned_faculty.name
        else:
            faculty_name = "Not Assigned"

        return {
            "Course ID": self.course_id,
            "Title": self.title,
            "Category": self.category,
            "Duration (weeks)": self.duration_weeks,
            "Fee": self.fee,
            "Seats Available": f"{self.available_seats}/{self.max_seats}",
            "Faculty": faculty_name,
            "Modules": len(self.modules),
            "Lessons": self.total_lessons(),
            "Status": "Active" if self.is_active else "Inactive"
        }


# ============================================================
#                    3. FACULTY CLASS
# ============================================================

class Faculty(Institution):

    # CLASS VARIABLE
    faculty_list = []

    def __init__(self, faculty_id, name, department,
                 qualification, experience_years):

        # INSTANCE VARIABLES
        self.faculty_id = faculty_id
        self.name = name
        self.department = department
        self.qualification = qualification
        self.experience_years = experience_years

        # PRIVATE INSTANCE VARIABLE
        # Courses currently assigned to this faculty
        self.__assigned_courses = []

        # PRIVATE INSTANCE VARIABLE
        # Monthly salary (sensitive, kept private)
        self.__salary = 0

        # PRIVATE INSTANCE VARIABLE
        # Daily work attendance -> {"YYYY-MM-DD": True/False}
        # (separate from the courses they teach - this tracks
        # whether the faculty member showed up to work that day)
        self.__attendance = {}

        Faculty.faculty_list.append(self)


    # ========================================================
    # INSTANCE METHOD - Faculty Details
    # ========================================================

    def faculty_details(self):
        return {
            "Faculty ID": self.faculty_id,
            "Name": self.name,
            "Department": self.department,
            "Qualification": self.qualification,
            "Experience (years)": self.experience_years,
            "Courses Assigned": len(self.__assigned_courses)
        }


    # ========================================================
    # INSTANCE METHOD - Add Assigned Course
    # ========================================================

    def add_assigned_course(self, course):
        self.__assigned_courses.append({
            "id": course.course_id,
            "title": course.title
        })


    # ========================================================
    # INSTANCE METHOD - Remove Assigned Course
    # ========================================================

    def remove_assigned_course(self, course_id):
        for course in self.__assigned_courses:
            if course["id"] == course_id:
                self.__assigned_courses.remove(course)
                return True
        return False


    # ========================================================
    # INSTANCE METHOD - Get Assigned Courses
    # ========================================================

    def get_assigned_courses(self):
        return self.__assigned_courses


    # ========================================================
    # INSTANCE METHOD - Set / Get Salary
    # ========================================================

    def set_salary(self, amount):
        self.__salary = amount

    def get_salary(self):
        return self.__salary


    # ========================================================
    # INSTANCE METHOD - Daily Work Attendance
    # Stored as: {"YYYY-MM-DD": True/False}
    # ========================================================

    def mark_attendance(self, date_str, present):
        # Marking the same date again simply overwrites
        # the previous entry for that day
        self.__attendance[date_str] = present

    def is_attendance_marked(self, date_str):
        return date_str in self.__attendance

    def get_attendance_records(self):
        # Returns {"YYYY-MM-DD": True/False, ...}
        return self.__attendance

    def get_monthly_attendance(self, year, month):
        # Filters records down to a single month
        monthly_records = {}

        for date_str, present in self.__attendance.items():
            record_date = date.fromisoformat(date_str)
            if record_date.year == year and record_date.month == month:
                monthly_records[date_str] = present

        return monthly_records

    def get_attendance_percentage(self):
        records = self.__attendance
        if not records:
            return 0

        present_days = sum(
            1 for present in records.values() if present
        )
        return round(
            (present_days / len(records)) * 100, 2
        )


# ============================================================
#                  4. PAYMENT CLASS (Fees)
# ============================================================

class Payment:
    """One fee installment received from a student for a course."""

    def __init__(self, receipt_no, student, course, amount, mode,
                 balance_after, payment_date=None):
        self.receipt_no = receipt_no
        self.student_id = student.student_id
        self.student_name = student.name
        self.course_id = course.course_id
        self.course_title = course.title
        self.amount = amount
        self.mode = mode
        self.balance_after = balance_after
        self.payment_date = payment_date if payment_date else date.today()

    def payment_details(self):
        return {
            "Receipt No.": self.receipt_no,
            "Date": str(self.payment_date),
            "Student ID": self.student_id,
            "Student": self.student_name,
            "Course": self.course_title,
            "Amount": self.amount,
            "Mode": self.mode,
            "Balance After": self.balance_after
        }


# ============================================================
#                    5. STUDENT CLASS
# ============================================================

class Student(Institution):

    def __init__(self, student_id, name, phone, age):

        # INSTANCE VARIABLES
        self.student_id = student_id
        self.name = name
        self.phone = phone
        self.age = age

        # PRIVATE INSTANCE VARIABLE
        # Courses currently enrolled by this student
        self.__enrolled_courses = []

        # PRIVATE INSTANCE VARIABLE
        # Fee payable per course -> {course_id: fee}
        self.__fee_due = {}

        # PRIVATE INSTANCE VARIABLE
        # Every installment paid (list of Payment objects)
        self.__payments = []

        # PRIVATE INSTANCE VARIABLE
        # Attendance record -> {course_id: {"YYYY-MM-DD": True/False}}
        self.__attendance = {}

        # PRIVATE INSTANCE VARIABLE
        # Grades record -> {course_id: grade}
        self.__grades = {}


    # ========================================================
    # INSTANCE METHOD - Student Details
    # ========================================================

    def student_details(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Phone Number": self.phone,
            "Age": self.age,
            "Courses Enrolled": len(self.__enrolled_courses),
            "Total Fees Paid": self.get_fees_paid(),
            "Fee Balance": self.get_total_balance()
        }


    # ========================================================
    # INSTANCE METHOD - Check Enrollment Eligibility
    # ========================================================

    def can_enroll(self):
        # Maximum 3 courses per student at a time
        if len(self.__enrolled_courses) < 3:
            return True
        return False


    # ========================================================
    # INSTANCE METHOD - Add / Remove Enrolled Course
    # ========================================================

    def add_enrolled_course(self, course):
        self.__enrolled_courses.append({
            "id": course.course_id,
            "title": course.title
        })
        # Attendance for this course starts as an empty
        # date -> present/absent record
        self.__attendance[course.course_id] = {}

        # The course fee becomes payable by this student
        self.__fee_due[course.course_id] = course.fee

    def remove_enrolled_course(self, course_id):
        for course in self.__enrolled_courses:
            if course["id"] == course_id:
                self.__enrolled_courses.remove(course)

                # Drop the fee only if nothing was paid for it
                if self.get_paid_for_course(course_id) == 0:
                    self.__fee_due.pop(course_id, None)
                return True
        return False

    def get_enrolled_courses(self):
        return self.__enrolled_courses


    # ========================================================
    # INSTANCE METHODS - Fees (per course, installments)
    # ========================================================

    def add_payment(self, payment):
        self.__payments.append(payment)

    def get_payments(self):
        return self.__payments

    def get_fees_paid(self):
        return sum(p.amount for p in self.__payments)

    def get_fee_due(self, course_id):
        return self.__fee_due.get(course_id, 0)

    def get_paid_for_course(self, course_id):
        return sum(
            p.amount for p in self.__payments
            if p.course_id == course_id
        )

    def get_balance(self, course_id):
        balance = (
            self.get_fee_due(course_id)
            - self.get_paid_for_course(course_id)
        )
        return max(balance, 0)

    def get_total_fee_due(self):
        return sum(self.__fee_due.values())

    def get_total_balance(self):
        return sum(
            self.get_balance(course_id)
            for course_id in self.__fee_due
        )

    def get_fee_status(self, course_id):
        due = self.get_fee_due(course_id)
        paid = self.get_paid_for_course(course_id)

        if paid >= due:
            return "Paid"
        elif paid > 0:
            return "Partial"
        return "Unpaid"


    # ========================================================
    # INSTANCE METHOD - Attendance (day-wise)
    # Stored as: {course_id: {"YYYY-MM-DD": True/False}}
    # ========================================================

    def mark_attendance(self, course_id, date_str, present):
        if course_id not in self.__attendance:
            self.__attendance[course_id] = {}

        # Marking the same date again simply overwrites
        # the previous entry for that day
        self.__attendance[course_id][date_str] = present

    def is_attendance_marked(self, course_id, date_str):
        return date_str in self.__attendance.get(course_id, {})

    def get_attendance_records(self, course_id):
        # Returns {"YYYY-MM-DD": True/False, ...} for one course
        return self.__attendance.get(course_id, {})

    def get_monthly_attendance(self, course_id, year, month):
        # Filters that course's records down to a single month
        records = self.__attendance.get(course_id, {})
        monthly_records = {}

        for date_str, present in records.items():
            record_date = date.fromisoformat    (date_str)
            if record_date.year == year and record_date.month == month:
                monthly_records[date_str] = present

        return monthly_records

    def get_attendance_percentage(self, course_id):
        records = self.__attendance.get(course_id, {})
        if not records:
            return 0

        present_days = sum(
            1 for present in records.values() if present
        )
        return round(
            (present_days / len(records)) * 100, 2
        )

    def get_all_attendance(self):
        return self.__attendance


    # ========================================================
    # INSTANCE METHOD - Grades
    # ========================================================

    def add_grade(self, course_id, grade):
        self.__grades[course_id] = grade

    def get_grade(self, course_id):
        return self.__grades.get(course_id, "Not Graded")

    def get_all_grades(self):
        return self.__grades


# ============================================================
#                 6. CERTIFICATE CLASS
# ============================================================

class Certificate:

    def __init__(self, student, course, grade, cert_number,
                 attendance=0, issue_date=None):
        self.cert_number = cert_number
        self.student_name = student.name
        self.student_id = student.student_id
        self.course_title = course.title
        self.course_id = course.course_id
        self.grade = grade
        self.attendance = attendance
        self.issue_date = issue_date if issue_date else date.today()

    def certificate_details(self):
        return {
            "Certificate No.": self.cert_number,
            "Certificate For": self.student_name,
            "Student ID": self.student_id,
            "Course Completed": self.course_title,
            "Grade": self.grade,
            "Attendance": f"{self.attendance}%",
            "Issued On": str(self.issue_date),
            "Issuing Institution": Institution.institution_name
        }


# ============================================================
#              7. LMS ACTIVITIES CLASS
# ============================================================

class LMSActivities:

    def __init__(self):
        # Running numbers used to build receipt / certificate IDs
        self._receipt_counter = 0
        self._certificate_counter = 0

        # Every certificate issued -> {certificate_number: Certificate}
        self.certificates = {}


    # ========================================================
    # INTERNAL - Create and store one payment
    # ========================================================

    def _record_payment(self, student, course, amount, mode,
                        payment_date=None):

        self._receipt_counter += 1
        year = (payment_date or date.today()).year

        payment = Payment(
            receipt_no=f"RCP-{year}-{self._receipt_counter:04d}",
            student=student,
            course=course,
            amount=amount,
            mode=mode,
            balance_after=student.get_balance(course.course_id) - amount,
            payment_date=payment_date
        )

        student.add_payment(payment)
        return payment


    # ========================================================
    # ENROLL STUDENT IN A COURSE
    # ========================================================

    def enroll_student(self, student, course, fee_paid=0,
                       mode="Cash", payment_date=None):

        # Check for duplicate enrollment
        if student.student_id in course.enrolled_students:
            return (
                False,
                "This student is already enrolled in this course."
            )

        # Check student eligibility
        if not student.can_enroll():
            return (
                False,
                "Enrollment limit reached. "
                "A student can enroll in maximum 3 courses at a time."
            )

        # Check course availability
        if not course.is_active or course.available_seats <= 0:
            return (
                False,
                "Sorry! This course has no available seats."
            )

        # Reduce available seats
        course.available_seats -= 1

        # Add student to course's enrolled list
        course.enrolled_students.append(student.student_id)

        # Add course to student's enrolled list
        student.add_enrolled_course(course)

        # Record any fee paid at the time of enrollment
        # (never more than the course fee)
        fee_paid = min(fee_paid, course.fee)

        if fee_paid > 0:
            self._record_payment(
                student, course, fee_paid, mode, payment_date
            )

        return (
            True,
            f"'{student.name}' enrolled successfully "
            f"in '{course.title}'."
        )


    # ========================================================
    # UNENROLL STUDENT FROM A COURSE
    # ========================================================

    def unenroll_student(self, student, course):

        if student.student_id not in course.enrolled_students:
            return (
                False,
                "This student is not enrolled in this course."
            )

        course.enrolled_students.remove(student.student_id)
        course.available_seats += 1
        student.remove_enrolled_course(course.course_id)

        return (
            True,
            f"'{student.name}' has been unenrolled from '{course.title}'."
        )


    # ========================================================
    # ASSIGN FACULTY TO A COURSE
    # ========================================================

    def assign_faculty(self, faculty, course):

        if course.assigned_faculty is not None:
            return (
                False,
                f"'{course.title}' already has a faculty assigned."
            )

        course.assigned_faculty = faculty
        faculty.add_assigned_course(course)

        return (
            True,
            f"'{faculty.name}' assigned to teach '{course.title}'."
        )


    # ========================================================
    # REASSIGN / REMOVE FACULTY FROM A COURSE
    # ========================================================

    def remove_faculty(self, faculty, course):

        if course.assigned_faculty != faculty:
            return (
                False,
                "This faculty is not assigned to this course."
            )

        course.assigned_faculty = None
        faculty.remove_assigned_course(course.course_id)

        return (
            True,
            f"'{faculty.name}' removed from '{course.title}'."
        )


    # ========================================================
    # MARK ATTENDANCE - single student, single date
    # ========================================================

    def mark_attendance(self, student, course, date_str, present):

        if student.student_id not in course.enrolled_students:
            return (
                False,
                "This student is not enrolled in this course."
            )

        student.mark_attendance(course.course_id, date_str, present)

        status = "Present" if present else "Absent"

        return (
            True,
            f"Attendance marked as '{status}' for "
            f"'{student.name}' in '{course.title}' on {date_str}."
        )


    # ========================================================
    # MARK ATTENDANCE FOR AN ENTIRE CLASS ON ONE DATE
    # Used by faculty taking daily attendance for a course.
    #
    # attendance_map: {student_id: True/False}
    # students_by_id: {student_id: Student object}
    # ========================================================

    def mark_class_attendance(
        self,
        course,
        date_str,
        attendance_map,
        students_by_id
    ):

        marked_names = []

        for student_id, present in attendance_map.items():

            # Only mark students actually enrolled in this course
            if student_id not in course.enrolled_students:
                continue

            student = students_by_id.get(student_id)
            if student is None:
                continue

            student.mark_attendance(
                course.course_id,
                date_str,
                present
            )
            marked_names.append(student.name)

        if not marked_names:
            return (
                False,
                "No enrolled students were marked."
            )

        return (
            True,
            f"Attendance saved for {len(marked_names)} "
            f"student(s) in '{course.title}' on {date_str}."
        )


    # ========================================================
    # MARK FACULTY ATTENDANCE - single faculty, single date
    # (Daily work attendance, used to evaluate whether a
    # faculty member showed up to work each day.)
    # ========================================================

    def mark_faculty_attendance(self, faculty, date_str, present):

        faculty.mark_attendance(date_str, present)

        status = "Present" if present else "Absent"

        return (
            True,
            f"Attendance marked as '{status}' for "
            f"'{faculty.name}' on {date_str}."
        )


    # ========================================================
    # MARK FACULTY ATTENDANCE FOR ALL FACULTY ON ONE DATE
    #
    # attendance_map: {faculty_id: True/False}
    # faculty_by_id: {faculty_id: Faculty object}
    # ========================================================

    def mark_all_faculty_attendance(
        self,
        date_str,
        attendance_map,
        faculty_by_id
    ):

        marked_names = []

        for faculty_id, present in attendance_map.items():

            faculty = faculty_by_id.get(faculty_id)
            if faculty is None:
                continue

            faculty.mark_attendance(date_str, present)
            marked_names.append(faculty.name)

        if not marked_names:
            return (
                False,
                "No faculty members were marked."
            )

        return (
            True,
            f"Attendance saved for {len(marked_names)} "
            f"faculty member(s) on {date_str}."
        )


    # ========================================================
    # RECORD FEE PAYMENT (installment for one course)
    # Returns (success, Payment or None, message)
    # ========================================================

    def pay_fee(self, student, course, amount, mode="Cash",
                payment_date=None):

        if student.student_id not in course.enrolled_students:
            return (
                False,
                None,
                "This student is not enrolled in this course."
            )

        if amount <= 0:
            return (
                False,
                None,
                "Payment amount must be greater than zero."
            )

        balance = student.get_balance(course.course_id)

        if balance <= 0:
            return (
                False,
                None,
                "The fee for this course is already fully paid."
            )

        if amount > balance:
            return (
                False,
                None,
                f"Payment rejected. The pending balance is only "
                f"₹{balance:,}."
            )

        payment = self._record_payment(
            student, course, amount, mode, payment_date
        )

        return (
            True,
            payment,
            f"Payment of ₹{amount:,} received from '{student.name}' "
            f"for '{course.title}'. Receipt {payment.receipt_no} "
            f"| Balance: ₹{payment.balance_after:,}."
        )


    # ========================================================
    # RECORD GRADE FOR A COURSE
    # ========================================================

    def record_grade(self, student, course, grade):

        if student.student_id not in course.enrolled_students:
            return (
                False,
                "This student is not enrolled in this course."
            )

        student.add_grade(course.course_id, grade)

        return (
            True,
            f"Grade '{grade}' recorded for '{student.name}' "
            f"in '{course.title}'."
        )


    # ========================================================
    # ISSUE CERTIFICATE
    # (Requires min 75% attendance and a recorded grade)
    # Each student/course pair gets exactly one certificate.
    # ========================================================

    def get_certificate(self, student, course):

        for certificate in self.certificates.values():
            if (certificate.student_id == student.student_id
                    and certificate.course_id == course.course_id):
                return certificate
        return None

    def verify_certificate(self, cert_number):

        return self.certificates.get(cert_number.strip().upper())

    def issue_certificate(self, student, course):

        # Already issued? Return the same certificate
        existing = self.get_certificate(student, course)
        if existing:
            return (
                True,
                existing,
                "Certificate was already issued for this course."
            )

        attendance = student.get_attendance_percentage(course.course_id)
        grade = student.get_grade(course.course_id)

        if attendance < MIN_ATTENDANCE_FOR_CERTIFICATE:
            return (
                False,
                None,
                f"Certificate denied. Attendance is {attendance}%, "
                f"minimum {MIN_ATTENDANCE_FOR_CERTIFICATE}% required."
            )

        if grade == "Not Graded":
            return (
                False,
                None,
                "Certificate denied. Course grade not yet recorded."
            )

        self._certificate_counter += 1

        cert_number = (
            f"SOS-{date.today().year}-{course.course_id}-"
            f"{self._certificate_counter:04d}"
        )

        certificate = Certificate(
            student, course, grade, cert_number, attendance
        )

        self.certificates[cert_number] = certificate

        return (
            True,
            certificate,
            f"Certificate issued to '{student.name}' for "
            f"completing '{course.title}'."
        )


    # ========================================================
    # GENERATE FULL STUDENT PROGRESS REPORT
    # ========================================================

    def generate_progress_report(self, student):

        report = []

        for course_entry in student.get_enrolled_courses():
            course_id = course_entry["id"]
            report.append({
                "Course": course_entry["title"],
                "Attendance %": student.get_attendance_percentage(course_id),
                "Grade": student.get_grade(course_id),
                "Fee Status": student.get_fee_status(course_id),
                "Fee Balance": student.get_balance(course_id)
            })

        return report


# ============================================================
#              8. LMS ANALYTICS CLASS
# ============================================================
#
# Read-only reporting. Every method returns plain lists of
# dictionaries, so the app can turn them into tables/charts.
# ============================================================

class LMSAnalytics:

    # ---------------- Attendance ----------------

    def overall_student_attendance(self, students):
        present_days = 0
        total_days = 0

        for student in students:
            for records in student.get_all_attendance().values():
                present_days += sum(1 for p in records.values() if p)
                total_days += len(records)

        if total_days == 0:
            return 0
        return round(present_days / total_days * 100, 1)

    def attendance_trend(self, students):
        # Monthly attendance % for students and for faculty
        student_totals = {}
        faculty_totals = {}

        for student in students:
            for records in student.get_all_attendance().values():
                for date_str, present in records.items():
                    bucket = student_totals.setdefault(date_str[:7], [0, 0])
                    bucket[0] += 1 if present else 0
                    bucket[1] += 1

        for faculty in Faculty.faculty_list:
            for date_str, present in faculty.get_attendance_records().items():
                bucket = faculty_totals.setdefault(date_str[:7], [0, 0])
                bucket[0] += 1 if present else 0
                bucket[1] += 1

        rows = []

        for group, totals in (
            ("Students", student_totals),
            ("Faculty", faculty_totals)
        ):
            for month in sorted(totals):
                present, total = totals[month]
                rows.append({
                    "Month": month,
                    "Group": group,
                    "Attendance %": round(present / total * 100, 1)
                })

        return rows

    def faculty_attendance_stats(self):
        return [
            {
                "Faculty": faculty.name,
                "Attendance %": faculty.get_attendance_percentage(),
                "Days Recorded": len(faculty.get_attendance_records())
            }
            for faculty in Faculty.faculty_list
            if faculty.get_attendance_records()
        ]

    def at_risk_students(self, students,
                         threshold=MIN_ATTENDANCE_FOR_CERTIFICATE):
        rows = []

        for student in students:
            for entry in student.get_enrolled_courses():
                course_id = entry["id"]

                if not student.get_attendance_records(course_id):
                    continue

                attendance = student.get_attendance_percentage(course_id)

                if attendance < threshold:
                    rows.append({
                        "Student ID": student.student_id,
                        "Student": student.name,
                        "Course": entry["title"],
                        "Attendance %": attendance,
                        "Phone": student.phone
                    })

        return sorted(rows, key=lambda r: r["Attendance %"])

    # ---------------- Enrollment ----------------

    def enrollment_stats(self):
        return [
            {
                "Course": course.title,
                "Enrolled": len(course.enrolled_students),
                "Seats Left": course.available_seats,
                "Max Seats": course.max_seats
            }
            for course in Course.courses_list
        ]

    # ---------------- Grades ----------------

    def grade_distribution(self, students):
        counts = {grade: 0 for grade in GRADES}

        for student in students:
            for grade in student.get_all_grades().values():
                if grade in counts:
                    counts[grade] += 1

        return [
            {"Grade": grade, "Students": count}
            for grade, count in counts.items()
        ]

    # ---------------- Fees ----------------

    def student_fee_rows(self, student):
        rows = []

        for entry in student.get_enrolled_courses():
            course_id = entry["id"]
            rows.append({
                "Course ID": course_id,
                "Course": entry["title"],
                "Fee": student.get_fee_due(course_id),
                "Paid": student.get_paid_for_course(course_id),
                "Balance": student.get_balance(course_id),
                "Status": student.get_fee_status(course_id)
            })

        return rows

    def fee_status_rows(self, students):
        rows = []

        for student in students:
            for row in self.student_fee_rows(student):
                rows.append({
                    "Student ID": student.student_id,
                    "Student": student.name,
                    **row
                })

        return rows

    def fee_defaulters(self, students):
        rows = []

        for student in students:
            balance = student.get_total_balance()

            if balance <= 0:
                continue

            pending_courses = [
                entry["title"]
                for entry in student.get_enrolled_courses()
                if student.get_balance(entry["id"]) > 0
            ]

            rows.append({
                "Student ID": student.student_id,
                "Student": student.name,
                "Phone": student.phone,
                "Pending Courses": ", ".join(pending_courses),
                "Total Fee": student.get_total_fee_due(),
                "Paid": student.get_fees_paid(),
                "Balance": balance
            })

        return sorted(rows, key=lambda r: r["Balance"], reverse=True)

    def fee_stats(self, students):
        rows = []

        for course in Course.courses_list:
            billed = 0
            collected = 0

            for student in students:
                if student.student_id in course.enrolled_students:
                    billed += student.get_fee_due(course.course_id)
                    collected += student.get_paid_for_course(course.course_id)

            rows.append({
                "Course": course.title,
                "Billed": billed,
                "Collected": collected,
                "Pending": max(billed - collected, 0)
            })

        return rows

    def all_payments(self, students):
        payments = [
            payment
            for student in students
            for payment in student.get_payments()
        ]

        return sorted(
            payments,
            key=lambda p: (p.payment_date, p.receipt_no),
            reverse=True
        )

    def payment_mode_stats(self, students):
        totals = {}

        for payment in self.all_payments(students):
            totals[payment.mode] = totals.get(payment.mode, 0) + payment.amount

        return [
            {"Mode": mode, "Amount": amount}
            for mode, amount in totals.items()
        ]

    def monthly_revenue(self, students):
        totals = {}

        for payment in self.all_payments(students):
            month = str(payment.payment_date)[:7]
            totals[month] = totals.get(month, 0) + payment.amount

        return [
            {"Month": month, "Collected": totals[month]}
            for month in sorted(totals)
        ]


# ============================================================
#                    9. DEMO / SAMPLE USAGE
# ============================================================

if __name__ == "__main__":

    lms = LMSActivities()

    # Create courses
    python_course = Course("C001", "Python Programming", "Technology", 8, 6000, 2)
    design_course = Course("C002", "Graphic Design", "Creative Arts", 6, 5000, 1)

    # Create faculty
    faculty1 = Faculty("F001", "Mr. Suresh Nair", "Technology", "M.Tech", 6)
    faculty2 = Faculty("F002", "Ms. Anjali Menon", "Creative Arts", "MFA", 4)

    # Create students
    student1 = Student("S001", "Rahul Krishnan", "9998887771", 21)
    student2 = Student("S002", "Meera Pillai", "9998887772", 23)

    # Assign faculty
    print(lms.assign_faculty(faculty1, python_course))
    print(lms.assign_faculty(faculty2, design_course))

    # Enroll students (student1 pays in full, student2 pays in installments)
    print(lms.enroll_student(student1, python_course, fee_paid=6000))
    print(lms.enroll_student(student2, python_course, fee_paid=2000, mode="UPI"))
    print(lms.pay_fee(student2, python_course, 9999))      # rejected: overpayment
    print(lms.pay_fee(student2, python_course, 4000, "Card"))

    # Course content
    module = python_course.add_module("Python Basics")
    python_course.add_lesson(module["id"], "Variables", "Video", "", 15)

    # Mark attendance (day-wise)
    from datetime import timedelta
    start_day = date.today()
    for day_offset in range(8):
        session_date = str(start_day + timedelta(days=day_offset))
        lms.mark_attendance(
            student1, python_course, session_date, present=True
        )
        lms.mark_faculty_attendance(
            faculty1, session_date, present=True
        )

    print(
        f"Faculty1 attendance %: "
        f"{faculty1.get_attendance_percentage()}"
    )

    # Record grade
    print(lms.record_grade(student1, python_course, "A"))

    # Issue certificate
    success, cert, message = lms.issue_certificate(student1, python_course)
    print(message)
    if success:
        print(cert.certificate_details())

    # Progress report
    print(lms.generate_progress_report(student1))

    # Analytics
    analytics = LMSAnalytics()
    print(analytics.fee_defaulters([student1, student2]))