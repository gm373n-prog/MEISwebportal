from flask import Flask, flash, render_template, request, redirect, url_for, session
import json
import os
import smtplib
from email.message import EmailMessage
import resend

resend.api_key = "re_Knz7FQQK_21gBCZUsuCQQssRY7nU4cQzA"
app = Flask(__name__)
app.secret_key = "MEIS_2026_SECRET_KEY"
EMAIL_ADDRESS = "g40834942@gmail.com"
EMAIL_APP_PASSWORD = "weznauvnclqtjyzr"

# ============================================
# ADD EVENTS
# ============================================
@app.route("/add_event", methods=["GET", "POST"])
def add_event():

    if request.method == "POST":

        title = request.form["title"]
        date = request.form["date"]
        description = request.form["description"]

        if os.path.exists("events.json"):
            with open("events.json", "r") as f:
                events = json.load(f)
        else:
            events = []

        events.append({
            "title": title,
            "date": date,
            "description": description
        })

        with open("events.json", "w") as f:
            json.dump(events, f, indent=4)

        flash("✅ Event added successfully!")

        return redirect(url_for("events_page"))

    return render_template("add_event.html")

# ============================================
# LOAD FEES
# ============================================

def load_fees():

    with open("fees.json", "r") as file:
        return json.load(file)


def save_fees(data):

    with open("fees.json", "w") as file:
        json.dump(data, file, indent=4)

# ============================================
# LOAD ATTENDANCE
# ============================================

def load_attendance():

    with open("attendance.json", "r") as file:
        return json.load(file)


def save_attendance(data):

    with open("attendance.json", "w") as file:
        json.dump(data, file, indent=4)

# =====================================================
# RESULTS
# =====================================================

def load_results():

    try:

        with open("results.json", "r") as file:

            return json.load(file)

    except:

        return {}


def save_results(data):

    with open("results.json", "w") as file:

        json.dump(data, file, indent=4)

# =====================================================
# MARKS SYSTEM
# =====================================================

def load_marks():

    try:

        with open("marks.json", "r") as file:

            return json.load(file)

    except:

        return {}



def save_marks(data):

    with open("marks.json", "w") as file:

        json.dump(data, file, indent=4)

# =====================================================
# ANNOUNCEMENTS
# =====================================================

announcements = [

    {
        "title": "Welcome to MEIS",
        "description": "Muhammadan Educational Institute of Science welcomes all students to the new academic session."
    }

]

# =====================================================
# EVENTS
# =====================================================

events = [

    {
        "title": "Science Exhibition",
        "description": "Annual Science Exhibition will be held in the Main Hall."
    }

]

# =====================================================
# USERS
# =====================================================

