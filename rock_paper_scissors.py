from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1, 3)

# Turn that random number into the computer's RPS move
# i kinda skipped this requirement

# Ask a user to enter their move
user_move = input("rock, paper or scissors?").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if user_move == "rock":
    print(rock)
elif user_move == "paper":
    print(paper)
elif user_move == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
if num == 1:
    print(rock)
elif num == 2:
    print(paper)
elif num == 3:
    print(scissors)

# Figure out who wins and print the result!
if user_move == "rock" and num == 2:
    print("paper wins")
elif user_move == "rock" and num == 1:
    print("its a tie")
elif user_move == "rock" and num == 3:
    print("rock wins")
elif user_move == "paper" and num == 2:
    print("Draw")
elif user_move == "paper" and num == 1:
    print("paper wins")
elif user_move == "paper" and num == 3:
    print("scissors wins")
elif user_move == "scissors" and num == 3:
    print("Draw")
elif user_move == "scissors" and num == 1:
    print("rock wins")
elif user_move == "scissors" and num == 2:
    print("scissors wins")
else:
    print("no one wins")
