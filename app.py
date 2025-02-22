from flask import Flask, render_template, request, session
import json
from make_questions import generate_interview_questions

app = Flask(__name__)
import os
app.secret_key = os.urandom(24)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        skill = request.form["skill"]
        level = request.form["level"]
        
        # Generate and load questions
        generate_interview_questions(skill, level)
        with open("questions.json", "r") as file:
            session["questions"] = json.load(file)["interview_questions"]
            session["current_question"] = 0
        
        return render_template("index.html", question=session["questions"][0], 
                               question_num=1, total=len(session["questions"]))

    return render_template("index.html", question=None)

@app.route("/next")
def next_question():
    if "questions" in session and session["current_question"] < len(session["questions"]) - 1:
        session["current_question"] += 1
    
    return render_template("index.html", question=session["questions"][session["current_question"]],
                           question_num=session["current_question"] + 1, total=len(session["questions"]))

@app.route("/prev")
def prev_question():
    if "questions" in session and session["current_question"] > 0:
        session["current_question"] -= 1
    
    return render_template("index.html", question=session["questions"][session["current_question"]],
                           question_num=session["current_question"] + 1, total=len(session["questions"]))

if __name__ == "__main__":
    app.run(debug=True)