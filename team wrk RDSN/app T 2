# ============================================================
#           SOS - SCHOOL OF SKILLS
#         LEARNING MANAGEMENT SYSTEM (LMS)
#                       app.py
# ============================================================
#
# Files in this project (keep them in the same folder):
#   app.py        - the pages (this file)
#   sos.py        - the classes (Course, Student, Faculty, ...)
#   theme.py      - the visual design (CSS + HTML cards)
#   pdf_utils.py  - certificate and receipt PDFs
#   demo_data.py  - sample data for demos
#   sos-logo.png  - the logo
# ============================================================


import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import date
from PIL import Image

import theme
from theme import esc, money
from sos import (
    Institution,
    Course,
    Faculty,
    Student,
    LMSActivities,
    LMSAnalytics,
    GRADES,
    PAYMENT_MODES,
    LESSON_TYPES,
    MIN_ATTENDANCE_FOR_CERTIFICATE
)
from pdf_utils import (
    build_certificate_pdf,
    build_receipt_pdf,
    get_logo_image,
    logo_data_uri
)
from demo_data import load_demo_data


# ============================================================
#                    LOGO
# ============================================================

LOGO_PATH = "sos-logo.png"


# ============================================================
#                    PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SOS - School of Skills | LMS",
    page_icon=Image.open(LOGO_PATH),
    layout="wide"
)


# ============================================================
#              WHITE & RED BRAND THEME
# ============================================================
# All styling lives in theme.py so this file stays about the
# pages. Colours below are only used for the Plotly charts.
# ============================================================

SOS_RED = "#A31F24"
SOS_RED_DARK = "#7E1519"
SOS_RED_SOFT = "#E6C4C4"
SOS_TEXT = "#241414"

st.markdown(
    "<style>" + theme.CSS + "</style>",
    unsafe_allow_html=True
)


# ============================================================
#                    INITIAL DATA
# ============================================================

# Create initial courses only once

if "courses_initialized" not in st.session_state:

    # Clear class list
    Course.courses_list = []

    Course("C001", "DATA SCIENCE", "Technology", 8, 70000, 20)
    Course("C002", "FASHION DESIGNING", "Creative Arts", 9, 85000, 30)
    Course("C003", "HUMAN RESOURCE", "Business", 6, 80000, 20)

    st.session_state.courses_initialized = True


# Create initial faculty only once

if "faculty_initialized" not in st.session_state:

    # Clear class list
    Faculty.faculty_list = []

    Faculty("F001", "Mrs. SHAHMA CP", "DATA SCIENCE", "PHD SCHOLAR", 6)
    Faculty("F002", "Ms. DIYA", "HUMAN RESOURCE", "MBA", 4)

    st.session_state.faculty_initialized = True


# Create initial students only once

if "students" not in st.session_state:

    st.session_state.students = [
        Student("DSA01", "MUHAMMED ROSHAN P", "8606333217", 21)
    ]


# Create LMSActivities object

if "activities" not in st.session_state:

    st.session_state.activities = LMSActivities()


# Shortcuts used throughout the pages below

activities = st.session_state.activities
analytics = LMSAnalytics()


# ============================================================
#                    SMALL HELPERS
# ============================================================

MONTH_NAMES = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

FEE_STATUS_LABEL = {
    "Paid": "🟢 Paid",
    "Partial": "🟠 Partial",
    "Unpaid": "🔴 Unpaid"
}


def html(markup):
    """Render an HTML string from theme.py."""
    st.markdown(markup, unsafe_allow_html=True)


def page_header(icon, title, subtitle=""):
    html(theme.page_header_html(icon, title, subtitle))


def section(title):
    html(theme.section_html(title))


def kpis(items):
    html(theme.kpi_grid_html(items))


def empty_state(icon, text):
    html(theme.empty_state_html(icon, text))


def go(page):
    """Switch page (used as a button callback)."""
    st.session_state.current_page = page


def flash(key, message):
    """Keep a success message across the st.rerun() that follows."""
    st.session_state[key] = message


def show_flash(key):
    message = st.session_state.pop(key, None)
    if message:
        st.success(message)


def select_student(label="Select Student", key=None):
    """Student dropdown. Returns the Student, or None if there are none."""

    students = st.session_state.students

    if not students:
        empty_state("🎓", "No students are registered yet.")
        return None

    options = {f"{s.student_id} - {s.name}": s for s in students}

    choice = st.selectbox(label, list(options.keys()), key=key)

    return options[choice]


def enrolled_course_options(student):
    """{'C001 - TITLE': Course} for the courses a student is in."""

    lookup = {c.course_id: c for c in Course.courses_list}

    return {
        f"{entry['id']} - {entry['title']}": lookup[entry["id"]]
        for entry in student.get_enrolled_courses()
        if entry["id"] in lookup
    }


def fmt_minutes(minutes):
    if minutes >= 60:
        return f"{minutes // 60}h {minutes % 60}m"
    return f"{minutes} min"


def month_year_picker(default_date, key_prefix):
    col_year, col_month = st.columns(2)

    with col_year:
        year = st.number_input(
            "Year",
            min_value=2020,
            max_value=2100,
            value=default_date.year,
            step=1,
            key=f"{key_prefix}_year"
        )

    with col_month:
        month_name = st.selectbox(
            "Month",
            MONTH_NAMES,
            index=default_date.month - 1,
            key=f"{key_prefix}_month"
        )

    return int(year), MONTH_NAMES.index(month_name) + 1


def render_monthly_records(name, monthly_records):
    if not monthly_records:
        st.write(f"**{name}** — no records for this month.")
        return

    present_days = sum(1 for p in monthly_records.values() if p)
    total_days = len(monthly_records)
    month_percentage = round((present_days / total_days) * 100, 2)

    with st.expander(
        f"{name} — {present_days}/{total_days} days "
        f"({month_percentage}%)"
    ):
        for record_date in sorted(monthly_records):
            if monthly_records[record_date]:
                st.write(f"✅ {record_date} — Present")
            else:
                st.write(f"❌ {record_date} — Absent")


def show_table(df, **kwargs):
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        **kwargs
    )


def with_status_labels(df):
    """Add a coloured dot to the Status column of a fee table."""

    df = df.copy()

    if "Status" in df.columns:
        df["Status"] = df["Status"].map(
            lambda s: FEE_STATUS_LABEL.get(s, s)
        )

    return df


