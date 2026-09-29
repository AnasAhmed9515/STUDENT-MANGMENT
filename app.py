from flask import Flask, render_template, request, redirect, url_for, flash
import data

app = Flask(__name__)
app.secret_key = "student-result-management"


def calculate_result(student):
    marks = student["MARKS"]

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, average, grade


def get_students():
    students = []

    for rollno, student in data.student_list.items():

        total, average, grade = calculate_result(student)

        students.append({
            "rollno": rollno,
            "name": student["Name"],
            "course": student["Course"],
            "marks": student["MARKS"],
            "total": total,
            "average": average,
            "grade": grade
        })

    return students


@app.route("/")
def index():

    students = get_students()

    if students:
        top = max(students, key=lambda x: x["average"])
        class_average = sum(
            student["average"] for student in students
        ) / len(students)
    else:
        top = None
        class_average = 0

    return render_template(
        "index.html",
        students=students,
        top=top,
        total_students=len(students),
        average_class=class_average
    )


@app.route("/add", methods=["POST"])
def add_student():

    rollno = request.form["rollno"]
    name = request.form["name"]
    course = request.form["course"]

    marks = [
        int(request.form["mark1"]),
        int(request.form["mark2"]),
        int(request.form["mark3"]),
        int(request.form["mark4"]),
        int(request.form["mark5"])
    ]

    if rollno in data.student_list:

        flash("Student already exists!", "error")

        return redirect(url_for("index"))

    data.student_list[rollno] = {

        "Name": name,

        "Course": course,

        "MARKS": marks
    }
    data.save_students()
    flash("Student added successfully!", "success")

    return redirect(url_for("index"))


@app.route("/search")
def search():

    rollno = request.args.get("rollno")

    if rollno not in data.student_list:

        flash("Student not found!", "error")

        return redirect(url_for("index"))

    student = data.student_list[rollno]

    total, average, grade = calculate_result(student)

    result = {

        "rollno": rollno,

        "name": student["Name"],

        "course": student["Course"],

        "marks": student["MARKS"],

        "total": total,

        "average": average,

        "grade": grade
    }

    students = get_students()

    if students:
        top = max(students, key=lambda x: x["average"])
        class_average = sum(
            student["average"] for student in students
        ) / len(students)
    else:
        top = None
        class_average = 0

    return render_template(

        "index.html",

        students=students,

        top=top,

        total_students=len(students),

        average_class=class_average,

        search_result=result
    )


@app.route("/result/<rollno>")
def result(rollno):

    if rollno not in data.student_list:

        flash("Student not found!", "error")

        return redirect(url_for("index"))

    student = data.student_list[rollno]

    total, average, grade = calculate_result(student)

    return render_template(

        "result.html",

        rollno=rollno,

        student=student,

        total=total,

        average=average,

        grade=grade
    )


@app.route("/top")
def top_student():

    students = get_students()

    if not students:

        flash("No students available!", "error")

        return redirect(url_for("index"))

    top = max(
        students,
        key=lambda x: x["average"]
    )

    return render_template(
        "top.html",
        top=top
    )


if __name__ == "__main__":

    app.run(debug=True)