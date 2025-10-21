
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

# ✅ 這裡要用 __name__ 而不是 name
app = Flask(__name__)

# ✅ 問答集（中英互譯）
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



# ✅ 問答頁面
@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        q = request.form['question']
        # ✅ 加上防呆：如果輸入不存在，顯示提示文字
        a = questions_answers.get(q, "抱歉，字典裡沒有這個詞。")
        return render_template('ask.html', question=q, answer=a)
    return render_template('ask.html', question="", answer="")

# ✅ 主程式啟動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    app.run(debug=True)
