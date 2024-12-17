# This is just a simple Heads or Tails coin toss
# It would be improved later

from random import randint

coin_toss = randint(0, 1)

if coin_toss == 0:
    print("Heads")
else:
    print("Tails")
