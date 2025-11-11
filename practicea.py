import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)   # Random score between 1 and 62

    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()

    if hiscore != "":
        hiscore = int(hiscore)
    else:
        hiscore = 0

    print(f"Your score: {score}")

    # Check if current score is greater than hiscore
    if score > hiscore:
        print("Congratulations! You made a new high score 🎉")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    else:
        print("Better luck next time!")

    return score


# Run the game
game()