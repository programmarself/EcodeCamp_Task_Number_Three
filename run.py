from flask import Flask, render_template, request, redirect, url_for
from quiz_data import questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        user_answer = request.form.get(f"answer{i+1}")
        if user_answer == question["answer"]:
            score += 1
    return f"Your score is {score}/{len(questions)}!"

if __name__ == '__main__':
    app.run(debug=True)
