"""
Create a simple script that calculates a user’s body mass index.  

1. Prompt a user to enter their height (in inches) and their weight (in pounds).  
2. Next, calculate their BMI using the formula: **(weight in pounds x 703) / (height in inches x height in inches)**
3. Output a message including their BMI number and category according to the following table:

> **< 16.0**    Severely Underweight 
**16.0 - 18.4**   Underweight
**18.5 - 24.9**   Normal
**25.0 - 29.9**   Overweight
**30.0 - 34.9**   Moderately Obese
**35.0 - 39.9**   Severely Obese
**> 39.9**   Morbidly Obese
>
"""

# ask the user for their weight in pounds
weight_ask_in_pounds = float(input("Enter your weight in pounds: "))
# ask user for their height in inches
height_ask_in_inches = float(input("Enter your height in inches: "))

# variable to calculate the BMi
# Next, calculate their BMI using the formula: **(weight in pounds x 703) / (height in inches x height in inches)**
bmi = (weight_ask_in_pounds * 703) / (height_ask_in_inches**2)

# round the bmi after 1 decimal place
bmi = round(bmi, 1)

# conditionals for BMi

if bmi == 16.0:
    print(f"Your bmi is {bmi}\nYou are severely underweight")
elif bmi > 16.0 and bmi < 18.5:
    print(f"Your bmi is {bmi}\nYou are underweight")
elif bmi > 18.4 and bmi < 25.0:
    print(f"Your bmi is {bmi}\nYou are normal")
elif bmi > 24.9 and bmi < 30.0:
    print(f"Your bmi is {bmi}\nYou are overweight")
elif bmi > 29.9 and bmi < 35.0:
    print(f"Your bmi is {bmi}\nYou are moderately obese")
elif bmi > 34.9 and bmi < 40.0:
    print(f"Your bmi is {bmi}\nYou are severely obese")
elif bmi > 39.9:
    print(f"Your bmi is {bmi}\nYou are mobidly obese")
else:
    print(f"Your bmi is {bmi}\nYou have an alien 👾👾👾 BMI")
print("*" * 50)
print("Now you know what to do with your life")
