try:
    num = int(input("a number "))
except:  # (ValueError, EOFError):
    print("id pick for you then ")
    num = 0
"""except EOFError:
    print("You didnt enter anything")"""
# this would give an error since we didnt specify any error above

print(f"{num} was chosen")
