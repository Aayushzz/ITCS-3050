def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")