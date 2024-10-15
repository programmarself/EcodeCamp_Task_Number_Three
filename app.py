from quiz_data import questions

def play_quiz():
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    play_quiz()
