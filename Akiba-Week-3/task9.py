def display_question(question, number):
    """Display a question and its options."""
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(f"  {option}")


def validate_answer(answer, options):
    """Check whether the user's answer is a valid option."""
    valid_options = [option[0].lower() for option in options]

    return answer.lower() in valid_options


def check_answer(answer, correct_answer):
    """Check whether the answer is correct."""
    return answer.lower() == correct_answer.lower()


def update_score(score, is_correct):
    """Increase the score if the answer is correct."""
    if is_correct:
        return score + 1

    return score


def calculate_percentage(score, total_questions):
    """Calculate quiz percentage."""
    return (score / total_questions) * 100


def get_result_category(percentage):
    """Return a category based on the final percentage."""
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Very Good"
    elif percentage >= 50:
        return "Pass"
    else:
        return "Needs Improvement"


def display_final_results(score, total_questions):
    """Display the final quiz results."""
    incorrect = total_questions - score
    percentage = calculate_percentage(score, total_questions)
    category = get_result_category(percentage)

    print("\n========== FINAL RESULTS ==========")
    print(f"Correct answers:   {score}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Total questions:   {total_questions}")
    print(f"Score:             {percentage:.2f}%")
    print(f"Result:            {category}")
    print("===================================")


def run_quiz(questions):
    """Run one complete quiz."""
    score = 0

    for number, question in enumerate(questions, start=1):

        display_question(question, number)

        while True:
            answer = input("Your answer: ").strip()

            if validate_answer(answer, question["options"]):
                break

            print("Invalid option. Please choose one of the available options.")

        if check_answer(answer, question["correct"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print(f"Incorrect. The correct answer is {question['correct']}.")

    display_final_results(score, len(questions))


# Quiz questions
questions = [
    {
        "question": "What is the capital city of Ethiopia?",
        "options": ["A. Addis Ababa", "B. Nairobi", "C. Kampala", "D. Kigali"],
        "correct": "A"
    },
    {
        "question": "Which language is used to program Python?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "correct": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing Utility"
        ],
        "correct": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "correct": "C"
    },
    {
        "question": "Which symbol is used for a comment in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "correct": "C"
    }
]


# Main program
while True:
    print("\n===== QUIZ GAME =====")

    run_quiz(questions)

    play_again = input("\nWould you like to play again? (Y/N): ").strip()

    if play_again.lower() != "y":
        print("Thank you for playing!")
        break