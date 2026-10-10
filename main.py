
print("===== AI TUTOR =====")

name = input("Enter your name: ")
score = 0

print("\nWelcome", name)
print("Choose a subject:")
print("1. Python")
print("2. Mathematics")
print("3. Chemistry")
print("4. English")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    questions = [
        ("Which function displays output?", "print",
         "The print() function displays output."),
        ("Which keyword checks a condition?", "if",
         "The if keyword executes code when a condition is true."),
        ("Which symbol checks equality?", "==",
         "Double equals compares two values.")
    ]

elif choice == "2":
    questions = [
        ("What is 5 + 3?", "8",
         "Addition combines numbers: 5 + 3 = 8."),
        ("What is 10 * 2?", "20",
         "Multiplication: 10 multiplied by 2 is 20."),
        ("What is 12 / 3?", "4",
         "Division: 12 divided by 3 is 4.")
    ]

elif choice == "3":
    questions = [
        ("What is the formula of water?", "h2o",
         "Water contains hydrogen and oxygen: H2O."),
        ("What is the symbol of oxygen?", "o",
         "The chemical symbol for oxygen is O."),
        ("What is the symbol of hydrogen?", "h",
         "The chemical symbol for hydrogen is H.")
    ]

elif choice == "4":
    questions = [
        ("Fill in the blank: I ___ a student.", "am",
         "Use 'am' with 'I'."),
        ("What is the plural of book?", "books",
         "The plural of book is books."),
        ("What is the opposite of hot?", "cold",
         "Cold is the opposite of hot.")
    ]

else:
    questions = []
    print("Invalid choice!")

if questions:
    print("\n===== QUIZ START =====")

    for question, answer, explanation in questions:
        print("\n" + question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answer:
            print("Correct! Well done!")
            score += 1
        else:
            print("Not quite. Correct answer:", answer)
            print("Explanation:", explanation)

    total = len(questions)
    percentage = (score / total) * 100

    print("\n===== YOUR REPORT =====")
    print("Student:", name)
    print("Score:", score, "/", total)
    print("Percentage:", round(percentage, 2), "%")

    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 60:
        print("Good job! Keep practising.")
    else:
        print("Keep learning. Try the quiz again!")

print("\nThank you for using AI Tutor!")
