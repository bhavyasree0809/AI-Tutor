
print("Welcome to AI Tutor!")

name = input("Enter your name: ")
print(f"\nHello, {name}! Let's learn something new.")

print("\nChoose a subject:")
print("1. Python")
print("2. Mathematics")
print("3. Chemistry")
print("4. English")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("\n--- Python Lesson 1 ---")
    print("Python is a programming language.")
    print("Example: print('Hello World')")
    print("Quiz: Which function displays output?")
    print("Answer: print()")

elif choice == "2":
    print("\n--- Mathematics Lesson 1 ---")
    print("Addition means combining numbers.")
    print("Example: 5 + 3 =", 5 + 3)
    print("Quiz: What is 10 + 5?")
    print("Answer: 15")

elif choice == "3":
    print("\n--- Chemistry Lesson 1 ---")
    print("An atom is a basic unit of an element.")
    print("Water has the chemical formula H2O.")
    print("Quiz: What is the formula of water?")
    print("Answer: H2O")

elif choice == "4":
    print("\n--- English Lesson 1 ---")
    print("Learn a simple sentence:")
    print("I am learning English.")
    print("Quiz: Fill in the blank: I ___ a student.")
    print("Answer: am")

else:
    print("Invalid choice. Please select 1 to 4.")

print("\nThank you for learning with AI Tutor!")
