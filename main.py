from flask import Flask
from u import get_all
from u import get_man
from u import get_by_skill

# http://127.0.0.1:5000/
app = Flask(__name__)


@app.route("/")
def index():
    people = get_all()
    words = "<br>"
    for i in range(0, 7):
        words += (people[i]["name"]) + "<br>"
        words += (people[i]["position"]) + "<br>"
        words += (people[i]["skills"]) + "<br>"
        words += "<br>"
    return words


@app.route('/people/<int:pk>')
def index_1(pk):
    man = get_man(pk)
    string = "<br>"
    string += man["name"] + "<br>"
    string += man["position"] + "<br>"
    string += man["skills"] + "<br>"
    return f""" <img src="{man["picture"]}"> <pre> {string} </pre>"""


@app.route("/people/<skill>")
def index_2(skill):
    people = get_by_skill(skill)
    return people


app.run()
