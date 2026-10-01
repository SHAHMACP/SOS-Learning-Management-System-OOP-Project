


# ============================================================
# SOS CLASS
# ============================================================

class SOS():

    # CLASS VARIABLES
    sos_name = "School of Skills"
    sos_location = "Calicut"
    starting_year = 2020
    founder = "ABCD"
    contact_number = "1234567890"

    # INSTANCE METHOD - Display SOS Details
    def sos_details(self):

        return {
            "SOS Name": self.sos_name,
            "Location": self.sos_location,
            "Starting Year": self.starting_year,
            "Founder": self.founder,
            "Contact Number": self.contact_number
        }


# ============================================================
# COURSES CLASS
# ============================================================

class Courses(SOS):

    # CLASS VARIABLE
    courses_list = []

    # ========================================================
    # CONSTRUCTOR
    # ========================================================

    def __init__(
        self,
        course_id,
        course_name,
        course_fee,
        course_duration,
        category,
        mode,
        instructor
    ):

        # INSTANCE VARIABLES
        self.course_id = course_id
        self.course_name = course_name
        self.course_fee = course_fee
        self.course_duration = course_duration
        self.category = category
        self.mode = mode
        self.instructor = instructor

        # Add course object to class list
        Courses.courses_list.append(self)

    # ========================================================
    # CLASS METHOD - Display All Courses
    # ========================================================

    @classmethod
    def display_courses(cls):

        all_courses = []

        for course in cls.courses_list:
            all_courses.append(course)

        return all_courses

    # ========================================================
    # CLASS METHOD - Search Course by Name
    # ========================================================

    @classmethod
    def search_course(cls, course_name):

        found_courses = []

        for course in cls.courses_list:

            if course_name.lower() in course.course_name.lower():
                found_courses.append(course)

        return found_courses

    # ========================================================
    # CLASS METHOD - Search Course by Category
    # ========================================================

    @classmethod
    def search_by_category(cls, category):

        found_courses = []

        for course in cls.courses_list:

            if category.lower() == course.category.lower():
                found_courses.append(course)

        return found_courses

    # ========================================================
    # INSTANCE METHOD - Display Course Details
    # ========================================================

    def display_course(self):

        return {
            "Course ID": self.course_id,
            "Course Name": self.course_name,
            "Course Fee": self.course_fee,
            "Course Duration": self.course_duration,
            "Category": self.category,
            "Mode": self.mode,
            "Instructor": self.instructor
        }


# ============================================================
# ADD COURSES
# ============================================================

course1 = Courses(
    101,
    "Data Science",
    45000,
    "6 Months",
    "Data & AI",
    "Offline",
    "SOS Faculty"
)

course2 = Courses(
    103,
    "Fashion Design",
    35000,
    "6 Months",
    "Design",
    "Offline",
    "SOS Faculty"
)

course3 = Courses(
    104,
    "Human Resource Management",
    30000,
    "4 Months",
    "Management",
    "Offline",
    "SOS Faculty"
)


# ============================================================
# DISPLAY ALL COURSES
# ============================================================

print("\n========== ALL COURSES ==========")

courses = Courses.display_courses()

for course in courses:
    print(course.display_course())


# ============================================================
# SEARCH COURSE BY NAME
# ============================================================

print("\n========== SEARCH COURSE ==========")

result = Courses.search_course("Data")

for course in result:
    print(course.display_course())


# ============================================================
# SEARCH COURSE BY CATEGORY
# ============================================================

print("\n========== SEARCH BY CATEGORY ==========")

result = Courses.search_by_category("Design")

for course in result:
    print(course.display_course())


# ============================================================
# DISPLAY ONE COURSE
# ============================================================

print("\n========== SINGLE COURSE DETAILS ==========")

print(course1.display_course())


# ============================================================
# EMPLOYEES CLASS
# ============================================================

