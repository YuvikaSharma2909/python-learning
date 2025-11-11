# 🎯 Program to check whether a student has PASSED or FAILED

# 📝 Taking marks of 3 subjects from the user
sub1 = float(input("📘 Enter marks of Subject 1: "))
sub2 = float(input("📗 Enter marks of Subject 2: "))
sub3 = float(input("📙 Enter marks of Subject 3: "))

# 🧮 Calculating total and percentage (assuming each subject is out of 100)
total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100

# 🧠 Checking pass/fail conditions
if (sub1 >= 33 and sub2 >= 33 and sub3 >= 33) and (percentage >= 40):
    print("🎉 Congratulations! You have PASSED! 🥳")
    print(f"📊 Your total percentage is {percentage:.2f}% ✅")
else:
    print("😞 Sorry! You have FAILED. 💔")
    print(f"📊 Your total percentage is {percentage:.2f}% ❌")