users = [

{
    "username": "kashif raza",
    "email": "principal@meis.edu.pk",
    "password": "Principal@2026",
    "role": "principal",
    "name": "Muhammad Kashif Raza",

},

    {
    "username": "Miss Beenish",
    "email": "teacher@meis.edu.pk",
    "password": "Teacher@2026",
    "role": "teacher",
    "name": "Miss Beenish",

    "subjects": [
        "Chemistry",
        "Biology",
        "English"
    ]
},



{
    "username": "Miss Shaheen",
    "email": "shaheen@meis.edu.pk",
    "password": "Shaheen2026",
    "role": "teacher",
    "name": "Miss Shaheen Naz Hashmi",

    "subjects": [
        "Islamiat",
        "Pakistan Studies",
        "Tarjuma-tul-Quran",
        "Handwriting"
    ]
},
{
    "username": "Sir Kashif",
    "email": "kashif@meis.edu.pk",
    "password": "Kashif2026",
    "role": "teacher",
    "name": "Sir Kashif",

    "subjects": [
        "Physics",
        "Mathematics",
        "Computer"
    ]
},

    {
    "username": "kaleemullah",
    "email": "kaleemullah@meis.edu.pk",
    "password": "Kal33m2026",
    "role": "student",
    "name": "Kaleemullah",
    "class": "9th",
    "group": "Computer",
    "attendance": 100,
    "fee_status": "Paid"
},

    {
        "username": "samiullah",
        "email": "samiullah@meis.edu.pk",
        "password": "Sam1ullah2026",
        "role": "student",
        "name": "Samiullah",
        "class": "9th",
        "group": "Computer",
        "attendance": 95,
        "fee_status": "Paid"
    },

    {
        "username": "raffay",
        "email": "raffay@meis.edu.pk",
        "password": "Raffay2026",
        "role": "student",
        "name": "Raffay",
        "class": "9th",
        "group": "Computer",
        "attendance": 90,
        "fee_status": "Paid"
    },

    {
        "username": "bisma",
        "email": "bisma@meis.edu.pk",
        "password": "Bisma2026",
        "role": "student",
        "name": "Bisma",
        "class": "9th",
        "group": "Computer",
        "attendance": 85,
        "fee_status": "Paid"
    },

    {
        "username": "subhan",
        "email": "subhan@meis.edu.pk",
        "password": "Subhan2026",
        "role": "student",
        "name": "Subhan",
        "class": "9th",
        "group": "Computer",
        "attendance": 80,
        "fee_status": "Paid"
    },

    {
        "username": "moiz",
        "email": "moiz@meis.edu.pk",
        "password": "Moiz2026",
        "role": "student",
        "name": "Moiz",
        "class": "10th",
        "group": "Computer",
        "attendance": 75,
        "fee_status": "Paid"
    },

    {
        "username": "tuba",
        "email": "tuba@meis.edu.pk",
        "password": "Tuba2026",
        "role": "student",
        "name": "Tuba",
        "class": "10th",
        "group": "Biology",
        "attendance": 70,
        "fee_status": "Paid"
    },

    {
        "username": "hadi",
        "email": "hadi@meis.edu.pk",
        "password": "Hadi2026",
        "role": "student",
        "name": "Hadi",
        "class": "10th",
        "group": "Biology",
        "attendance": 65,
        "fee_status": "Paid"
    },

    {
        "username": "sadoon",
        "email": "sadoon@meis.edu.pk",
        "password": "Sadoon2026",
        "role": "student",
        "name": "Sadoon",
        "class": "10th",
        "group": "Biology",
        "attendance": 60,
        "fee_status": "Paid"
    },

    {
        "username": "maryam",
        "email": "maryam@meis.edu.pk",
        "password": "Maryam2026",
        "role": "student",
        "name": "Maryam",
        "class": "10th",
        "group": "Computer",
        "attendance": 55,
        "fee_status": "Paid"
    },

    {
        "username": "hareem",
        "email": "hareem@meis.edu.pk",
        "password": "hareem123",
        "role": "student",
        "name": "Hareem",
        "class": "9th",
        "group": "Computer",
        "attendance": 0,
        "fee_status": "Paid"
    },
    {
        "username": "shehryar",
        "email": "shehryar@meis.edu.pk",
        "password": "shehryar123",
        "role": "student",
        "name": "Shehryar",
        "class": "9th",
        "group": "Computer",
        "attendance": 0,
        "fee_status": "Paid"
    },
    {
        "username": "Qadan",
        "email": "qadan@meis.edu.pk",
        "password": "qadan123",
        "role": "student",
        "name": "Qadan",
        "class": "2nd Year",
        "group": "Statistics",
        "attendance": 0,
        "fee_status": "Paid"
    },
    {
        "username": "shahzain",
        "email": "Shahzain@meis.edu.pk",
        "password": "Shahzain123",
        "role": "student",
        "name": "Shahzain",
        "class": "9th",
        "group": "Computer",
        "attendance": 0,
        "fee_status": "Paidd"
    },
    {
        "username": "Qirat",
        "email": "Qirat@meis.edu.pk",
        "password": "Qirat123",
        "role": "student",
        "name": "Qirat",
        "class": "7th",
        "group": "Computer",
        "attendance": 0,
        "fee_status": "Paid"
    },
     {
        "username": "Ibrahim",
        "email": "Ibrahim@meis.edu.pk",
        "password": "Ibrahim123",
        "role": "student",
        "name": "Ibrahim",
        "class": "1st Year",
        "group": "Computer",
        "attendance": 0,
        "fee_status": "Paid"
    },
]
#======================================================#
#CLASS SUBJECTS
#======================================================#

