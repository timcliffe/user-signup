from flask import Flask, request, render_template

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def sign_up():


@app.route("/")
def index():
    return render_template("index.html")

app.run