def show_chart(fig, height=340):
    """Apply the SOS look to a Plotly figure and draw it."""

    fig.update_layout(
        height=height,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(family="Inter, sans-serif", color=SOS_TEXT),
        margin=dict(l=10, r=10, t=50, b=10),
        legend_title_text="",
        title_font=dict(family="Poppins, Inter, sans-serif",
                        color=SOS_RED, size=16)
    )
    fig.update_xaxes(gridcolor="#F3E3E3", title_text="")
    fig.update_yaxes(gridcolor="#F3E3E3")
    st.plotly_chart(fig, use_container_width=True)


def render_certificate(cert):
    """Certificate preview + PDF download."""

    html(
        theme.certificate_preview_html(cert, logo_data_uri(LOGO_PATH))
    )

    st.download_button(
        "⬇️ Download Certificate (PDF)",
        data=build_certificate_pdf(cert, LOGO_PATH),
        file_name=f"{cert.cert_number}.pdf",
        mime="application/pdf",
        key=f"dl_cert_{cert.cert_number}"
    )


def load_demo_callback():
    load_demo_data(st.session_state.students, st.session_state.activities)
    st.session_state.demo_loaded = True
    st.session_state.demo_toast = True


# ============================================================
#                       SIDEBAR
# ============================================================

st.sidebar.image(get_logo_image(LOGO_PATH, 500), use_container_width=True)

st.sidebar.markdown(
    '<div class="sos-side-tag">Learning Management System</div>',
    unsafe_allow_html=True
)


# Remember which page is currently selected across reruns

if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home"


# Group definitions: label shown on the expander -> pages inside it

NAV_GROUPS = {
    "📘 Courses": [
        "📘 Courses",
        "➕ Add Course",
        "📚 Course Content",
    ],
    "🧑‍🏫 Faculty": [
        "🧑‍🏫 Faculty",
        "➕ Add Faculty",
        "🔗 Assign Faculty to Course",
        "🗓️ Mark Faculty Attendance",
    ],
    "🎓 Students": [
        "🎓 Students",
        "➕ Add Student",
        "📝 Enroll Student",
        "✅ Mark Attendance",
        "🏆 Record Grade",
        "💰 Fee Management",
        "📜 Issue Certificate",
        "📊 Progress Report",
    ],
}


def nav_button(container, label):
    """Render one sidebar nav button and switch pages on click."""

    is_current = (st.session_state.current_page == label)

    container.button(
        label,
        key=f"nav_{label}",
        use_container_width=True,
        type="primary" if is_current else "secondary",
        on_click=go,
        args=(label,)
    )


# ----------------------------------------------------------
# General pages (not grouped)
# ----------------------------------------------------------

st.sidebar.markdown(
    '<div class="sos-side-label">Main</div>',
    unsafe_allow_html=True
)

nav_button(st.sidebar, "🏠 Home")
nav_button(st.sidebar, "📈 Analytics Dashboard")
nav_button(st.sidebar, "🔍 Verify Certificate")
nav_button(st.sidebar, "🏫 Institution Details")


# ----------------------------------------------------------
# Grouped pages - each group is a collapsible expander
# ----------------------------------------------------------

st.sidebar.markdown(
    '<div class="sos-side-label">Manage</div>',
    unsafe_allow_html=True
)

for group_label, pages in NAV_GROUPS.items():

    # Auto-expand the group that contains the active page
    group_is_active = st.session_state.current_page in pages

    with st.sidebar.expander(group_label, expanded=group_is_active):

        for page_label in pages:
            nav_button(st, page_label)


# ----------------------------------------------------------
# Demo data - fills every page with realistic sample records
# ----------------------------------------------------------

st.sidebar.markdown(
    '<div class="sos-side-label">Demo</div>',
    unsafe_allow_html=True
)

st.sidebar.button(
    "🧪 Load Demo Data",
    key="load_demo",
    use_container_width=True,
    disabled=st.session_state.get("demo_loaded", False),
    on_click=load_demo_callback,
    help="Adds sample students, attendance, grades, fee "
         "installments and syllabi (one-time)."
)


menu = st.session_state.current_page


if st.session_state.pop("demo_toast", False):
    st.toast("Demo data loaded ✅")


# ============================================================
#                         HOME
# ============================================================

if menu == "🏠 Home":

    students = st.session_state.students

    collected = sum(s.get_fees_paid() for s in students)
    pending = sum(s.get_total_balance() for s in students)
    enrollments = sum(len(c.enrolled_students) for c in Course.courses_list)
    open_courses = Course.display_available_courses()

    html(
        theme.hero_html(
            logo_data_uri(LOGO_PATH),
            "Welcome to the SOS Learning Management System",
            "Manage courses, faculty, students, attendance, fees and "
            "certificates — all in one place.",
            [
                f"🎓 {len(students)} students",
                f"📘 {len(Course.courses_list)} courses",
                f"🧑‍🏫 {len(Faculty.faculty_list)} faculty",
            ]
        )
    )

    kpis([
        ("📘", "Courses", len(Course.courses_list),
         f"{len(open_courses)} open for enrollment"),
        ("🧑‍🏫", "Faculty", len(Faculty.faculty_list)),
        ("🎓", "Students", len(students)),
        ("📝", "Enrollments", enrollments),
        ("💰", "Fees Collected", money(collected)),
        ("⏳", "Fees Pending", money(pending)),
    ])


    # ----------------------------------------------------
    # Quick actions
    # ----------------------------------------------------

    section("Quick Actions")

    qa1, qa2, qa3, qa4 = st.columns(4)

    for column, label, target in (
        (qa1, "📝 Enroll a Student", "📝 Enroll Student"),
        (qa2, "💳 Collect a Fee", "💰 Fee Management"),
        (qa3, "✅ Mark Attendance", "✅ Mark Attendance"),
        (qa4, "📈 View Analytics", "📈 Analytics Dashboard"),
    ):
        with column:
            st.button(
                label,
                key=f"qa_{target}",
                use_container_width=True,
                on_click=go,
                args=(target,)
            )


    # ----------------------------------------------------
    # Open courses
    # ----------------------------------------------------

    section("Courses Open for Enrollment")

    if open_courses:

        html(
            theme.grid_html(
                [theme.course_card_html(c) for c in open_courses]
            )
        )

    else:

        empty_state("📘", "No courses are currently open for enrollment.")


    # ----------------------------------------------------
    # Recent activity
    # ----------------------------------------------------

    section("Recent Activity")

    col_pay, col_attention = st.columns(2)

    with col_pay:

        rows = "".join(
            '<div class="sos-list-item"><span>'
            f'<b>{esc(p.student_name)}</b><br>'
            f'<span class="sos-card-sub">{esc(p.course_title)} · '
            f'{p.payment_date} · {esc(p.mode)}</span></span>'
            f'<b>{money(p.amount)}</b></div>'
            for p in analytics.all_payments(students)[:5]
        )

        html(
            theme.list_card_html(
                "🧾 Recent Payments", rows, "No payments recorded yet."
            )
        )

    with col_attention:

        rows = "".join(
            '<div class="sos-list-item"><span>'
            f'<b>{esc(r["Student"])}</b><br>'
            f'<span class="sos-card-sub">{esc(r["Course"])}</span></span>'
            f'{theme.chip(str(r["Attendance %"]) + "% attendance", "red")}'
            '</div>'
            for r in analytics.at_risk_students(students)[:4]
        )

        defaulter_count = len(analytics.fee_defaulters(students))

        if defaulter_count:
            rows += (
                '<div class="sos-list-item"><span>'
                f'<b>{defaulter_count}</b> student(s) have pending fees'
                '</span>'
                f'{theme.chip("View in Fee Management", "amber")}</div>'
            )

        html(
            theme.list_card_html(
                "⚠️ Needs Attention", rows, "Everything looks good. 🎉"
            )
        )


