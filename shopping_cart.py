"""
- Prints out a “banner” to welcome users to our shop
- Asks the user for the name of the item they are buying
- Asks the user for the price of that item
- Asks the user for the quantity they are purchasing
- Prints out a message that includes their subtotal (quantity 𝚡 price)
"""

print("****8WELCOME TO MY SIMPLE STORE****")
item_purchasing = input("What are you buying ")
item_pricing = input("How much do you want to bny it for ")
item_quantity = input("How many do you want to buy ")
total = float(item_pricing) * float(item_quantity)
print(
    f"""  
        Added {item_quantity} {item_purchasing} to your shopping cart.
        Your subtotal is {total}. Thanks for coming
    """
)