CLASS_SUBJECTS = {

    ("7th", ""): [
        "English",
        "Urdu",
        "Mathematics",
        "Science",
        "Islamiat"
    ],

    ("9th", "Computer"): [
        "Computer",
        "Physics",
        "Mathematics",
        "Chemistry",
        "English",
        "Urdu",
        "Islamiat",
        "Pakistan Studies",
        "Tarjuma-tul-Quran"
    ],

    ("1st Year", "Computer"): [
        "Computer",
        "Physics",
        "Mathematics",
        "English",
        "Urdu",
        "Islamiat",
        "Pakistan Studies"
    ],

    ("2nd Year", "Computer"): [
        "Computer",
        "Statistics",
        "Mathematics",
        "English",
        "Urdu",
        "Islamiat",
        "Pakistan Studies"
    ]
}

# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():

    if os.path.exists("events.json"):
        with open("events.json", "r") as f:
            events = json.load(f)
    else:
        events = []

    return render_template(
        "index.html",
        announcements=announcements,
        events=events
    )

# =====================================================
# ABOUT
# =====================================================

@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        try:
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": ["g40834942@gmail.com@gmail.com"],
                "subject": "New Website Contact Message",
                "text": f"""
Name: {name}

Email: {email}

Message:
{message}
"""
            })

            return render_template(
                "contact.html",
                success=True
            )

        except Exception as e:
            return f"Error: {e}"

    return render_template("contact.html")
# =====================================================
# EVENTS
# =====================================================

@app.route("/events")
def events_page():

    if os.path.exists("events.json"):
        with open("events.json", "r") as f:
            events = json.load(f)
    else:
        events = []

    return render_template(
        "events.html",
        events=events
    )
# =====================================================
# ANNOUNCEMENTS
# =====================================================

@app.route("/announcements")
def announcements_page():

    return render_template(
        "announcements.html",
        announcements=announcements
    )
# =====================================================
# LOGIN
# =====================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":

        login_input = request.form["username"].strip()

        password = request.form["password"]

        for user in users:

            if (
                login_input == user["username"]
                or login_input == user["email"]
            ) and password == user["password"]:

                session["name"] = user["name"]

                session["role"] = user["role"]

                session["email"] = user["email"]

                session["username"] = user["username"]

                session["class"] = user.get("class", "")

                if user["role"] == "principal":

                    return redirect(url_for("principal_dashboard"))

                elif user["role"] == "teacher":

                    return redirect(url_for("teacher_dashboard"))

                elif user["role"] == "student":

                    return redirect(url_for("student_dashboard"))

        error = "Invalid Username/Email or Password."

    return render_template(
        "login.html",
        error=error
    )


# =====================================================
# PRINCIPAL DASHBOARD
# =====================================================

@app.route("/principal_dashboard")
def principal_dashboard():

    if session.get("role") != "principal":

        return redirect(url_for("login"))

    return render_template("principal_dashboard.html")


# =====================================================
# ADD ANNOUNCEMENT
# =====================================================

@app.route("/add_announcement", methods=["GET", "POST"])
def add_announcement():

    if session.get("role") != "principal":

        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]

        description = request.form["description"]

        announcements.append({

            "title": title,

            "description": description

        })

        return redirect(url_for("home"))

    return render_template("add_announcement.html")


