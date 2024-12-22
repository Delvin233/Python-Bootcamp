# so we want to start from 100 and continually reduce it
# when we get to zero we say no more botlles to pass

bottles = 100
while bottles > 2:
    bottles -= 1
    print(
        f"{bottles} bottles of beer on the wall\n{bottles} bottles of beer\nTake one down, pass it around.\n{bottles - 1} bottles on the wall\n****************"
    )
    if bottles == 2:
        print(
            f"{bottles -1} bottle of beer on the wall.\n{bottles - 1} bottle of beer\nNo more bottles to pass down"
        )

"""for number in range(99, 0, -1):
    print(f"{number} bottles of beer on the wall.\n{number} bottles of beer.")
    if number == 1:
        print("Take one dwon and pass the rest. No more bottles of beer to pass")
    else:
        print(
            f"Take one down and pass the rest.\n{number - 1} bottles of beer on the wall\n****************"
        )
"""
