# the script should take a date of birth
date_ask = input("which year were you born: ")

# the script should subtract it from the current year
current_age = 2024 - int(date_ask)

# the script should print the result
print("You are ", current_age, "years old")
# you can use an f string as well
print(f"You are {current_age} years old")
