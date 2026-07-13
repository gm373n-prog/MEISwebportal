from flask import Flask, flash, render_template, request, redirect, url_for, session
import json
import os
import smtplib
from email.message import EmailMessage

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
        "fee_status": "Unpaid"
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
        "fee_status": "Unpaid"
    },
    
    

]

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

# =====================================================
# CONTACT
# =====================================================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        msg = EmailMessage()

        msg["Subject"] = "New Website Contact Message"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "g40834942@gmail.com"

        msg.set_content(
            f"""
Name: {name}

Email: {email}

Message:

{message}
"""
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                EMAIL_ADDRESS,
                EMAIL_APP_PASSWORD
            )

            smtp.send_message(msg)

        return render_template(
            "contact.html",
            success=True
        )

    return render_template(
        "contact.html"
    )

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
# MARKS
# =====================================================
@app.route("/marks", methods=["GET", "POST"])
def marks():

    if session.get("role") not in ["teacher", "principal"]:
        return redirect(url_for("login"))

    marks_data = load_marks()

    if session.get("role") == "principal":

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

    else:

        teacher_subjects = []

        for user in users:

            if (
                user["role"] == "teacher"
                and user["name"] == session.get("name")
            ):

                teacher_subjects = user.get("subjects", [])
                break

    student_list = []

    for user in users:

        if user["role"] == "student":

            student = user.copy()
            student["marks"] = marks_data.get(student["username"], {})
            student_list.append(student)

    if request.method == "POST":

        for student in student_list:

            username = student["username"]

            if username not in marks_data:
                marks_data[username] = {}

            for subject in teacher_subjects:

                value = request.form.get(
                    f"{username}_{subject}",
                    "0"
                )

                marks_data[username][subject] = int(value)

        save_marks(marks_data)

        return redirect(url_for("marks"))

    return render_template(
        "marks.html",
        students=student_list,
        subjects=teacher_subjects
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
# PRINCIPAL RESULTS
# =====================================================

@app.route("/principal_results")
def principal_results():

    if session.get("role") != "principal":
        return redirect(url_for("login"))

    marks_data = load_marks()

    subjects = [
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

    student_list = []

    for user in users:

        if user["role"] == "student":

            student = user.copy()

            student["marks"] = marks_data.get(
                student["username"],
                {}
            )

            student_list.append(student)

    return render_template(
        "principal_results.html",
        students=student_list,
        subjects=subjects
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