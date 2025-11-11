import random

print("🐍💧🔫 Snake, Water, Gun Game 🐍💧🔫")
print("Enter 's' for Snake, 'w' for Water, 'g' for Gun")

player = input("Your choice: ").lower()
computer = random.choice(['s', 'w', 'g'])

print(f"Computer chose: {computer}")

if player == computer:
    print("It's a Draw!")
elif player == 's' and computer == 'w':
    print("🎉 You Win! (Snake drinks Water)")
elif player == 's' and computer == 'g':
    print("😢 You Lose! (Gun kills Snake)")
elif player == 'w' and computer == 'g':
    print("🎉 You Win! (Water damages Gun)")
elif player == 'w' and computer == 's':
    print("😢 You Lose! (Snake drinks Water)")
elif player == 'g' and computer == 's':
    print("🎉 You Win! (Gun kills Snake)")
elif player == 'g' and computer == 'w':
    print("😢 You Lose! (Water damages Gun)")
else:
    print("Invalid input! Please choose 's', 'w', or 'g'.")
