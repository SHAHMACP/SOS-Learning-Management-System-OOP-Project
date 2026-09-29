import streamlit as st
from pro import(
    SOS,
    Courses,
    Employees,
    Student,
    SOSActivities,
    employees,
    students,
    activities
    
    
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SOS - School of Skills",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    font-size: 42px;
    font-weight: bold;
    color: #17365D;
}

.subtitle {
    font-size: 20px;
    color: #555555;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.course-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff;
    border-left: 5px solid #17365D;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)



    # ========================================================
    


# ============================================================
# CREATE ACTIVITIES OBJECT
# ============================================================
if "activities" not in st.session_state:
    st.session_state.activities = SOSActivities()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image(
    "https://images.unsplash.com/photo-1523240795612-9a054b0db644"
    "?auto=format&fit=crop&w=800&q=80",
    use_container_width=True
)

st.sidebar.title("🎓 SOS Management")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📚 Courses",
        "👨‍💼 Employees",
        "➕ Add Employees",
        "🎓 Students",
        "➕ Add Students",
        "📊 Activities",
        "ℹ️ SOS Details"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="title">School of Skills</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Student & Staff Management Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # Hero Image
    st.image(
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644"
        "?auto=format&fit=crop&w=1600&q=85",
        use_container_width=True
    )

    st.write("")

    # Statistics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📚 Courses",
            len(Courses.courses_list)
        )

    with col2:
        st.metric(
            "👨‍💼 Employees",
            len(employees)
        )

    with col3:
        st.metric(
            "🎓 Students",
            len(students)
        )

    with col4:
        st.metric(
            "💼 Placed Students",
            len(
                activities.get_placed_students(
                    students
                )
            )
        )

    st.divider()

    st.subheader("Welcome to SOS")

    st.write(
        """
        School of Skills is an educational institution
        providing skill-based courses in areas such as
        Data Science, Design and Management.
        """
    )


# ============================================================
# COURSES
# ============================================================