# =====================================================
# TEACHER DASHBOARD
# =====================================================

@app.route("/teacher_dashboard")
def teacher_dashboard():

    if session.get("role") != "teacher":
        return redirect(url_for("login"))

    return render_template("teacher_dashboard.html")

 
  # =====================================================
# STUDENT DASHBOARD
# =====================================================

@app.route("/student_dashboard")
def student_dashboard():

    if session.get("role") != "student":
        return redirect(url_for("login"))

    attendance_data = load_attendance()
    fees_data = load_fees()

    username = session.get("username")

    attendance = attendance_data.get(username, "Present")
    fee_status = fees_data.get(username, "Pending")

    return render_template(
        "student_dashboard.html",
        attendance=attendance,
        fee_status=fee_status
    )

# =====================================================
# VIEW TEACHERS
# =====================================================

@app.route("/teachers")
def teachers():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    teacher_list = []

    for user in users:
        if user["role"] == "teacher":
            teacher_list.append(user)

    return render_template(
        "teachers.html",
        teachers=teacher_list
    )

# =====================================================
# FEES MANAGEMENT
# =====================================================

@app.route("/fees", methods=["GET", "POST"])
def fees():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    fees_data = load_fees()

    # Save changes
    if request.method == "POST":

        for user in users:

            if user["role"] == "student":

                username = user["username"]

                fees_data[username] = request.form.get(username)

        save_fees(fees_data)

    student_list = []

    for user in users:

        if user["role"] == "student":

            student = user.copy()

            student["fee_status"] = fees_data.get(
                student["username"],
                "Pending"
            )

            student_list.append(student)

    return render_template(
        "fees.html",
        students=student_list
    )
# =====================================================
# SUBJECTS
# =====================================================

@app.route("/subjects")
def subjects():

    if "role" not in session:
        return redirect(url_for("login"))

    return render_template("subjects.html")

# =====================================================
# ATTENDANCE
# =====================================================

@app.route("/attendance", methods=["GET", "POST"])
def attendance():

    if session.get("role") not in ["principal", "teacher"]:
        return redirect(url_for("login"))

    attendance_data = load_attendance()

    if request.method == "POST":

        for user in users:

            if user["role"] == "student":

                username = user["username"]

                attendance_data[username] = request.form.get(username)

        save_attendance(attendance_data)

    student_list = []

    for user in users:

        if user["role"] == "student":

            student = user.copy()

            student["attendance"] = attendance_data.get(
                student["username"],
                "Present"
            )

            student_list.append(student)

    return render_template(
        "attendance.html",
        students=student_list
    )
# =====================================================
# VIEW STUDENTS
# =====================================================
@app.route("/students")
def students():

    if session.get("role") not in ["teacher", "principal"]:
        return redirect(url_for("login"))

    student_list = []

    for user in users:
        if user["role"] == "student":
            student_list.append(user)

    return render_template(
        "students.html",
        students=student_list
    )

# =====================================================
# SUBJECTS BY CLASS & GROUP
# =====================================================

def get_subjects(student_class, group):

    # 7th
    if student_class == "7th":
        return [
            "English",
            "Urdu",
            "Mathematics",
            "General Science",
            "Islamiat",
            "Pakistan Studies",
            "Tarjuma-tul-Quran"
        ]

    # 9th & 10th Computer
    elif student_class in ["9th", "10th"] and group == "Computer":
        return [
            "English",
            "Urdu",
            "Physics",
            "Mathematics",
            "Computer",
            "Chemistry",
            "Islamiat",
            "Pakistan Studies",
            "Tarjuma-tul-Quran"
        ]

    # 9th & 10th Biology
    elif student_class in ["9th", "10th"] and group == "Biology":
        return [
            "English",
            "Urdu",
            "Physics",
            "Chemistry",
            "Biology",
            "Islamiat",
            "Pakistan Studies",
            "Tarjuma-tul-Quran"
        ]

    # 1st Year Computer
    elif student_class == "1st Year":
        return [
            "English",
            "Urdu",
            "Physics",
            "Mathematics",
            "Computer",
            "Pakistan Studies",
            "Tarjuma-tul-Quran"
        ]

    # 2nd Year Statistics
    elif student_class == "2nd Year" and group == "Statistics":
        return [
            "English",
            "Urdu",
            "Physics",
            "Mathematics",
            "Statistics",
            "Pakistan Studies",
            "Tarjuma-tul-Quran"
        ]

    return []
