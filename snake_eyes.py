import random

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
counter = 1

while roll1 != 1 or roll2 != 1:
    print(roll1, roll2)
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    counter += 1
print(roll1, roll2)
print("SNAKE EYES")
print(counter)
