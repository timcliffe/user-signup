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

    if username == "" or " " or len(username) < 3 or len(username) > 20:
        username_error = "invalid username"
    if password = "" or " " or len(password) < 3 or len(password) > 20:
        password_error = "invalid password"
    if verify = "" or verify != password:
        verify_error = "invalid verification"
    if email != "":
        if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
            email_error = "invalid email"


    if email_error == "" and username_error == "" and verify_error == "" and password_error == "":
        return render_template("welcome.html", username = username)
    else:
        return render_template("index.html", username_error = username_error,
        password_error = password_error, verify_error = verify_error, username = username,
        email = email)


@app.route("/")
def index():
    return render_template("index.html")

app.run