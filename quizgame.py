# ==========================================
#        PYTHON QUIZ GAME PROJECT
# ==========================================

def quiz_game():

    print("=" * 50)
    print("        WELCOME TO PYTHON QUIZ GAME")
    print("=" * 50)

    name = input("Enter your Name: ")

    print("\nHello", name + "!")
    print("Let's start the quiz.\n")

    questions = [
        {
            "question": "1. Which language is widely used for Data Science?",
            "options": ["A. HTML", "B. Python", "C. CSS", "D. JavaScript"],
            "answer": "B"
        },

        {
            "question": "2. Which keyword is used for decision making?",
            "options": ["A. for", "B. while", "C. if", "D. print"],
            "answer": "C"
        },

        {
            "question": "3. Which symbol is used for comments in Python?",
            "options": ["A. //", "B. /* */", "C. #", "D. --"],
            "answer": "C"
        },

        {
            "question": "4. Which function is used to display output?",
            "options": ["A. input()", "B. print()", "C. display()", "D. show()"],
            "answer": "B"
        },

        {
            "question": "5. Which function takes input from the user?",
            "options": ["A. input()", "B. print()", "C. enter()", "D. scan()"],
            "answer": "A"
        },

        {
            "question": "6. Which data type stores text?",
            "options": ["A. int", "B. float", "C. string", "D. bool"],
            "answer": "C"
        },

        {
            "question": "7. Which loop is used when the number of iterations is known?",
            "options": ["A. while", "B. do while", "C. for", "D. repeat"],
            "answer": "C"
        },

        {
            "question": "8. What is the correct file extension of Python?",
            "options": ["A. .java", "B. .cpp", "C. .py", "D. .html"],
            "answer": "C"
        },

        {
            "question": "9. Which keyword defines a function?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },

        {
            "question": "10. Which operator checks equality?",
            "options": ["A. =", "B. ==", "C. !=", "D. >="],
            "answer": "B"
        }

    ]

    score = 0

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")
            print("Correct Answer:", q["answer"])

    total_questions = len(questions)

    percentage = (score / total_questions) * 100

    print("\n" + "=" * 50)
    print("              QUIZ COMPLETED")
    print("=" * 50)

    print("Player Name :", name)
    print("Total Questions :", total_questions)
    print("Correct Answers :", score)
    print("Wrong Answers :", total_questions - score)
    print("Percentage :", percentage, "%")

    if percentage >= 90:
        grade = "Excellent"
    elif percentage >= 75:
        grade = "Very Good"
    elif percentage >= 60:
        grade = "Good"
    elif percentage >= 40:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    print("Grade :", grade)

    print("=" * 50)

while True:

    quiz_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for playing!")
        print("Have a great day!")
        break