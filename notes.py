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
