import random
import gameLogic

#Defined moves
possible_moves = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(possible_moves)

# Start game
user_move = input("Rock, Paper or Scissors?")
print(f"Computer chose: {computer_move}")
gameLogic.run(computer_move, user_move)