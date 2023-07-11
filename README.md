# Rock Paper Scissors Python Game
### User story
As a player I want to do the following:
I want to enter my name before playing the game
I want the game to say goodbye to me when it finishes
I want to play more than one game

## How to run
Write `python main.py` in terminal

## Tasks
### Task 1 - Variables
##### Concepts to cover
What is a variable?
How to assign a variable?
input() function
Resources:
[What is a variable?](https://www.twinkl.co.uk/teaching-wiki/variable-in-programming)
[Python variables cheatsheet](https://www.tutorialspoint.com/python/python_variables.htm)
[input() function documentation](https://www.w3schools.com/python/ref_func_input.asp)
##### Task
Before the game starts (on line 8):
Create a variable called username
Assign the variable `username` to your own name
Challenge: Assign the variable `username` to user input.
You can do this by following [input() function documentation](https://www.w3schools.com/python/ref_func_input.asp)
##### Answer
```
username = input("Enter username:")
print(username)
```
### Task 2 - Data types
##### Concepts to cover
What are data types?
Different types of data types
Mixing different data types (String Interpolation)
Resources:
[What are data types?](https://teachcomputerscience.com/programming-data-types/)
[Python data types](https://www.slingacademy.com/article/python-data-types-cheat-sheet/)
[Python String Interpolation: 4 Ways to Do It (with code)](https://favtutor.com/blogs/string-interpolation-python)
##### Task
After gameLogic.run function, do the following:
Print the message `GAME OVER` once the game finishes.
Challenge: Print the message `See you later <USERNAME>` once the game finishes.
You will need to mix different data types. This can be done by string interpolation. Follow the resource [Python String Interpolation: 4 Ways to Do It (with code)](https://favtutor.com/blogs/string-interpolation-python) to complete.
##### Answer
```
print("GAME OVER!")
print(f"See you later {username}") - String Interpolation (Using multiple data types)
```
### Task 3 - Iteration
##### Concepts to cover
What are iterations?
Different ways to iterate in Python
for loops
range()
Resources:
[What are iterations?](https://teachcomputerscience.com/iterations/)
[Different iterations in Python](https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-loops/cheatsheet)
[For loops](https://www.w3schools.com/python/python_for_loops.asp)
[range() function](https://www.w3schools.com/python/ref_func_range.asp)
##### Task
The game should run 3 times before ending
Put the following lines of code in a `for` loop
    ```
    computer_move = random.choice(possible_moves)
    user_move = input("Rock, Paper or Scissors?")
    print(f"Computer chose: {computer_move}")
    gameLogic.run(computer_move, user_move)
    ```
Use range() function state how many games to play
Example:
       ```
        for i in range(3):
          ////
        ```
##### Answer
```
for i in range(3):
  computer_move = random.choice(possible_moves)
  user_move = input("Rock, Paper or Scissors?")
  print(f"Computer chose: {computer_move}")
  gameLogic.run(computer_move, user_move)
```