# ============================================================
#                  INSTITUTION DETAILS
# ============================================================

elif menu == "🏫 Institution Details":

    page_header(
        "🏫", "Institution Details",
        "About SOS - School of Skills."
    )

    details = Institution().institution_details()

    icons = {
        "Institution Name": "🏫",
        "Location": "📍",
        "Established Year": "📅",
        "Founder": "👤",
        "Contact Number": "📞",
        "Email": "✉️",
    }

    html(
        theme.info_grid_html([
            (icons.get(key, "ℹ️"), key, value)
            for key, value in details.items()
        ])
    )


# ============================================================
#                  ANALYTICS DASHBOARD
# ============================================================
#
# Live charts built from the same objects the other pages
# use: enrollment, revenue, attendance and grades. Click
# "Load Demo Data" in the sidebar to fill it with samples.
# ============================================================

elif menu == "📈 Analytics Dashboard":

    page_header(
        "📈", "Analytics Dashboard",
        "Live insights on enrollment, revenue, attendance and grades."
    )

    students = st.session_state.students

    # ----------------------------------------------------
    # Headline numbers
    # ----------------------------------------------------

    fee_rows = analytics.fee_stats(students)

    collected = sum(r["Collected"] for r in fee_rows)
    pending = sum(r["Pending"] for r in fee_rows)

    enrolled_total = sum(
        len(c.enrolled_students) for c in Course.courses_list
    )
    seats_total = sum(c.max_seats for c in Course.courses_list)

    if seats_total:
        utilisation = round(enrolled_total / seats_total * 100, 1)
    else:
        utilisation = 0

    kpis([
        ("📝", "Enrollments", enrolled_total),
        ("🪑", "Seat Utilisation", f"{utilisation}%"),
        ("💰", "Fees Collected", money(collected)),
        ("⏳", "Fees Pending", money(pending)),
        ("✅", "Avg Attendance",
         f"{analytics.overall_student_attendance(students)}%"),
    ])


    # ----------------------------------------------------
    # Row 1 - Seats and fees per course
    # ----------------------------------------------------

    col_a, col_b = st.columns(2)

    with col_a:

        rows = analytics.enrollment_stats()

        if rows:

            fig = px.bar(
                pd.DataFrame(rows),
                x="Course",
                y=["Enrolled", "Seats Left"],
                barmode="stack",
                title="Seat Utilisation by Course",
                color_discrete_map={
                    "Enrolled": SOS_RED,
                    "Seats Left": SOS_RED_SOFT
                }
            )

            show_chart(fig)

        else:

            empty_state("📘", "No courses yet.")

    with col_b:

        if enrolled_total:

            fig = px.bar(
                pd.DataFrame(fee_rows),
                x="Course",
                y=["Collected", "Pending"],
                barmode="stack",
                title="Fees Collected vs Pending (₹)",
                color_discrete_map={
                    "Collected": SOS_RED,
                    "Pending": SOS_RED_SOFT
                }
            )

            show_chart(fig)

        else:

            empty_state("💰", "Fee data appears once students enroll.")


    # ----------------------------------------------------
    # Row 2 - Grades and attendance trend
    # ----------------------------------------------------

    col_a, col_b = st.columns(2)

    with col_a:

        grade_rows = analytics.grade_distribution(students)

        if any(r["Students"] for r in grade_rows):

            fig = px.bar(
                pd.DataFrame(grade_rows),
                x="Grade",
                y="Students",
                text="Students",
                title="Grade Distribution",
                category_orders={"Grade": GRADES},
                color_discrete_sequence=[SOS_RED]
            )

            show_chart(fig)

        else:

            empty_state("🏆", "Grades appear once they are recorded.")

    with col_b:

        trend_rows = analytics.attendance_trend(students)

        if trend_rows:

            fig = px.line(
                pd.DataFrame(trend_rows),
                x="Month",
                y="Attendance %",
                color="Group",
                markers=True,
                title="Monthly Attendance Trend",
                range_y=[0, 105],
                color_discrete_map={
                    "Students": SOS_RED,
                    "Faculty": "#333333"
                }
            )

            fig.update_xaxes(type="category")

            show_chart(fig)

        else:

            empty_state("✅", "Mark attendance to see the trend.")


    # ----------------------------------------------------
    # Row 3 - Faculty punctuality and revenue by month
    # ----------------------------------------------------

    col_a, col_b = st.columns(2)

    with col_a:

        faculty_rows = analytics.faculty_attendance_stats()

        if faculty_rows:

            fig = px.bar(
                pd.DataFrame(faculty_rows),
                x="Attendance %",
                y="Faculty",
                orientation="h",
                text="Attendance %",
                title="Faculty Work Attendance (%)",
                range_x=[0, 100],
                color_discrete_sequence=[SOS_RED_DARK]
            )

            show_chart(fig)

        else:

            empty_state("🧑‍🏫", "Mark faculty attendance to see this chart.")

    with col_b:

        revenue_rows = analytics.monthly_revenue(students)

        if revenue_rows:

            fig = px.bar(
                pd.DataFrame(revenue_rows),
                x="Month",
                y="Collected",
                text_auto=True,
                title="Fee Collection by Month (₹)",
                color_discrete_sequence=[SOS_RED]
            )

            fig.update_xaxes(type="category")

            show_chart(fig)

        else:

            empty_state("💰", "Revenue appears once payments are recorded.")


    # ----------------------------------------------------
    # Row 4 - Payment modes and at-risk students
    # ----------------------------------------------------

    col_a, col_b = st.columns(2)

    with col_a:

        mode_rows = analytics.payment_mode_stats(students)

        if mode_rows:

            fig = px.pie(
                pd.DataFrame(mode_rows),
                names="Mode",
                values="Amount",
                hole=0.5,
                title="Payments by Mode",
                color_discrete_sequence=[
                    SOS_RED, SOS_RED_DARK, "#D9534F",
                    "#E8A0A0", "#333333"
                ]
            )

            show_chart(fig)

        else:

            empty_state("💳", "Payment modes appear once fees are paid.")

    with col_b:

        at_risk = analytics.at_risk_students(students)

        rows = "".join(
            '<div class="sos-list-item"><span>'
            f'<b>{esc(r["Student"])}</b><br>'
            f'<span class="sos-card-sub">{esc(r["Course"])} · '
            f'📞 {esc(r["Phone"])}</span></span>'
            f'{theme.chip(str(r["Attendance %"]) + "%", "red")}</div>'
            for r in at_risk[:6]
        )

        html(
            theme.list_card_html(
                f"⚠️ At-Risk Students (below "
                f"{MIN_ATTENDANCE_FOR_CERTIFICATE}% attendance)",
                rows,
                "No students are currently at risk. 🎉"
            )
        )

        if at_risk:
            st.caption(
                "These students will not be eligible for a certificate "
                "unless their attendance improves."
            )