elif page == "📚 Courses":

    st.title("📚 Courses")

    # Search
    search = st.text_input(
        "🔍 Search Course",
        placeholder="Enter course name..."
    )

    if search:

        result = Courses.search_course(search)

    else:

        result = Courses.display_courses()

    st.write(
        f"Showing **{len(result)}** course(s)"
    )

    for course in result:

        st.markdown(
            '<div class="course-card">',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([3, 1])

        with col1:

            st.subheader(
                f"🎓 {course.course_name}"
            )

            st.write(
                f"**Category:** {course.category}"
            )

            st.write(
                f"**Duration:** {course.course_duration}"
            )

            st.write(
                f"**Mode:** {course.mode}"
            )

            st.write(
                f"**Instructor:** {course.instructor}"
            )

        with col2:

            st.metric(
                "Course Fee",
                f"₹{course.course_fee:,}"
            )

            st.write(
                f"Course ID: {course.course_id}"
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# EMPLOYEES
# ============================================================

elif page == "👨‍💼 Employees":

    st.title("👨‍💼 Employees")

    department = st.selectbox(
        "Select Department",
        [
            "All",
            "Human Resource Management",
            "Fasion Design",
            "Data Science"
        ]
    )

    if department == "All":

        filtered_employees = employees

    else:

        filtered_employees = [
            employee
            for employee in employees
            if employee.department == department
        ]

    st.write(
        f"Total Employees: **{len(filtered_employees)}**"
    )

    for employee in filtered_employees:

        with st.expander(
            f"👤 {employee.name} - "
            f"{employee.department}"
        ):

            st.write(
                f"**Employee ID:** "
                f"{employee.employee_id}"
            )

            st.write(
                f"**Phone:** {employee.phone}"
            )

            st.write(
                f"**Age:** {employee.age}"
            )

            st.write(
                f"**Department:** "
                f"{employee.department}"
            )

            st.write(
                f"**Salary:** ₹{employee.salary:,}"
            )

            st.write(
                f"**Leave:** "
                f"{employee.get_leave()} days"
            )

            st.write(
                f"**Status:** {employee.status}"
            )
            st.subheader("Leave Management")
            
            leave_days=st.number_input(
                "Leave Days",
                min_value=1,
                step=1,
                key=f"leave_{employee.employee_id}"
            )
            
            if st.button(
                "Apply Leave",
                key=f"apply_leave_{employee.employee_id}"
            ):
                employee.add_leave(leave_days)
                st.success(
                    f"Leave added for {employee.name}"
                )
# ============================================================
# Adding Employee 
# ============================================================
elif page ==  "➕ Add Employees":
    
    st.title(" ➕ Add New Employees")
    
    employee_id=st.number_input(
        "employee ID",
        min_value=1,
        step=1
        
    )
    
    employee_name=st.text_input(
        "Employee Name"
    )
    
    age=st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )
    
    department = st.selectbox(
            "Select Department",
            [
                "Human Resource Management",
                "Fasion Design",
                "Data Science"
            ]
        )
    

    phone=st.text_input(
        "phone Number"
        
    )
    
    salary=st.number_input(
        "Salary",
        step=2
    )
    
    if st.button(
        "Add Employee",
        type="primary"
    ):
        if not employee_name or not age or not department or not phone or not salary:
            st.warning(
                "Please Fill all fields"
            )
            
        else:
            
            new_employee=Employees.add_employee(
                employee_id,
                employee_name,
                phone,
                age,
                department,
                salary
            )
            employees.append(new_employee)
            
            st.success(
                f"Employee {employee_name} added Successfully"
            )
            
            
    
    
    
    
    


# ============================================================
# STUDENTS
# ============================================================

elif page == "🎓 Students":

    st.title("🎓 Students")

    status_filter = st.selectbox(
        "Filter by Status",
        [
            "All",
            "Passed",
            "Dropped"
        ]
    )

    if status_filter == "All":

        filtered_students = students

    else:

        filtered_students = [
            student
            for student in students
            if student.status == status_filter
        ]

    for student in filtered_students:

        with st.expander(
            f"🎓 {student.name} - "
            f"{student.course}"
        ):

            st.write(
                f"**Student ID:** "
                f"{student.student_id}"
            )

            st.write(
                f"**Course:** {student.course}"
            )

            st.write(
                f"**Status:** {student.status}"
            )

            st.write(
                f"**Fee Paid:** "
                f"{'Yes' if student.fee_paid else 'No'}"
            )

            st.write(
                f"**Admission Type:** "
                f"{student.admission_type}"
            )
            
            st.write(
                f"**Leave:** "
                f"{student.get_leave()} days"
            )

            st.write(
                f"**Placed:** "
                f"{'Yes' if student.placed else 'No'}"
            )
            
            st.subheader("Leave Management")
            
            leave_days=st.number_input(
                "Leave Days",
                min_value=1,
                step=1,
                key=f"leave_{student.student_id}"
            )
            
            if st.button(
                "Apply Leave",
                key=f"apply_leave_{student.student_id}"
            ):
                student.add_leave(leave_days)
                st.success(
                    f"Leave added for {student.name}"
                )

# ============================================================
# Add Students
# ============================================================
elif page == "➕ Add Students":
    
    st.title(" ➕ Add New Students")
    
        
    student_id=st.number_input(
            "Student ID",
            min_value=1,
            step=1
            
        )
        
    student_name=st.text_input(
            "Student Name"
        )
        
    age=st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            step=1
        )
        
    course=st.text_input(
            "Course"
        )
        
    phone=st.number_input(
            "phone Number",
            step=2
            
        )
        
    fee_paid = st.checkbox(
        "Fee Paid"
        )
        
        
    if st.button(
            "Add Student",
            type="primary"
        ):
            if not student_name or not age or not course or not phone or not fee_paid:
                st.warning(
                    "Please Fill all fields"
                )
                
            else:
                
                new_student=Student.add_student(
                    student_id,
                    student_name,
                    course,
                    fee_paid
                )
                students.append(new_student)
                
                st.success(
                    f"Student {student_name} added Successfully"
                )
    
     



# ============================================================
# ACTIVITIES
# ============================================================

elif page == "📊 Activities":

    st.title("📊 SOS Activities")

    # Student statistics

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Students",
            activities.get_total_students(
                students
            )
        )

    with col2:

        st.metric(
            "Passed Students",
            len(
                activities.get_passed_students(
                    students
                )
            )
        )

    with col3:

        st.metric(
            "Dropped Students",
            len(
                activities.get_dropped_students(
                    students
                )
            )
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💰 Fee Details")

        st.metric(
            "Fee Paid",
            len(
                activities.get_fee_paid_students(
                    students
                )
            )
        )

        st.metric(
            "Fee Not Paid",
            len(
                activities.get_fee_not_paid_students(
                    students
                )
            )
        )

    with col2:

        st.subheader("🎯 Admission & Placement")

        st.metric(
            "New Admissions",
            len(
                activities.get_new_admissions(
                    students
                )
            )
        )

        st.metric(
            "Placed Students",
            len(
                activities.get_placed_students(
                    students
                )
            )
        )


# ============================================================
# SOS DETAILS
# ============================================================

elif page == "ℹ️ SOS Details":

    st.title("ℹ️ SOS Details")

    sos = SOS()

    details = sos.sos_details()

    for key, value in details.items():

        st.info(
            f"**{key}:** {value}"
        )

    st.divider()

    st.subheader("🎓 About SOS")

    st.write(
        """
        School of Skills provides skill-oriented education
        and training programs designed to help students
        develop practical and professional skills.
        """
    )

    st.success(
        "Welcome to School of Skills!"
    )