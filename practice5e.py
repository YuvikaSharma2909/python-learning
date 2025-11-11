# 🧮 Program to display grade using match-case

marks = int(input("🎓 Enter your marks (0-100): "))

# 🎯 Using match-case (Python 3.10+)
match marks:
    case m if 90 <= m <= 100:
        print("🌟 Excellent! Keep it up! 💯")
    case m if 80 <= m < 90:
        print("🥳 Very Good! You did great!")
    case m if 70 <= m < 80:
        print("👍 Good! Keep improving!")
    case m if 60 <= m < 70:
        print("🙂 Fair! You can do better!")
    case m if 33 <= m < 60:
        print("😐 Passed, but need more effort!")
    case m if 0 <= m < 33:
        print("❌ Failed! Work harder next time!")
    case _:
        print("⚠️ Invalid Marks! Please enter between 0 and 100.")

