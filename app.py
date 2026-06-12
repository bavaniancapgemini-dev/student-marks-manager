from flask import *
from database_v2 import *
from auth import *

app = Flask(__name__)

@app.route("/")
def home():

    return redirect("/login")


@app.route("/students")
def students():

    data = view_students_db()

    return render_template(
        "students.html",
        students=data
    )


@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        if check_login(
            username,
            password
        ):

            return redirect(
                "/dashboard"
            )

        return "Invalid Login"

    return render_template(
        "login.html"
    )


@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html"
    )

@app.route(
    "/add_student",
    methods=["GET", "POST"]
)
def add_student():

    if request.method == "POST":

        name = request.form["name"]

        marks = int(
            request.form["marks"]
        )

        add_student_db(
            name,
            marks
        )

        return redirect(
            "/students"
        )

    return render_template(
        "add_student.html"
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )

@app.route(
    "/add_student",
    methods=["GET", "POST"]
)
def add_student():

    if request.method == "POST":

        name = request.form["name"]

        marks = int(
            request.form["marks"]
        )

        add_student_db(
            name,
            marks
        )

        return redirect(
            "/students"
        )

    return render_template(
        "add_student.html"
    )