# =====================================================
# MARKS
# =====================================================
@app.route("/marks", methods=["GET", "POST"])
def marks():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    marks_data = load_marks()

    teacher_subjects = [
        "Physics",
        "Mathematics",
        "Computer",
        "Chemistry",
        "Biology",
        "English",
        "Urdu",
        "Islamiat",
        "Tarjuma-tul-Quran",
        "Pakistan Studies"
    ]

    selected_class = ""
    selected_group = "General"
    student_list = []

    display_subjects = teacher_subjects

    if request.method == "POST":

        selected_class = request.form.get("selected_class", "")
        selected_group = request.form.get("selected_group", "General")
        action = request.form.get("action")

        # -----------------------------
        # Subjects according to Group
        # -----------------------------
        display_subjects = get_subjects(
            selected_class,
            selected_group
)

        # -----------------------------
        # Load Students
        # -----------------------------
        for user in users:

            if user["role"] != "student":
                continue

            if selected_class and user.get("class") != selected_class:
                continue

            if (
                selected_group != "General"
                and user.get("group") != selected_group
            ):
                continue

            student = user.copy()
            student["marks"] = marks_data.get(student["username"], {})
            student_list.append(student)

        # -----------------------------
        # Save Marks
        # -----------------------------
        if action == "save":

            test_name = request.form.get("test")

            for student in student_list:

                username = student["username"]

                if username not in marks_data:
                    marks_data[username] = {}

                for subject in display_subjects:

                    status = request.form.get(
                        f"{username}_{subject}_status",
                        "Present"
                    )

                    obtained = request.form.get(
                        f"{username}_{subject}_obtained",
                        ""
                    )

                    total = request.form.get(
                        f"{username}_{subject}_total",
                        ""
                    )

                    if subject not in marks_data[username]:
                        marks_data[username][subject] = {}

                    marks_data[username][subject][test_name] = {
                        "status": status,
                        "obtained": obtained,
                        "total": total
                    }

            save_marks(marks_data)

            return redirect(url_for("marks"))

    return render_template(
        "marks.html",
        students=student_list,
        subjects=display_subjects,
        selected_class=selected_class,
        selected_group=selected_group
    )

