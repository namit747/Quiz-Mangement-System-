import random

print("Program running from:", __file__) 
# ADD QUESTION
# ------------------------

def add_question():

    question = input("Enter question: ")

    option_a = input("Option A: ")
    option_b = input("Option B: ")
    option_c = input("Option C: ")
    option_d = input("Option D: ")

    answer = input(
        "Correct Answer (A/B/C/D): "
    ).upper() #added .upper in case input is in lowercase a,b,c,d

    with open("questions.txt", "a") as file:   #creating txt file to store questions

        file.write(
            f"{question}|{option_a}|{option_b}|"
            f"{option_c}|{option_d}|{answer}\n"
        )

    print("DEBUG: Question written to file")
    print("Question Added Successfully!\n")


# LOAD QUESTIONS
# ------------------------

def load_questions():

    questions = []

    try:

        with open("questions.txt", "r") as file:

            for line in file:

                data = line.strip().split("|")

                question = {
                    "question": data[0],
                    "options": [
                        f"A. {data[1]}",
                        f"B. {data[2]}",
                        f"C. {data[3]}",
                        f"D. {data[4]}"
                    ],
                    "answer": data[5]
                }

                questions.append(question)

    except FileNotFoundError:

        print("No questions found.")

    return questions


# VIEW QUESTIONS
# ------------------------

def view_questions():

    questions = load_questions()

    if len(questions) == 0:
        print("No questions available.\n")
        return

    print("\nQUESTION BANK")

    for i, q in enumerate(questions, start=1):

        print(f"\nQuestion {i}")
        print(q["question"])

        for option in q["options"]:
            print(option)

        print("Answer:", q["answer"])


# ASK QUESTION
# ------------------------

def ask_question(question, options, answer):

    print("\n" + question)

    for option in options:
        print(option)

    user_answer = input(
        "Enter your choice: "
    ).upper()

    if user_answer == answer:
        return 1, user_answer
    return 0, user_answer
 


# SAVE SCORE
# ------------------------

def save_score(
        name,
        score,
        total,
        percentage
):

    with open("scores.txt", "a") as file:

        file.write(
            f"{name},{score}/{total},"
            f"{percentage:.2f}%\n"
        )


# VIEW SCORE HISTORY
# ------------------------

def view_scores():

    try:

        with open("scores.txt", "r") as file:

            print("\n===== SCORE HISTORY =====")

            for line in file:
                print(line.strip())

    except FileNotFoundError:

        print("No score history found.")



# TAKE QUIZ
# ------------------------

def take_quiz():

    questions = load_questions()

    if len(questions) == 0:

        print("No questions available.")
        return

    random.shuffle(questions)

    name = input("Enter your name: ")

    score = 0

    # this i
    wrong_questions = []

    for i, q in enumerate(questions, start=1):

        print(
            f"\n----- Question {i}/{len(questions)} -----"
        )

        points, user_answer = ask_question(
            q["question"],
            q["options"],
            q["answer"]
        )

        score += points

        # Save wrong answers for review
        if user_answer != q["answer"]:

            wrong_questions.append(
                {
                    "question": q["question"],
                    "your_answer": user_answer,
                    "correct_answer": q["answer"]
                }
            )

    total = len(questions)

    percentage = (
        score / total
    ) * 100

    print("\n===== RESULT =====")

    print(
        f"Score: {score}/{total}"
    )

    print(
        f"Percentage: {percentage:.2f}%"
    )

    save_score(
        name,
        score,
        total,
        percentage
    )

    print("Score Saved!")

    # Review section
    choice = input(
        "\nReview incorrect answers? (Y/N): "
    ).upper()

    if choice == "Y":

        if len(wrong_questions) == 0:

            print(
                "\nPerfect score! No mistakes."
            )

        else:

            print("\n===== REVIEW =====")

            for i, item in enumerate(
                    wrong_questions,
                    start=1
            ):

                print(
                    f"\nMistake {i}"
                )

                print(
                    "Question:",
                    item["question"]
                )

                print(
                    "Your Answer:",
                    item["your_answer"]
                )

                print(
                    "Correct Answer:",
                    item["correct_answer"]
                )


# MAIN MENU
# ------------------------

while True:

    print("\n")
    print("=" * 40)
    print("QUIZ MANAGEMENT SYSTEM") #title here
    print("=" * 40)

    print("1. Add Question")
    print("2. View Questions")
    print("3. Take Quiz")
    print("4. View Score History")
    print("5. Exit")

    choice = input(
        "Enter choice: "
    )

    if choice == "1":

        add_question()

    elif choice == "2":

        view_questions()

    elif choice == "3":

        take_quiz()

    elif choice == "4":

        view_scores()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid Choice")