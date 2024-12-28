# ============== PART 1 ==============
# Write a function called contains_pickle that accepts any number of arguments.
# The function should return True if it is passed "pickle" as one of the args
# Otherwise it should return False
def contains_pickle(*args):
    if "pickle" in args:
        return True
    else:
        return False


print(contains_pickle("red", 45, "pickle", []))  # --> True
print(contains_pickle(1, 2, "blue"))  # ---------------> False


# ============== PART 2 ==============
# Write a function called count_fails that counts up the number of failing test scores it is passes
# It should accept any number of arguments
# It should return a count of how many args are less than or equal to 50
def count_fails(*args):
    count = 0
    for num in args:
        if num <= 50:
            count += 1
    return count


print(count_fails(99, 48, 79, 36))  # -------> 2
print(count_fails(85, 78, 91))  # ----------> 0
print(count_fails(50, 41, 47, 74, 76, 81))  # -> 3


# ============== PART 3 ==============
# Write a function called get_top_students that helps teachers find their A-grade students!
# It should accept any number of student=score keyword arguments like colt=78 or elton=98
# It should return a list containing the names of students who scored 90 or above
def get_top_students(**kwargs):
    top_students = []
    for name, score in kwargs.items():
        if score > 89:
            top_students.append(name)
    return top_students


print(get_top_students(tim=91, stacy=83, carlos=97, jim=69))  # -> ['tim', 'carlos']
print(get_top_students(colt=61, elton=76))  # -------------------> []
print(get_top_students(kitty=80, blue=95, toad=91))  # -----------> ['blue', 'toad']