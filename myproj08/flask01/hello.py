# pip install flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    like_foods = [
        "묵밥",
        "김치찜",
        "항정살",
        "칼국수",
        "자장면",
    ]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