# ============================================================
#                  VERIFY CERTIFICATE
# ============================================================

elif menu == "🔍 Verify Certificate":

    page_header(
        "🔍", "Verify Certificate",
        "Confirm that a certificate was issued by SOS - School of Skills."
    )

    st.write(
        "Enter the certificate number printed at the bottom of the "
        "certificate (it is also encoded in its QR code)."
    )

    cert_number = st.text_input(
        "Certificate number",
        placeholder="e.g. SOS-2026-C001-0001"
    )

    if cert_number:

        html(
            theme.verify_result_html(
                activities.verify_certificate(cert_number)
            )
        )


# ============================================================
#                         COURSES
# ============================================================

elif menu == "📘 Courses":

    page_header(
        "📘", "Courses",
        "Everything SOS offers — search by title or category."
    )

    search_keyword = st.text_input(
        "🔍 Search courses",
        placeholder="Type a course title or category…"
    )

    if search_keyword:
        courses = Course.search_course(search_keyword)
    else:
        courses = Course.courses_list

    if courses:

        html(theme.grid_html([theme.course_card_html(c) for c in courses]))

    elif search_keyword:

        empty_state("🔍", "No course found matching this keyword.")

    else:

        empty_state("📘", "No courses have been added yet.")


# ============================================================
#                       ADD COURSE
# ============================================================

elif menu == "➕ Add Course":

    page_header(
        "➕", "Add New Course",
        "Create a course that students can enroll in."
    )

    with st.form("add_course_form"):

        col_left, col_right = st.columns(2)

        with col_left:

            course_id = st.text_input("Course ID", placeholder="e.g. C004")

            category = st.text_input(
                "Category", placeholder="e.g. Technology"
            )

            duration_weeks = st.number_input(
                "Duration (weeks)", min_value=1, step=1
            )

        with col_right:

            title = st.text_input(
                "Course Title", placeholder="e.g. WEB DEVELOPMENT"
            )

            fee = st.number_input("Fee (₹)", min_value=0, step=500)

            max_seats = st.number_input(
                "Maximum Seats", min_value=1, step=1
            )

        submitted = st.form_submit_button("Add Course", type="primary")


    if submitted:

        course_id = course_id.strip()
        title = title.strip()
        category = category.strip()

        if not course_id or not title or not category:

            st.warning("Please fill all fields.")

        elif any(c.course_id == course_id for c in Course.courses_list):

            st.error("A course with this ID already exists.")

        else:

            Course(
                course_id, title, category,
                duration_weeks, fee, max_seats
            )

            st.success(
                f"Course '{title}' added successfully! "
                f"Add its syllabus under Course Content."
            )


# ============================================================
#                    COURSE CONTENT
# ============================================================
#
# Faculty/admin build each course's syllabus here:
# course -> modules -> lessons (video, reading, assignment,
# quiz).
# ============================================================

