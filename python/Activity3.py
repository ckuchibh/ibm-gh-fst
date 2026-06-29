player1 = input("Enter your choice(Rock, Paper, Scissors): ")
player2 = input("Enter your choice(Rock, Paper, Scissors): ")

if player1 == player2:
    print("Draw")
elif player1.lower() == "rock" and player2.lower() == "scissors":
    print("Player-1 wins!")
elif player1.lower() == "paper" and player2.lower() == "rock":
    print("Player-1 wins!")
elif player1.lower() == "scissors" and player2.lower() == "paper":
    print("Player-1 wins!")
elif player2.lower() == "rock" and player1.lower() == "scissors":
    print("Player-2 wins!")
elif player2.lower() == "paper" and player1.lower() == "rock":
    print("Player-2 wins!")
elif player2.lower() == "scissors" and player1.lower() == "paper":
    print("Player-2 wins!")
else:
    print("Enter valid option")