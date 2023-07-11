import random
import gameLogic

#Defined moves
possible_moves = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(possible_moves)

# Start game
username = input("Enter username:")
for i in range(3):
  computer_move = random.choice(possible_moves)
  user_move = input("Rock, Paper or Scissors?")
  print(f"Computer chose: {computer_move}")
  gameLogic.run(computer_move, user_move)
print("GAME OVER!")
print(f"See you later {username}")