import random
options = ["Rock", "Paper", "Scissors"]

player1 = random.choice(options)
player2 = random.choice(options)

def game():
    player1 = random.choice(options)
    player2 = random.choice(options)
    if (player1 == player2):
        return game()

    elif(player1 == "Rock" and player2 == "Scissors")  or (player1 == "Paper" and player2 == "Rock") or (player1 == "Scissors" and player2 == "Paper"):
        return player1, player2, "Player 1"
    else:
        return player1, player2, "Player 2"
