# pip install flask
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>안녕, 권정빈!</p>"


@app.route("/posts")
def post_list():
    return """
    <DOCTYPE html>
    <html lang="ko">

    <head>
        <title>웹 문서 만들기</title>
        <style>
            body {
                background-color: aquamarine;
            }

            h1 {
                font-weight: bold;
                color: blueviolet;
                border-bottom: 4px dashed red;
            }

            h1:hover {
                color: seashell;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <h1>웹 개발 기초</h1>
        <p>HTML</p>
        <p>CSS</p>
        <p>자바스크립트</p>
    </body>

    </html>
    """
