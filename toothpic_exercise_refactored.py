# 2 players input their names
player_1 = input("P1, Enter your name: ")
player_2 = input("P2, Enter your name: ")
print("*" * 10)

# intorduce the toothpics
toothpics = 13
print(f"There are {toothpics} toothpics remaining")
print("| " * toothpics)

# set a variable for the current player
current_player = player_1

# loop for the question
while True:
    # moves
    move = int(
        input(
            f"{current_player} how many toothpics are you removing? You can only remove up to 3 at a time    "
        )
    )
    # condition to prevent number not in range(1,2,3)
    if move not in range(1, 4):
        print(f"{move} is not valid. 1, 2 or 3 toothpics can be removed\n")
        continue

    # increase and print
    toothpics -= move
    print("|" * toothpics)
    print(f"There are {toothpics} toothpics remaining\n")

    # point of break for a win
    if toothpics == 0:
        print(f"{current_player} wins")
        break

    # PLAYER SWITCH
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1

    """
    Dont end up comparing (==) on the second line of the player switch 
    instead assign (=)
    also assign on the else since the current player has changed
    """
print("GMAE OVER")