elif menu == "📚 Course Content":

    page_header(
        "📚", "Course Content",
        "Build each course's syllabus from modules and lessons."
    )

    lesson_icons = {
        "Video": "🎬",
        "Reading": "📖",
        "Assignment": "📝",
        "Quiz": "❓"
    }

    if not Course.courses_list:

        empty_state("📘", "No courses are available.")

    else:

        course_options = {
            f"{c.course_id} - {c.title}": c
            for c in Course.courses_list
        }

        course = course_options[
            st.selectbox(
                "Select Course",
                list(course_options.keys()),
                key="content_course"
            )
        ]

        # Filled in last, so the numbers include what was just added
        summary_box = st.container()

        tab_syllabus, tab_module, tab_lesson = st.tabs([
            "📖 Syllabus",
            "➕ Add Module",
            "➕ Add Lesson"
        ])


        # ------------------------------------------------
        # Add Module
        # ------------------------------------------------

        with tab_module:

            with st.form(
                f"module_form_{course.course_id}",
                clear_on_submit=True
            ):

                module_title = st.text_input("Module title")

                if st.form_submit_button("Add Module", type="primary"):

                    if not module_title.strip():

                        st.warning("Please enter a module title.")

                    else:

                        course.add_module(module_title.strip())

                        st.success(
                            f"Module '{module_title.strip()}' added."
                        )


        # ------------------------------------------------
        # Add Lesson
        # ------------------------------------------------

        with tab_lesson:

            if not course.modules:

                st.info("Add a module first, then add lessons to it.")

            else:

                module_options = {
                    f"{m['id']} - {m['title']}": m
                    for m in course.modules
                }

                with st.form(
                    f"lesson_form_{course.course_id}",
                    clear_on_submit=True
                ):

                    module_label = st.selectbox(
                        "Module",
                        list(module_options.keys())
                    )

                    lesson_title = st.text_input("Lesson title")

                    col_type, col_time = st.columns(2)

                    with col_type:
                        lesson_type = st.selectbox(
                            "Lesson type", LESSON_TYPES
                        )

                    with col_time:
                        duration_min = st.number_input(
                            "Duration (minutes)",
                            min_value=0,
                            value=15,
                            step=5
                        )

                    lesson_content = st.text_area(
                        "Description / link / instructions"
                    )

                    if st.form_submit_button("Add Lesson", type="primary"):

                        if not lesson_title.strip():

                            st.warning("Please enter a lesson title.")

                        else:

                            course.add_lesson(
                                module_options[module_label]["id"],
                                lesson_title.strip(),
                                lesson_type,
                                lesson_content.strip(),
                                duration_min
                            )

                            st.success(
                                f"Lesson '{lesson_title.strip()}' added."
                            )


        # ------------------------------------------------
        # Syllabus view (with delete buttons)
        # ------------------------------------------------

        with tab_syllabus:

            if not course.modules:

                empty_state(
                    "📚",
                    "This course has no content yet. Use the tabs above "
                    "to add modules and lessons."
                )

            for module in course.modules:

                with st.expander(
                    f"{module['id']} · {module['title']} "
                    f"({len(module['lessons'])} lessons)",
                    expanded=True
                ):

                    for lesson in module["lessons"]:

                        col_text, col_del = st.columns([8, 1])

                        with col_text:

                            st.write(
                                f"{lesson_icons.get(lesson['type'], '📄')} "
                                f"**{lesson['title']}** — "
                                f"{lesson['type']}, "
                                f"{lesson['duration_min']} min"
                            )

                            if lesson["content"]:
                                st.caption(lesson["content"])

                        with col_del:

                            if st.button(
                                "🗑️",
                                key=f"del_lesson_{course.course_id}_"
                                    f"{lesson['id']}",
                                help="Delete this lesson"
                            ):

                                course.remove_lesson(lesson["id"])
                                st.rerun()

                    if st.button(
                        "Delete this module",
                        key=f"del_module_{course.course_id}_{module['id']}"
                    ):

                        course.remove_module(module["id"])
                        st.rerun()


        # ------------------------------------------------
        # Summary numbers (rendered above the tabs)
        # ------------------------------------------------

        with summary_box:

            kpis([
                ("🧩", "Modules", len(course.modules)),
                ("📖", "Lessons", course.total_lessons()),
                ("⏱️", "Total Duration",
                 fmt_minutes(course.total_duration_min())),
            ])


# ============================================================
#                         FACULTY
# ============================================================

elif menu == "🧑‍🏫 Faculty":

    page_header(
        "🧑‍🏫", "Faculty",
        "Our teaching staff, their courses and work attendance."
    )

    if Faculty.faculty_list:

        html(
            theme.grid_html(
                [theme.faculty_card_html(f) for f in Faculty.faculty_list]
            )
        )

    else:

        empty_state("🧑‍🏫", "No faculty members are registered yet.")


# ============================================================
#                       ADD FACULTY
# ============================================================

elif menu == "➕ Add Faculty":

    page_header(
        "➕", "Add New Faculty",
        "Register a new teaching staff member."
    )

    with st.form("add_faculty_form"):

        col_left, col_right = st.columns(2)

        with col_left:

            faculty_id = st.text_input(
                "Faculty ID", placeholder="e.g. F003"
            )

            department = st.text_input(
                "Department", placeholder="e.g. DATA SCIENCE"
            )

            experience_years = st.number_input(
                "Experience (years)", min_value=0, step=1
            )

        with col_right:

            name = st.text_input(
                "Faculty Name", placeholder="e.g. Mr. ARJUN NAIR"
            )

            qualification = st.text_input(
                "Qualification", placeholder="e.g. M.Tech"
            )

        submitted = st.form_submit_button("Add Faculty", type="primary")


    if submitted:

        faculty_id = faculty_id.strip()
        name = name.strip()
        department = department.strip()

        if not faculty_id or not name or not department:

            st.warning("Please fill all fields.")

        elif any(f.faculty_id == faculty_id for f in Faculty.faculty_list):

            st.error("A faculty member with this ID already exists.")

        else:

            Faculty(
                faculty_id, name, department,
                qualification.strip(), experience_years
            )

            st.success(f"Faculty '{name}' added successfully!")


# ============================================================
#                 ASSIGN FACULTY TO COURSE
# ============================================================

elif menu == "🔗 Assign Faculty to Course":

    page_header(
        "🔗", "Assign Faculty to Course",
        "Each course is taught by one faculty member."
    )

    if not Faculty.faculty_list:

        empty_state("🧑‍🏫", "No faculty members are registered.")

    elif not Course.courses_list:

        empty_state("📘", "No courses are available.")

    else:

        faculty_options = {
            f"{f.faculty_id} - {f.name}": f
            for f in Faculty.faculty_list
        }

        course_options = {
            f"{c.course_id} - {c.title}": c
            for c in Course.courses_list
        }

        col_faculty, col_course = st.columns(2)

        with col_faculty:

            faculty = faculty_options[
                st.selectbox("Select Faculty", list(faculty_options.keys()))
            ]

        with col_course:

            course = course_options[
                st.selectbox("Select Course", list(course_options.keys()))
            ]

        if st.button("Assign Faculty", type="primary"):

            success, message = activities.assign_faculty(faculty, course)

            if success:
                st.success(message)
            else:
                st.error(message)

        section("Current Assignments")

        show_table(
            pd.DataFrame([
                {
                    "Course ID": c.course_id,
                    "Course": c.title,
                    "Faculty": (
                        c.assigned_faculty.name
                        if c.assigned_faculty else "— Not assigned —"
                    )
                }
                for c in Course.courses_list
            ])
        )


# ============================================================
#                 MARK FACULTY ATTENDANCE
# ============================================================
#
# This is separate from the student "Mark Attendance" page
# below. It tracks whether each faculty member showed up to
# work on a given day — not which course they taught — so
# the institution can evaluate faculty punctuality/regularity
# over time.
# ============================================================