class Employees(SOS):

    def __init__(
        self,
        employee_id,
        name,
        phone,
        age,
        department,
        salary
    ):

        # INSTANCE VARIABLES
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age = age
        self.department = department
        self.salary = salary

        # PRIVATE INSTANCE VARIABLE
        self.__leave = 0

        # Employee status
        self.status = "Active"
        
    @classmethod
    def add_employee(cls,emplyee_id,name,phone,age,deprtment,salary):
        new_employee=cls(
            emplyee_id,
            name,
            phone,
            age,
            deprtment,
            salary
            
        )
        return new_employee

    # ========================================================
    # INSTANCE METHOD - Employee Details
    # ========================================================

    def employee_details(self):

        return {
            "Employee ID": self.employee_id,
            "Employee Name": self.name,
            "Phone Number": self.phone,
            "Age": self.age,
            "Department": self.department,
            "Salary": self.salary,
            "Leave": self.__leave,
            "Status": self.status
        }

    # ========================================================
    # CLASS METHOD - Faculty
    # ========================================================

    @classmethod
    def faculty(cls):
        return "Faculty Department"

    # ========================================================
    # CLASS METHOD - Content Creators
    # ========================================================

    @classmethod
    def content_creators(cls):
        return "Content Creators Department"

    # ========================================================
    # CLASS METHOD - Receptionist
    # ========================================================

    @classmethod
    def receptionist(cls):
        return "Receptionist Department"

    # ========================================================
    # INSTANCE METHOD - Add Leave
    # ========================================================

    def add_leave(self, days):
        self.__leave += days

    # ========================================================
    # INSTANCE METHOD - Get Leave
    # ========================================================

    def get_leave(self):
        return self.__leave

    # ========================================================
    # INSTANCE METHOD - Update Phone Number
    # ========================================================

    def update_phone(self, phone):
        self.phone = phone

    # ========================================================
    # INSTANCE METHOD - Update Salary
    # ========================================================

    def update_salary(self, salary):
        self.salary = salary


# ============================================================
# ADD EMPLOYEES
# ============================================================

employees = []

# HR Department
emp1 = Employees(
    101,
    "Anu",
    "9876543210",
    25,
    "HR",
    25000
)

emp2 = Employees(
    102,
    "Meera",
    "9876543211",
    27,
    "HR",
    28000
)

# FAD Department
emp3 = Employees(
    103,
    "Rahul",
    "9876543212",
    26,
    "FAD",
    30000
)

emp4 = Employees(
    104,
    "Arun",
    "9876543213",
    29,
    "FAD",
    32000
)

# DSA Department
emp5 = Employees(
    105,
    "Akhil",
    "9876543214",
    24,
    "DSA",
    35000
)

emp6 = Employees(
    106,
    "Neha",
    "9876543215",
    25,
    "DSA",
    38000
)

employees.append(emp1)
employees.append(emp2)
employees.append(emp3)
employees.append(emp4)
employees.append(emp5)
employees.append(emp6)


# ============================================================
# STUDENT CLASS
# ============================================================

class Student(SOS):

    def __init__(
        self,
        student_id,
        name,
        course,
        status,
        fee_paid,
        admission_type,
        placed
    ):

        self.student_id = student_id
        self.name = name
        self.course = course
        self.status = status
        self.fee_paid = fee_paid
        self.admission_type = admission_type
        self.placed = placed
        
        self.__leave = 0
        
        
    @classmethod
    def add_student(cls,student_id,name,course,fee_paid):
        new_student=cls(
            student_id,
            name,
            course,
            "Active",
            fee_paid,
            "New",
            False
        )
        return new_student

    # ========================================================
    # INSTANCE METHOD - Student Details
    # ========================================================

    def student_details(self):

        return {
            "Student ID": self.student_id,
            "Student Name": self.name,
            "Course": self.course,
            "Status": self.status,
            "Fee Paid": self.fee_paid,
            "Admission Type": self.admission_type,
            "Leave" : self.__leave,
            "Placed": self.placed
        }

    def add_leave(self,days):
        self.__leave += days
        
    def get_leave(self):
        return self.__leave
