# I might skip some things since they are very basic
# It would be in a note format

# checking the type of data
# print(type(6.88))

# you can use the underscore to separate zeros or any number
# 3_000_000
# Arithmetics: P E M D O S
# ** is for exponents
# even numbers have a remainder of 0
# odd numbers have a remainder of 1
# value += 3; this implies add value to 3 and update the value variable


# varibales; snake case is preferred, though camel case wont spil the code

# strings example:  name = "Delvin"
# strings are indexed : name[0] would output D
# name [-1] would output n
# string slicing; name [0:3] would output Del. index 3 is not inclusive

# None denoted a lack of a value: user = None
# type(None) would output NoneType  :)

# escape characters: \n for new line
# print("\\") two backslashes to print \

# tripple quoting:  ''' hello ''' or """Hello"""
# its normally used for multi line printing
# address = ''' name: Delvin Street
#               location: Ghana
# '''

# fucntions are reusable or repeatable actions that have a name
# in-built functions: len(), help(), input(), type(),
# we can also decide to do type casting: int(), str(), floot()

# f strings
# f" there are {25+22+28} days remaining

# string methods: basically functions that live on objects
# name.capitalize(), name.upper(),
# name.strip() defaults to removing white spaces, yet you can decide
# new_name = "....Delvin.."
# what it shoud strip with ["chars"]
# for example: new_name.strip["."] would remove the .
# theres lstrip() and rstrip() as weell
#

# you can also chain methods: new_name.strip(".").upper()

# in, not , is
# help(ord)

# conditionals: if ,if...else, if...elif, if ....elif.... else
# the conditionals can be nested

# logical "and" , "or" . "not"
# the order of presedence is not > and > or
# name.isnumeric() is a method to check if a variable is numeric

# loops: whille, for
# Do your best to avaid infintie loops
# remeber to indent appropiately
# break and continue keywords can be used to manipulate the loops
# while True: ..... break ; this would end the code at the condition
# while False:...... false : this would skip the condition
# rnage(start, stop, step). The stop is not inclusssive

# Nested loops is basically a loop in another loop
"""for outer in range(1, 5):
    print(outer)
    for inner in range(1, 3):
        print("\t", inner)"""
# usually just two is okay . Dont overdo it
"""for char in "CAT":
    for x in range(3):
        print(char)"""


# fucntions are normally used to preveent code repitition
# they are also used to break down large chunks of code
# we define and then execute functions
# the return keyword is used to end the execution of a function
"""def is_even(num):
    if num % 2 == 0:
        return "EVEN"
    return "Not even"


print(is_even(14))"""

"""def slugify(sentence):
    return sentence.strip().replace(" ", "-").lower()


print(slugify("    Local Men Have a whole lot to cook  "))"""


"""def vowel_count(sentence):
    counter = 0
    for letter in sentence:
        if letter in "aeiou":
            counter += 1
    return counter


print(vowel_count("Now we test the code 113"))"""


# we can also set a default parameter
"""def hello(number=5):
    return "hello " * number


print(hello())"""
# when using the default approach, you can skip the first and fill out the second
# order is important. Default comes at the end


# you can also use keyword arguments to make calling easier
# the order matters. It follows the rule on line 118 and 119
"""def names(fist, second, third="Lamar"):
    print(f"Hello Mr. {fist} {second} {third}")


names(fist="James", third="Water", second="Boat")"""

# Scoping
"""
L       E         G         B
lexical Enclosing Global Built-In
"""
# It follows the order
"""
    L > E > G > B
"""
# "global" keyword cam be used to make a variable global
"""score = 100


def double_score():
    global score
    score *= 2


double_score()
print(score)
"""

# lists are orderred collection of values
# rndoms  = [99, "Macis", 233, True]
# the values in the lists can be updated at a particular index or
# with the append  keyword
# extend is another keyword
# insert is another keyword

"""randoms = [99, "Macis", 233, True]
randoms.append(False)

randoms[1] = "Light"

randoms.extend("Men")

randoms.insert(0, "Dark")  # this would take the spot of index 9

print(randoms)"""
# list slicing : list[start: end: step]
"""nums = [2, 3, 4, 5]
nums[1:3] = ["a", "b", "c"]
print(nums)"""

# looping through lists
"""emails = ["man@man.com", "boys@boys.com", "women@women.com", "oldies@oldies.com"]
for email in emails:
    print(f"Sending new mails to {email}")
"""
# You can nest a list. Normally called 2D List
"""example = [["me", 22], ["you", 12], ["they", 34]]
print(example[1])
print(example[1][1])"""

# concatonating lists
# multiplying lists
# list methods : count, revere, sort, split, join
"""even = [2, 4, 6, 2, 4]

odd = [1, 3, 5]

new = even + odd
multiply_List = even * 2
counter = even.count(2)
reverser = even.reverse()
sortedList = even.sort()  # default is in ascending order
reverseSort = even.sort(reverse=True)
print(new)
print(multiply_List)
print(counter)
print(sortedList)
print(reverseSort)"""