elif menu == "🗓️ Mark Faculty Attendance":

    page_header(
        "🗓️", "Faculty Attendance",
        "Record who came to work each day, then review it by month."
    )

    if not Faculty.faculty_list:

        empty_state("🧑‍🏫", "No faculty members are registered.")

    else:

        # ----------------------------------------------------
        # Select Date
        # ----------------------------------------------------

        attendance_date = st.date_input(
            "Date",
            value=date.today(),
            key="faculty_attendance_date"
        )

        date_str = str(attendance_date)

        section(f"Attendance for {date_str}")

        if any(
            f.is_attendance_marked(date_str) for f in Faculty.faculty_list
        ):
            st.caption(
                "Attendance already exists for this date — "
                "resubmitting will overwrite it."
            )


        # ----------------------------------------------------
        # One Present/Absent choice per faculty member
        # ----------------------------------------------------

        attendance_inputs = {}

        for faculty in Faculty.faculty_list:

            existing_records = faculty.get_attendance_records()

            if date_str in existing_records and not existing_records[date_str]:
                default_index = 1
            else:
                default_index = 0

            col_name, col_status = st.columns([3, 2])

            with col_name:

                st.write(
                    f"**{faculty.faculty_id} - {faculty.name}** "
                    f"({faculty.department})"
                )

            with col_status:

                status = st.radio(
                    "Status",
                    ["Present", "Absent"],
                    index=default_index,
                    horizontal=True,
                    label_visibility="collapsed",
                    key=f"fac_att_{date_str}_{faculty.faculty_id}"
                )

            attendance_inputs[faculty.faculty_id] = (status == "Present")


        # ----------------------------------------------------
        # Submit Button - saves all faculty at once
        # ----------------------------------------------------

        if st.button("Save Faculty Attendance", type="primary"):

            success, message = activities.mark_all_faculty_attendance(
                date_str,
                attendance_inputs,
                {f.faculty_id: f for f in Faculty.faculty_list}
            )

            if success:
                st.success(message)
            else:
                st.error(message)


        # ----------------------------------------------------
        # Overall Attendance % per faculty
        # ----------------------------------------------------

        section("Overall Work Attendance")

        html(
            theme.list_card_html(
                "📈 Attendance since joining",
                "".join(
                    theme.bar_row_html(
                        f.name, f.faculty_id, f.get_attendance_percentage()
                    )
                    for f in Faculty.faculty_list
                )
            )
        )


        # ----------------------------------------------------
        # Monthly Attendance View
        # ----------------------------------------------------

        section("Monthly Attendance")

        view_year, view_month = month_year_picker(
            attendance_date, "faculty_att"
        )

        for faculty in Faculty.faculty_list:

            render_monthly_records(
                faculty.name,
                faculty.get_monthly_attendance(view_year, view_month)
            )


# ============================================================
#                         STUDENTS
# ============================================================

elif menu == "🎓 Students":

    page_header(
        "🎓", "Students",
        "Enrolled courses, attendance, grades and fee status."
    )

    if st.session_state.students:

        html(
            theme.grid_html(
                [theme.student_card_html(s) for s in st.session_state.students]
            )
        )

    else:

        empty_state("🎓", "No students are registered yet.")


# ============================================================
#                       ADD STUDENT
# ============================================================

elif menu == "➕ Add Student":

    page_header(
        "➕", "Add New Student",
        "Register a student, then enroll them in a course."
    )

    with st.form("add_student_form"):

        col_left, col_right = st.columns(2)

        with col_left:

            student_id = st.text_input(
                "Student ID", placeholder="e.g. DSA02"
            )

            phone = st.text_input(
                "Phone Number", placeholder="10-digit mobile number"
            )

        with col_right:

            name = st.text_input(
                "Student Name", placeholder="Full name"
            )

            age = st.number_input(
                "Age", min_value=1, max_value=120, step=1
            )

        submitted = st.form_submit_button("Add Student", type="primary")


    if submitted:

        student_id = student_id.strip()
        name = name.strip()
        phone = phone.strip()

        if not student_id or not name or not phone:

            st.warning("Please fill all fields.")

        elif any(
            s.student_id == student_id for s in st.session_state.students
        ):

            st.error("A student with this ID already exists.")

        else:

            st.session_state.students.append(
                Student(student_id, name, phone, age)
            )

            st.success(f"Student '{name}' added successfully!")


# ============================================================
#                     ENROLL STUDENT
# ============================================================

elif menu == "📝 Enroll Student":

    page_header(
        "📝", "Enroll Student",
        "Add a student to a course. Fees can be paid later in installments."
    )

    available_courses = Course.display_available_courses()

    if not available_courses:

        empty_state("📘", "No courses are currently open for enrollment.")

    elif not st.session_state.students:

        empty_state("🎓", "No students are registered yet.")

    else:

        col_student, col_course = st.columns(2)

        with col_student:

            student = select_student()

        course_options = {
            f"{c.course_id} - {c.title}": c for c in available_courses
        }

        with col_course:

            course = course_options[
                st.selectbox("Select Course", list(course_options.keys()))
            ]

        kpis([
            ("📚", "Courses Enrolled",
             f"{len(student.get_enrolled_courses())} / 3"),
            ("💰", "Course Fee", money(course.fee)),
            ("🪑", "Seats Left",
             f"{course.available_seats}/{course.max_seats}"),
        ])


        # Fees can be paid in installments, so collecting
        # anything now is optional (0 = pay later).

        col_amount, col_mode = st.columns(2)

        with col_amount:

            initial_payment = st.number_input(
                "Amount to collect now (₹)",
                min_value=0,
                max_value=int(course.fee),
                value=0,
                step=500,
                help="Leave at 0 to collect the fee later "
                     "under Fee Management."
            )

        with col_mode:

            payment_mode = st.selectbox("Payment mode", PAYMENT_MODES)


        if st.button("Enroll Student", type="primary"):

            success, message = activities.enroll_student(
                student, course, initial_payment, payment_mode
            )

            if success:

                st.success(message)

                st.info(
                    f"Collected {money(initial_payment)} — "
                    f"balance due: "
                    f"{money(student.get_balance(course.course_id))}."
                )

            else:

                st.error(message)


# ============================================================
#                     MARK ATTENDANCE
# ============================================================

