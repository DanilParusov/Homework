from flask import Flask
import json

app = Flask(__name__)

def load_canditates():
    with open("candidates_json", 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data

dictionary = load_canditates()

@app.route("/")
def get_all():
    for i in range(0, 7):
        name = f"Имя - {dictionary[i]['name']}\nПозиция: {dictionary[i]['position']}\nНавыки: {dictionary[i]['skills']}\n "
        yield name

@app.route("/candidates/<pk>")
def get_by_pk(pk):
    pk = int(pk) - 1
    name = dictionary[pk]['name']
    position = dictionary[pk]['position']
    skills = dictionary[pk]['skills']
    url = dictionary[pk]['picture']
    return f"{url}\n{name}\n{position}\n{skills}"

@app.route("/skills/<skill_name>")
def get_by_skill(skill_name):
    for i in range(0, 7):
        person_skills = str(dictionary[i]["skills"]).lower()
        if skill_name in person_skills:
            yield f"{dictionary[i]['name']}\n"


app.run()

