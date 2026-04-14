from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def students_age():

    students = [
        {"name": "Ali", "age": 17},
        {"name": "Vali", "age": 18},
        {"name": "Hasan", "age": 16},
        {"name": "Husan", "age": 19},
        {"name": "Sardor", "age": 20}
    ]

    total_age = 0

    for s in students:
        total_age += s["age"]

    average_age = total_age / len(students)

    oldest = max(students, key=lambda x: x["age"])
    youngest = min(students, key=lambda x: x["age"])

    return render_template(
        "index.html",
        students=students,
        average_age=average_age,
        oldest=oldest,
        youngest=youngest
    )


if __name__ == "__main__":
    app.run(debug=True)
