from flask import Flask, request, render_template

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "":
        username_error = "invalid username"
    if password = "":
        password_error = "invalid password"
    if verify_error = "":
        verify_error = "invalid verification"
    if email = "":
        email_error = "invalid email"


@app.route("/")
def index():
    return render_template("index.html")

app.run