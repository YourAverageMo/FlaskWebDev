import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask

#loading env variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
FLASK_APP = os.getenv("FLASK_APP")

app = Flask(__name__)


def make_bold(func):

    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


@app.route('/')
@make_bold
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"\
            "<p>This is a paragraph.</p>"\
            "<img src='https://media.giphy.com/media/Puc4FZWExJc0E/giphy.gif?cid=ecf05e47ptecxelrpt3vmdnbyy03sv0pq87x31u8luqtic9f&rid=giphy.gif&ct=g' width=200>"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)