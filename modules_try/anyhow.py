color = ["red", "yellow", "green"]


def average(*args):
    total = 0
    for numbers in args:
        total += numbers
    return total / len(args)
