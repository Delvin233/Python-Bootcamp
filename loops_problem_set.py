#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
"""for char in word:
    print(char)
print("*" * 50)"""

# Write a while loop that does the same thing!
"""i = 0
while i < len(word):
    print(word[i])
    i += 1
print("*" * 50)"""


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
"""i = 100
while i < 141:
    print(i)
    i += 2"""

# Write a for loop that does the same thing (with range())
"""for number in range(100, 141, 2):
    print(number)"""
#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
sillygoose_annoyance = input("Repeat after me:\n         sillygoose          ")
while sillygoose_annoyance != "sillygoose":
    sillygoose_annoyance = input("Repeat after me:\n         sillygoose          ")
if sillygoose_annoyance == "sillygoose":
    print("Now we can vibe")
