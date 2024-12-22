"""Create a script that rolls dice for a user.  When the script runs, 
it should ask a user how many dice they want to roll and how many sides 
each die will have.  
Then it randomly rolls those dice and prints the result.  
Every time a user hits Enter, the dice are rolled again.  
If a user every enter “q”, then the script quits and stops running!

**Hints:**

- use `randint()` to generate the dice rolls. Remember, you need to import it from `random`
- start by rolling a single die before rolling multiple
- you’ll need to use nested loops!"""

from random import randint

dice_amount = int(input("How many  dice do you want to roll "))
dice_sides = int(input("How many sides of the dice do you want "))


while True:
    result = "|"
    for die in range(dice_sides):
        randoms = randint(1, dice_sides)
        result += f"{randoms} |"
    print(result)

    re_ask = input("We go again? Type q to end ")
    if re_ask == "q":
        break
