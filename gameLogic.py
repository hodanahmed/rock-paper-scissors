#Game logic - Conditionals
def run(computer_move,user_move):
  if computer_move == user_move:
    print("Tie!")
  elif user_move == "Rock":
      if computer_move == "Scissors":
          print("Rock smashes scissors! You win!")
      else:
          print("Paper covers rock! You lose.")
  elif user_move == "Paper":
      if computer_move == "Rock":
          print("Paper covers rock! You win!")
      else:
          print("Scissors cuts paper! You lose.")
  elif user_move == "Scissors":
      if computer_move == "Paper":
          print("Scissors cuts paper! You win!")
      else:
          print("Rock smashes scissors! You lose.")