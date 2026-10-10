
print("Welcome to AI Tutor!")

name = input("Enter your name: ")

print("Hello,", name)
print("I am your personal learning assistant.")

print("\nWhat do you want to learn?")
print("1. Python")
print("2. Mathematics")
print("3. Chemistry")
print("4. English")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Let's learn Python!")
elif choice == "2":
    print("Let's learn Mathematics!")
elif choice == "3":
    print("Let's learn Chemistry!")
elif choice == "4":
    print("Let's learn English!")
else:
    print("Invalid choice. Please select 1 to 4.")

print("Happy Learning!")
