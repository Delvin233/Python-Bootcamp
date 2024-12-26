"""
Create an interactive, text-based todo list that has the following features:

- A user can add todos by entering them into the prompt
- A user can complete todos by entering the todo’s corresponding number
- A user can view a help screen by typing ‘h’ or ‘help’
- A user can quit by typing ‘q’ or ‘quit
"""

print(
    """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
"""
)
print("*" * 20)


# we want to loop the asking, so we can ask over and over
# we set q to end the loop
# we set h for help
print("Quick Note:")
print("Use q to quit and get summary")
print("Use h to ask for help")
print("*" * 20)


"""# if we want to take the functions approach
def to_do_list(task):
    task = input("What do you want to do today ")
    adding_list = big_list.append(task)
    return big_list"""


to_do = []
finished_task = []

while True:
    # we want to append before asking so that it doesn't occur after
    for index in range(len(to_do)):
        print(f"{index + 1}) {to_do[index]}")

    print("What task do you want to complete")
    task = input("> ")

    # q to quit and the output of the tasks we completed
    if task == "q":
        print("*" * 20)
        print("Done!!!!")
        break

    # help side
    elif task == "h":
        print("*" * 20)
        print("Type q to quit")
        print("type the number for the task you have completed")
        print("type  any task you want to complete")
        print("*" * 20)

    # making numeric inputs remove the task based on the index
    elif task.isnumeric():
        index = int(task)
        if index >= len(to_do):
            print("invalid")
        else:
            completed = to_do.pop(index - 1)
            finished_task.append(completed)

    else:
        to_do.append(task)
print(f"You completed {len(finished_task)} tasks: ")
for finsih in finished_task:
    print(f"* {finsih}")