# =====================================================
# PRINCIPAL RESULTS
# =====================================================
@app.route("/principal_results", methods=["GET", "POST"])
def principal_results():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    marks_data = load_marks()

    selected_class = ""
    selected_group = "General"
    selected_student = ""

    students = []

    result = None
    obtained_total = 0
    grand_total = 0
    percentage = 0
    position = None
    student_name = ""

    if request.method == "POST":

        action = request.form.get("action")

        selected_class = request.form.get("selected_class", "")
        selected_group = request.form.get("selected_group", "General")
        selected_student = request.form.get("student", "")

        # -----------------------------
        # Load Students
        # -----------------------------
        for user in users:

            if user["role"] != "student":
                continue

            if selected_class and user.get("class") != selected_class:
                continue

            if (
                selected_group != "General"
                and user.get("group") != selected_group
            ):
                continue

            students.append(user)

        # -----------------------------
        # Generate Result
        # -----------------------------
        if action == "generate" and selected_student:

            # Student Name
            for stu in students:

                if stu["username"] == selected_student:

                    student_name = stu["name"]
                    break

            result = marks_data.get(selected_student, {})

            # -----------------------------
            # Subjects According to Class
            # -----------------------------
            allowed_subjects = get_subjects(
                selected_class,
                selected_group
            )

            result = {
                subject: result[subject]
                for subject in allowed_subjects
                if subject in result
            }

            # -----------------------------
            # Calculate Totals
            # -----------------------------
            for subject, tests in result.items():

                for test, mark in tests.items():

                    if mark.get("status") == "Present":

                        obtained_total += int(
                            mark.get("obtained") or 0
                        )

                        grand_total += int(
                            mark.get("total") or 0
                        )

            if grand_total > 0:

                percentage = round(
                    (obtained_total / grand_total) * 100,
                    2
                )

            # -----------------------------
            # Calculate Position
            # -----------------------------
            percentages = []

            for stu in students:

                stu_marks = marks_data.get(
                    stu["username"],
                    {}
                )

                obt = 0
                tot = 0

                stu_subjects = get_subjects(
                    stu.get("class"),
                    stu.get("group", "General")
                )

                for subject in stu_subjects:

                    if subject not in stu_marks:
                        continue

                    for test, mark in stu_marks[subject].items():

                        if mark.get("status") == "Present":

                            obt += int(
                                mark.get("obtained") or 0
                            )

                            tot += int(
                                mark.get("total") or 0
                            )

                if tot > 0:
                    per = round((obt / tot) * 100, 2)
                else:
                    per = 0

                percentages.append(
                    (
                        stu["username"],
                        per
                    )
                )

            percentages.sort(
                key=lambda x: x[1],
                reverse=True
            )

            for i, item in enumerate(percentages):

                if item[0] == selected_student:

                    position = i + 1
                    break

    return render_template(
        "principal_results.html",
        students=students,
        result=result,
        student_name=student_name,
        selected_class=selected_class,
        selected_group=selected_group,
        selected_student=selected_student,
        obtained_total=obtained_total,
        grand_total=grand_total,
        percentage=percentage,
        position=position
    )

# =====================================================
# MERIT LIST
# =====================================================
@app.route("/merit_list", methods=["GET", "POST"])
def merit_list():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    marks_data = load_marks()

    selected_class = ""
    selected_group = "General"

    merit = []

    if request.method == "POST":

        selected_class = request.form.get("selected_class", "")
        selected_group = request.form.get("selected_group", "General")

        for user in users:

            if user["role"] != "student":
                continue

            if selected_class and user.get("class") != selected_class:
                continue

            if (
                selected_group != "General"
                and user.get("group") != selected_group
            ):
                continue

            stu_marks = marks_data.get(
                user["username"],
                {}
            )

            obtained = 0
            total = 0

            # -----------------------------
            # Get Correct Subjects
            # -----------------------------
            subjects = get_subjects(
                user.get("class"),
                user.get("group", "General")
            )

            for subject in subjects:

                if subject not in stu_marks:
                    continue

                for test, mark in stu_marks[subject].items():

                    if mark.get("status") == "Present":

                        obtained += int(
                            mark.get("obtained") or 0
                        )

                        total += int(
                            mark.get("total") or 0
                        )

            if total > 0:

                percentage = round(
                    (obtained / total) * 100,
                    2
                )

            else:

                percentage = 0

            merit.append({

                "name": user["name"],
                "class": user.get("class"),
                "group": user.get("group", "General"),
                "percentage": percentage

            })

        merit.sort(
            key=lambda x: x["percentage"],
            reverse=True
        )

    return render_template(
        "merit_list.html",
        merit=merit,
        selected_class=selected_class,
        selected_group=selected_group
    )

