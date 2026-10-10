
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
        ("Which function displays output in Python?", "print"),
        ("Which keyword checks a condition?", "if"),
        ("Which symbol is used for equality comparison?", "==")
    ]

elif choice == "2":
    questions = [
        ("What is 5 + 3?", "8"),
        ("What is 10 * 2?", "20"),
        ("What is 12 / 3?", "4")
    ]

elif choice == "3":
    questions = [
        ("What is the chemical formula of water?", "h2o"),
        ("What is the symbol of oxygen?", "o"),
        ("What is the symbol of hydrogen?", "h")
    ]

elif choice == "4":
    questions = [
        ("Fill in the blank: I ___ a student.", "am"),
        ("What is the plural of book?", "books"),
        ("What is the opposite of hot?", "cold")
    ]

else:
    questions = []
    print("Invalid choice!")

if questions:
    print("\n===== QUIZ START =====")

    for question, answer in questions:
        print("\n", question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answer:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer:", answer)

    print("\n===== QUIZ RESULT =====")
    print("Student:", name)
    print("Your score:", score, "/", len(questions))

    if score == len(questions):
        print("Excellent work!")
    elif score >= 2:
        print("Good job! Keep practising.")
    else:
        print("Keep learning. You can improve!")

print("\nThank you for using AI Tutor!")
