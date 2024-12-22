# Implement a version of the “classic” matchsticks/toothpicks two player
# game.  We start with 13 toothpicks, and players take turns removing
# 1, 2, or 3 toothpicks at a time.
# The person who removes the last toothpick wins.

# 2 players input their names
player_1 = input("P1, Enter your name ")
player_2 = input("P2, Enter your name ")
print("*" * 10)

# intorduce the toothpics
toothpics = 13
print("| " * toothpics)
print(f"There are {toothpics} toothpics remaining")

# loop for the question
while True:
    # player 1 moves
    p1_move = int(
        input(
            f"{player_1} how many toothpics are you removing? You can only remove up to 3 at a time    "
        )
    )
    # condition to prevent number not in range(1,2,3)
    if p1_move not in range(1, 4):
        print(f"{p1_move} is not valid. 1, 2 or 3 toothpics can be removed\n********")
        continue

    # increase and print
    toothpics -= p1_move
    print("|" * toothpics)
    print(f"There are {toothpics} toothpics remaining\n********")

    # point of break for a win
    if toothpics == 0:
        print(f"{player_1} wins")
        break

    # Player 2 moves
    p2_move = int(
        input(
            f"{player_2} how many toothpics are you removing? You can only remove up to 3 at a time    "
        )
    )
    # condition to prevent number not in range(1,2,3)
    if p2_move not in range(1, 4):
        print(f"{p2_move} is not valid. 1, 2 or 3 toothpics can be removed\n********")
        continue

    # increase and print
    toothpics -= p2_move
    print("|" * toothpics)
    print(f"There are {toothpics} toothpics remaining\n********")

    # point of break for a win
    if toothpics == 0:
        print(f"{player_2} wins")
        break
