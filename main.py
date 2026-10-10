
print("===== AI TUTOR =====")

name = input("Enter your name: ")
print("\nWelcome", name, "!")

subjects = {
    "1": ("Python", [
        ("Which function displays output?",
         ["A. input", "B. print", "C. scan", "D. show"],
         "B", "The print() function displays output."),
        ("Which keyword checks a condition?",
         ["A. for", "B. def", "C. if", "D. import"],
         "C", "The if keyword executes code based on a condition."),
        ("What is the output of 2 + 3?",
         ["A. 23", "B. 6", "C. 5", "D. 1"],
         "C", "The + operator adds numbers: 2 + 3 = 5.")
    ]),
    "2": ("Mathematics", [
        ("What is 5 squared?",
         ["A. 10", "B. 15", "C. 20", "D. 25"],
         "D", "5 squared means 5 x 5 = 25."),
        ("What is 10 / 2?",
         ["A. 2", "B. 5", "C. 8", "D. 10"],
         "B", "10 divided by 2 equals 5."),
        ("What is the sum of 7 and 8?",
         ["A. 14", "B. 16", "C. 15", "D. 13"],
         "C", "7 + 8 = 15.")
    ]),
    "3": ("Chemistry", [
        ("What is the symbol for oxygen?",
         ["A. Ox", "B. O", "C. Oy", "D. Om"],
         "B", "O is the chemical symbol for oxygen."),
        ("What is the charge of an electron?",
         ["A. Positive", "B. Neutral",
          "C. Negative", "D. Zero"],
         "C", "An electron has a negative electric charge."),
        ("What is the chemical formula of water?",
         ["A. CO2", "B. O2", "C. H2O", "D. NaCl"],
         "C", "Water contains hydrogen and oxygen: H2O.")
    ]),
    "4": ("English", [
        ("What is the plural of child?",
         ["A. Childs", "B. Children", "C. Childes", "D. Child"],
         "B", "The plural form of child is children."),
        ("Choose the correct spelling.",
         ["A. Beautifull", "B. Beutiful",
          "C. Beautiful", "D. Beautifal"],
         "C", "Beautiful is the correct spelling."),
        ("What is the opposite of hot?",
         ["A. Warm", "B. Cold", "C. Heat", "D. Fire"],
         "B", "Cold is the opposite of hot.")
    ])
}

print("\nChoose a subject:")
for key, value in subjects.items():
    print(key + ".", value[0])

choice = input("Enter your choice (1-4): ").strip()

if choice not in subjects:
    print("Invalid choice. Please run the program again.")

else:
    subject, questions = subjects[choice]
    score = 0
    total = len(questions)

    print("\nSubject:", subject)
    print("Enter A, B, C, or D.\n")

    for number, question in enumerate(questions, start=1):
        text, options, correct, explanation = question

        print(f"Q{number}. {text}")
        for option in options:
            print(option)

        answer = input("Your answer: ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Enter A, B, C, or D.")
            answer = input("Your answer: ").strip().upper()

        if answer == correct:
            print("Correct answer! Well done.\n")
            score += 1
        else:
            print("Wrong answer.")
            print("Correct answer:", correct)
            print("Explanation:", explanation, "\n")

    percentage = (score / total) * 100

    print("\n===== PERFORMANCE REPORT =====")
    print("Student:", name)
    print("Subject:", subject)
    print("Correct answers:", score, "/", total)
    print(f"Score percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Feedback: Excellent! All answers are correct!")
    elif percentage >= 70:
        print("Feedback: Great work! Keep practising.")
    elif percentage >= 40:
        print("Feedback: Good effort. Revise the difficult topics.")
    else:
        print("Feedback: Keep learning and try the quiz again.")

    print("\nThank you for using AI-Tutor!")