elif menu == "✅ Mark Attendance":

    page_header(
        "✅", "Mark Attendance",
        "Faculty take day-wise attendance for their own course."
    )

    if not Faculty.faculty_list:

        empty_state("🧑‍🏫", "No faculty members are registered.")

    else:

        # ----------------------------------------------------
        # Select Faculty (the person taking attendance)
        # ----------------------------------------------------

        faculty_options = {
            f"{f.faculty_id} - {f.name}": f for f in Faculty.faculty_list
        }

        col_faculty, col_course, col_date = st.columns(3)

        with col_faculty:

            faculty = faculty_options[
                st.selectbox("Faculty", list(faculty_options.keys()))
            ]

        assigned_courses = faculty.get_assigned_courses()

        # Only this faculty's own courses
        course_lookup = {c.course_id: c for c in Course.courses_list}

        course_options = {
            f"{entry['id']} - {entry['title']}": course_lookup[entry["id"]]
            for entry in assigned_courses
            if entry["id"] in course_lookup
        }

        with col_course:

            if course_options:
                course = course_options[
                    st.selectbox("Course", list(course_options.keys()))
                ]
            else:
                course = None
                st.selectbox("Course", ["—"], disabled=True)

        with col_date:

            attendance_date = st.date_input("Date", value=date.today())

        date_str = str(attendance_date)


        if course is None:

            st.info("This faculty has no courses assigned yet.")

        else:

            # ------------------------------------------------
            # Enrolled students for this course
            # ------------------------------------------------

            enrolled_students = [
                s for s in st.session_state.students
                if s.student_id in course.enrolled_students
            ]


            if not enrolled_students:

                st.info("No students are enrolled in this course yet.")

            else:

                section(f"{course.title} — {date_str}")

                if any(
                    s.is_attendance_marked(course.course_id, date_str)
                    for s in enrolled_students
                ):
                    st.caption(
                        "Attendance already exists for this date — "
                        "resubmitting will overwrite it."
                    )


                # ----------------------------------------------
                # One Present/Absent choice per enrolled student
                # ----------------------------------------------

                attendance_inputs = {}

                for student in enrolled_students:

                    existing_records = student.get_attendance_records(
                        course.course_id
                    )

                    if (date_str in existing_records
                            and not existing_records[date_str]):
                        default_index = 1
                    else:
                        default_index = 0

                    col_name, col_status = st.columns([3, 2])

                    with col_name:

                        st.write(
                            f"**{student.student_id} - {student.name}**"
                        )

                    with col_status:

                        status = st.radio(
                            "Status",
                            ["Present", "Absent"],
                            index=default_index,
                            horizontal=True,
                            label_visibility="collapsed",
                            key=(
                                f"att_{course.course_id}_"
                                f"{date_str}_{student.student_id}"
                            )
                        )

                    attendance_inputs[student.student_id] = (
                        status == "Present"
                    )


                # ----------------------------------------------
                # Submit Button - saves the whole class at once
                # ----------------------------------------------

                if st.button("Save Attendance", type="primary"):

                    success, message = activities.mark_class_attendance(
                        course,
                        date_str,
                        attendance_inputs,
                        {s.student_id: s for s in st.session_state.students}
                    )

                    if success:
                        st.success(message)
                    else:
                        st.error(message)


                # ----------------------------------------------
                # Monthly Attendance View
                # ----------------------------------------------

                section("Monthly Attendance")

                view_year, view_month = month_year_picker(
                    attendance_date, "student_att"
                )

                for student in enrolled_students:

                    render_monthly_records(
                        student.name,
                        student.get_monthly_attendance(
                            course.course_id, view_year, view_month
                        )
                    )


# ============================================================
#                      RECORD GRADE
# ============================================================

