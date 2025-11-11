
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competition')
def competition():
    return render_template('competition.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/club')
def club():
    return render_template('club.html')

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')
from flask import Flask, render_template, request


app = Flask(__name__)
questions_answers = {
    "蘋果": "apple",
    "apple": "蘋果",
    "香蕉": "banana",
    "banana": "香蕉",
    "貓": "cat",
    "cat": "貓",
    "狗": "dog",
    "dog": "狗",
    "書": "book",
    "book": "書",
    "桌子": "table",
    "table": "桌子",
    "椅子": "chair",
    "chair": "椅子",
    "房子": "house",
    "house": "房子",
    "汽車": "car",
    "car": "汽車",
    "學校": "school",
    "school": "學校",
    "老師": "teacher",
    "teacher": "老師",
    "學生": "student",
    "student": "學生",
    "咖啡": "coffee",
    "coffee": "咖啡",
    "茶": "tea",
    "tea": "茶",
    "醫生": "doctor",
    "doctor": "醫生",
    "護士": "nurse",
    "nurse": "護士",
    "sad": "難過",
    "難過": "sad"
}
if __name__ == '__main__':
    app.run(debug=True)