# For list mutablility, don't get lost
# lemme use this example
# num1 = [1,2,3]
# num1 = num2
# if i append a value to num2, it'd also affect num1
# for instance: num2.append(4)
# this is so because there are assigned the same id

# comparing lists
# we can use == and is
# the difference is that == compared the contecnt of the lists
# the order is even checked
# is, checks to see if they have the same id in memory

"""date = "03/04/1999"

splitted = date.split("/")
joined = "".join(date)  # outputs the string form of the list
print(splitted)
print(joined)"""

# list unpacking
"""angles = [0, 180, 360, 334, 323, 22233]
zero, hundred, threeSixty, *nonse = angles
print(zero)
print(nonse)"""  # the asterisk used above would take the remainng values of the lists
# that have not been assigned

# making a shallow copy
# this means that it wont have the same id and that it wont copy
# any nested lists
"""angles_Copy = angles.copy()
angles_Copy2 = angles[:]

print(angles_Copy)
print(angles_Copy2)
"""

# Dictionaries
# to group related unordered data. In situations where lists dont help
# it uses key-value pairs
"""book = {"title": "Vagabond", "Ratings": 5, "Lore": "Very Acurate"}

book["title"] = "Berserk"
book["Source"] = "Nihon"
jjk = book.get("Juustsu")
no_title = book.pop("title")
popped = book.popitem() """  # this would return the key and value of the
# book.clear()
"""del book["Lore"]

print(book)
# print(book["title"])
print(jjk)
print(no_title)
print(popped)"""

# Dictionaries are mutable: so recall from lists num1 = num2
# they would have the same id. so updating num2 affects num1
# uses the == and is . Same as lists

"""numbers = {1: "one", 2: "two", 3: "three"}

all_keys = numbers.keys()
all_values = numbers.values()
all_items = numbers.items()

updated_num = {4: "four", 5: "five"}
more_updated_nums = {"music": ["Tems", "Ayra Star"]}
new = {**numbers, **updated_num}
piped_new = (
    numbers | updated_num | more_updated_nums
)"""  # the right side wins in case of a duplicatd key

"""numbers.update(updated_num)

print(all_keys)
print(all_values)
print(all_items)
print(new)
print(piped_new)"""
# dictionary  unpacking
"""for key, value in all_items:
    print(f"key is {key}. Value is {value}")"""

# we can nest lists and call what we want with [key][nmsted-key]

# Tuples
# they are immutable : we cant change the elements
# they are ordered like lists
# they have indexes
"""names = ("me", "you", "we", "we")
"""

# use a trailing comma for a single tuple
# leaving the comma makes Python assume we want an expression
"""manga = ("Wild Strawberry",)
"""
# tuple index and count
"""print(names.count("we"))
print(names.index("you"))"""
# Tuples can be used as keys in dictionaries

# SEts
# they are immutable
# using == and is behaves like lists or dictioanries or even tuples
"""set_of_numbers = {1, 2, 3, 4, 5}
odds = {2.3, 3.3, 3.33, 2, 5}

empty_set = set()
single_set = {1}
# using just {} makes it a dictionary

adding_another_vale = set_of_numbers.add(10)
removing_a_value = set_of_numbers.remove(2)
discard_a_set = set_of_numbers.discard(44)  # wont throw a key error

intersectio = set_of_numbers & odds
union = set_of_numbers | odds
difference = set_of_numbers - odds """  # order is important here
# it  returns values in the left side
# which are not in the right side

"""print(set_of_numbers)
print(intersectio)
print(union)
print(difference)"""

# RETURN TO FUNCTIONS
# in cases where do not know how many arguments we want to take
# we use the *args  wildcard
#  you can use any name after the *


"""def average(word, *args):
    total = 0
    for arg in args:
        total += arg
    print(word)
    return total / len(args)"""


# *arg unpacking
"""print(average("Anyhow", *[1, 2, 3, 1, 2]))"""


# the *args would collect the remaining  arguments and store them in a tuple
"""print(average("Anyhow", 1, 2, 3, 1, 2))

"""
# **kwargs
# we use the ** to write a function that accepts any number of
# keyword arguments into key-value pairs


"""def demo(**kwargs):
    print(kwargs)


print(demo(name=45, color="red"))"""
# they are stored in a dictionary argument

# HANDLING ERRORS
"""try:
    num = int(input("a number "))
except:  # (ValueError, EOFError):
    print("id pick for you")
    num = 0"""
"""except EOFError:
    print("You didnt enter anything")"""  # this would give an error since we didnt specify any error above

"""print(f"{num} was chosen")"""

# ANTICIPATING ERRORS
# LOOK BEFORE YOU LEAP
"""THE LOGIC HERE IS: IF I CAN DO THIS, THEN ID DO THIS"""
# EASIER TO ASK FOR FORGIVENESS THAN PERMISSION
"""THE LOGIC HERE IS: YOU ASSUME SOMETHING TO WORK IF IT DOESNT THEN WE DO THIS"""
# The above uses a lot of try and accept and "more pythony"