# =====================================================
# TOP 3 STUDENTS
# =====================================================
@app.route("/top3_students", methods=["GET", "POST"])
def top3_students():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    marks_data = load_marks()

    selected_class = ""
    selected_group = "General"

    top3 = []

    if request.method == "POST":

        selected_class = request.form.get("selected_class", "")
        selected_group = request.form.get("selected_group", "General")

        percentages = []

        for user in users:

            if user["role"] != "student":
                continue

            if selected_class and user.get("class") != selected_class:
                continue

            if (
                selected_group != "General"
                and user.get("group") != selected_group
            ):
                continue

            stu_marks = marks_data.get(
                user["username"],
                {}
            )

            obtained = 0
            total = 0

            # -----------------------------
            # Correct Subjects
            # -----------------------------
            subjects = get_subjects(
                user.get("class"),
                user.get("group", "General")
            )

            for subject in subjects:

                if subject not in stu_marks:
                    continue

                for test, mark in stu_marks[subject].items():

                    if mark.get("status") == "Present":

                        obtained += int(
                            mark.get("obtained") or 0
                        )

                        total += int(
                            mark.get("total") or 0
                        )

            percentage = (
                round((obtained / total) * 100, 2)
                if total else 0
            )

            percentages.append({

                "name": user["name"],
                "class": user.get("class"),
                "group": user.get("group", "General"),
                "percentage": percentage

            })

        percentages.sort(
            key=lambda x: x["percentage"],
            reverse=True
        )

        top3 = percentages[:3]

    return render_template(
        "top_3_students.html",
        top3=top3,
        selected_class=selected_class,
        selected_group=selected_group
    )
# =====================================================
# STUDENT RESULTS
# =====================================================

@app.route("/results")
def results():

    if session.get("role") != "student":
        return redirect(url_for("login"))

    marks_data = load_marks()

    username = session.get("username")

    student_marks = marks_data.get(username, {})

    return render_template(
        "results.html",
        marks=student_marks
    )

# =====================================================
# CLASS ANALYTICS
# =====================================================
@app.route("/analytics", methods=["GET", "POST"])
def analytics():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    marks_data = load_marks()

    selected_class = ""
    selected_group = "General"

    total_students = 0
    average_percentage = 0
    highest_percentage = 0
    lowest_percentage = 0
    pass_students = 0
    fail_students = 0
    pass_percentage = 0

    if request.method == "POST":

        selected_class = request.form.get("selected_class", "")
        selected_group = request.form.get("selected_group", "General")

        percentages = []

        for user in users:

            if user["role"] != "student":
                continue

            if selected_class and user.get("class") != selected_class:
                continue

            if (
                selected_group != "General"
                and user.get("group") != selected_group
            ):
                continue

            total_students += 1

            stu_marks = marks_data.get(
                user["username"],
                {}
            )

            obtained = 0
            total = 0

            # -----------------------------
            # Correct Subjects
            # -----------------------------
            subjects = get_subjects(
                user.get("class"),
                user.get("group", "General")
            )

            for subject in subjects:

                if subject not in stu_marks:
                    continue

                for test, mark in stu_marks[subject].items():

                    if mark.get("status") == "Present":

                        obtained += int(
                            mark.get("obtained") or 0
                        )

                        total += int(
                            mark.get("total") or 0
                        )

            if total > 0:

                per = round(
                    (obtained / total) * 100,
                    2
                )

            else:

                per = 0

            percentages.append(per)

            if per >= 40:
                pass_students += 1
            else:
                fail_students += 1

        if percentages:

            average_percentage = round(
                sum(percentages) / len(percentages),
                2
            )

            highest_percentage = max(percentages)
            lowest_percentage = min(percentages)

        if total_students > 0:

            pass_percentage = round(
                (pass_students / total_students) * 100,
                2
            )

    return render_template(
        "analytics.html",
        total_students=total_students,
        average_percentage=average_percentage,
        highest_percentage=highest_percentage,
        lowest_percentage=lowest_percentage,
        pass_students=pass_students,
        fail_students=fail_students,
        pass_percentage=pass_percentage
    )

# =====================================================
# LOGOUT
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":

    app.run(debug=True)