elif menu == "🏆 Record Grade":

    page_header(
        "🏆", "Record Grade",
        "Record a student's final grade for a course."
    )

    col_student, col_course = st.columns(2)

    with col_student:

        student = select_student()

    if student is not None:

        course_options = enrolled_course_options(student)

        if not course_options:

            st.info("This student is not enrolled in any courses.")

        else:

            with col_course:

                course = course_options[
                    st.selectbox("Select Course", list(course_options.keys()))
                ]

            col_grade, _ = st.columns(2)

            with col_grade:

                grade = st.selectbox("Select Grade", GRADES)

            current = student.get_grade(course.course_id)

            st.caption(f"Current grade: {current}")

            if st.button("Record Grade", type="primary"):

                success, message = activities.record_grade(
                    student, course, grade
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# ============================================================
#                    FEE MANAGEMENT
# ============================================================
#
# Fees are tracked per course. Students can pay in
# installments; overpayment is blocked; every payment gets a
# receipt number and a downloadable PDF receipt.
# ============================================================

elif menu == "💰 Fee Management":

    page_header(
        "💰", "Fee Management",
        "Collect installments, track balances and download receipts."
    )

    students = st.session_state.students


    if not students:

        empty_state("🎓", "No students are registered yet.")

    else:

        tab_collect, tab_status, tab_history = st.tabs([
            "💳 Collect Payment",
            "📋 Fee Status & Defaulters",
            "🧾 Payment History & Receipts"
        ])


        # ----------------------------------------------------
        # TAB 1 - Collect a payment
        # ----------------------------------------------------

        with tab_collect:

            show_flash("fee_flash")

            student = select_student(key="fee_student")

            fee_rows = analytics.student_fee_rows(student)


            if not fee_rows:

                st.info("This student is not enrolled in any courses.")

            else:

                kpis([
                    ("📘", "Courses", len(fee_rows)),
                    ("💰", "Total Fee",
                     money(student.get_total_fee_due())),
                    ("✅", "Paid", money(student.get_fees_paid())),
                    ("⏳", "Balance", money(student.get_total_balance())),
                ])

                show_table(with_status_labels(pd.DataFrame(fee_rows)))

                st.caption("All amounts are in ₹.")

                pending_options = {
                    label: course
                    for label, course in
                    enrolled_course_options(student).items()
                    if student.get_balance(course.course_id) > 0
                }


                if not pending_options:

                    st.success(
                        "All fees are cleared for this student. 🎉"
                    )

                else:

                    section("Record a Payment")

                    col_course, col_amount, col_mode = st.columns(3)

                    with col_course:

                        selected_label = st.selectbox(
                            "Course to pay for",
                            list(pending_options.keys()),
                            key="fee_course"
                        )

                    course = pending_options[selected_label]

                    balance = int(student.get_balance(course.course_id))

                    with col_amount:

                        amount = st.number_input(
                            f"Amount (₹) — balance {money(balance)}",
                            min_value=1,
                            max_value=balance,
                            value=balance,
                            step=500
                        )

                    with col_mode:

                        mode = st.selectbox(
                            "Payment mode",
                            PAYMENT_MODES,
                            key="fee_mode"
                        )


                    if st.button("Submit Payment", type="primary"):

                        success, payment, message = activities.pay_fee(
                            student, course, int(amount), mode
                        )

                        if success:

                            st.session_state.last_payment = payment

                            flash("fee_flash", message)

                            st.rerun()

                        else:

                            st.error(message)


            # Latest receipt stays available after the rerun

            last_payment = st.session_state.get("last_payment")

            if last_payment is not None:

                section("Latest Receipt")

                st.write(
                    f"🧾 **{last_payment.receipt_no}** — "
                    f"{last_payment.student_name}, "
                    f"{money(last_payment.amount)}"
                )

                st.download_button(
                    "⬇️ Download Receipt (PDF)",
                    data=build_receipt_pdf(last_payment, LOGO_PATH),
                    file_name=f"{last_payment.receipt_no}.pdf",
                    mime="application/pdf",
                    key="dl_last_receipt"
                )


        # ----------------------------------------------------
        # TAB 2 - Status of every fee + defaulters
        # ----------------------------------------------------

        with tab_status:

            status_rows = analytics.fee_status_rows(students)


            if not status_rows:

                empty_state(
                    "💰", "Fee records appear once students are enrolled."
                )

            else:

                billed = sum(r["Fee"] for r in status_rows)
                paid = sum(r["Paid"] for r in status_rows)
                balance_total = sum(r["Balance"] for r in status_rows)

                if billed:
                    collection_rate = round(paid / billed * 100, 1)
                else:
                    collection_rate = 0

                kpis([
                    ("🧮", "Total Billed", money(billed)),
                    ("✅", "Collected", money(paid)),
                    ("⏳", "Pending", money(balance_total)),
                    ("📈", "Collection Rate", f"{collection_rate}%"),
                ])

                status_filter = st.multiselect(
                    "Filter by status",
                    ["Paid", "Partial", "Unpaid"],
                    default=["Paid", "Partial", "Unpaid"]
                )

                filtered = [
                    r for r in status_rows if r["Status"] in status_filter
                ]

                if filtered:
                    show_table(with_status_labels(pd.DataFrame(filtered)))
                else:
                    st.info("No records match this filter.")


                section("Students with Pending Fees")

                defaulters = analytics.fee_defaulters(students)

                if defaulters:

                    defaulters_df = pd.DataFrame(defaulters)

                    show_table(defaulters_df)

                    st.download_button(
                        "⬇️ Download List (CSV)",
                        data=defaulters_df.to_csv(index=False).encode("utf-8"),
                        file_name="pending_fees.csv",
                        mime="text/csv",
                        key="dl_defaulters"
                    )

                else:

                    st.success("No pending fees. 🎉")


        # ----------------------------------------------------
        # TAB 3 - Payment history + receipt download
        # ----------------------------------------------------

        with tab_history:

            payments = analytics.all_payments(students)


            if not payments:

                empty_state("🧾", "No payments have been recorded yet.")

            else:

                show_table(
                    pd.DataFrame([p.payment_details() for p in payments])
                )

                receipt_options = {
                    f"{p.receipt_no} · {p.student_name} · "
                    f"{money(p.amount)}": p
                    for p in payments
                }

                chosen = receipt_options[
                    st.selectbox(
                        "Select a receipt",
                        list(receipt_options.keys()),
                        key="receipt_choice"
                    )
                ]

                st.download_button(
                    "⬇️ Download Receipt (PDF)",
                    data=build_receipt_pdf(chosen, LOGO_PATH),
                    file_name=f"{chosen.receipt_no}.pdf",
                    mime="application/pdf",
                    key="dl_history_receipt"
                )


# ============================================================
#                    ISSUE CERTIFICATE
# ============================================================

elif menu == "📜 Issue Certificate":

    page_header(
        "📜", "Issue Certificate",
        f"Needs at least {MIN_ATTENDANCE_FOR_CERTIFICATE}% attendance and "
        f"a recorded grade. Every certificate gets a unique number."
    )

    show_flash("cert_flash")

    col_student, col_course = st.columns(2)

    with col_student:

        student = select_student()

    if student is not None:

        course_options = enrolled_course_options(student)


        if not course_options:

            st.info("This student is not enrolled in any courses.")

        else:

            with col_course:

                course = course_options[
                    st.selectbox("Select Course", list(course_options.keys()))
                ]

            attendance = student.get_attendance_percentage(course.course_id)
            grade = student.get_grade(course.course_id)

            existing = activities.get_certificate(student, course)

            if existing:
                eligibility = "Issued"
            elif (attendance >= MIN_ATTENDANCE_FOR_CERTIFICATE
                    and grade != "Not Graded"):
                eligibility = "Eligible"
            else:
                eligibility = "Not yet"

            kpis([
                ("✅", "Attendance", f"{attendance}%",
                 f"minimum {MIN_ATTENDANCE_FOR_CERTIFICATE}%"),
                ("🏆", "Grade", grade),
                ("📜", "Certificate", eligibility),
            ])


            if existing:

                render_certificate(existing)

            else:

                if st.button("Issue Certificate", type="primary"):

                    success, certificate, message = (
                        activities.issue_certificate(student, course)
                    )

                    if success:

                        flash("cert_flash", message)

                        st.rerun()

                    else:

                        st.error(message)


# ============================================================
#                    PROGRESS REPORT
# ============================================================

elif menu == "📊 Progress Report":

    page_header(
        "📊", "Student Progress Report",
        "Attendance, grades and fee status for every course."
    )

    student = select_student()


    if student is not None:

        report = activities.generate_progress_report(student)


        if not report:

            st.info("This student is not enrolled in any courses.")

        else:

            kpis([
                ("💰", "Total Fees", money(student.get_total_fee_due())),
                ("✅", "Paid", money(student.get_fees_paid())),
                ("⏳", "Balance", money(student.get_total_balance())),
            ])

            show_table(
                with_status_labels(
                    pd.DataFrame(report).rename(
                        columns={"Fee Status": "Status"}
                    )
                ),
                column_config={
                    "Attendance %": st.column_config.ProgressColumn(
                        "Attendance",
                        min_value=0,
                        max_value=100,
                        format="%.0f%%"
                    )
                }
            )


# ============================================================
#                         FOOTER
# ============================================================

html(
    theme.footer_html(
        Institution.institution_name,
        Institution.location
    )
)