# ============================================================
# ADD STUDENTS
# ============================================================

students = []

student1 = Student(
    1,
    "Vijay",
    "Data Science",
    "Passed",
    True,
    "New",
    True
)

student2 = Student(
    2,
    "Arun",
    "Data Science",
    "Passed",
    True,
    "New",
    False
)

student3 = Student(
    3,
    "Rahul",
    "Fashion Design",
    "Dropped",
    False,
    "New",
    False
)

student4 = Student(
    4,
    "Meera",
    "HR Management",
    "Passed",
    False,
    "New",
    True
)

student5 = Student(
    5,
    "Anu",
    "Data Science",
    "Passed",
    True,
    "Old",
    False
)

students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)


# ============================================================
# SOS ACTIVITIES CLASS
# ============================================================

class SOSActivities:

    # ========================================================
    # STUDENT DETAILS
    # ========================================================

    def get_total_students(self, students):
        return len(students)

    def get_passed_students(self, students):

        return [
            student
            for student in students
            if student.status == "Passed"
        ]

    def get_dropped_students(self, students):

        return [
            student
            for student in students
            if student.status == "Dropped"
        ]

    # ========================================================
    # STAFF DETAILS
    # ========================================================

    def get_total_staff(self, staff):
        return len(staff)

    def get_dropped_staff(self, staff):

        return [
            member
            for member in staff
            if member.status == "Dropped"
        ]

    # ========================================================
    # FEE DETAILS
    # ========================================================

    def get_fee_paid_students(self, students):

        return [
            student
            for student in students
            if student.fee_paid
        ]

    def get_fee_not_paid_students(self, students):

        return [
            student
            for student in students
            if not student.fee_paid
        ]

    # ========================================================
    # NEW ADMISSIONS
    # ========================================================

    def get_new_admissions(self, students):

        return [
            student
            for student in students
            if student.admission_type == "New"
        ]

    # ========================================================
    # PLACED STUDENTS
    # ========================================================

    def get_placed_students(self, students):

        return [
            student
            for student in students
            if student.placed
        ]


# ============================================================
# SOS ACTIVITIES OBJECT
# ============================================================

activities = SOSActivities()


# ============================================================
# DISPLAY STUDENT ACTIVITIES
# ============================================================

print("\n========== STUDENT ACTIVITIES ==========")

print(
    "Total Students:",
    activities.get_total_students(students)
)

print(
    "Passed Students:",
    len(activities.get_passed_students(students))
)

print(
    "Dropped Students:",
    len(activities.get_dropped_students(students))
)

print(
    "Fee Paid Students:",
    len(activities.get_fee_paid_students(students))
)

print(
    "Fee Not Paid Students:",
    len(activities.get_fee_not_paid_students(students))
)

print(
    "New Admissions:",
    len(activities.get_new_admissions(students))
)

print(
    "Placed Students:",
    len(activities.get_placed_students(students))
)


# ============================================================
# DISPLAY EMPLOYEE DETAILS
# ============================================================

print("\n========== EMPLOYEE DETAILS ==========")

for employee in employees:
    print(employee.employee_details())


# ============================================================
# TEST LEAVE
# ============================================================

print("\n========== LEAVE DETAILS ==========")

emp1.add_leave(3)

print("Anu Leave:", emp1.get_leave())


# ============================================================
# UPDATE EMPLOYEE DETAILS
# ============================================================

emp1.update_phone("9999999999")
emp1.update_salary(30000)

print("\n========== UPDATED EMPLOYEE ==========")

print(emp1.employee_details())


# ============================================================
# SOS DETAILS
# ============================================================

print("\n========== SOS DETAILS ==========")

print(course1.sos_details())
