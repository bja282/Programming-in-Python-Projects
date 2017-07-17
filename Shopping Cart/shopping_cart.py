import code
import datetime
import time

#Groceries List
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # Products based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Prompt cashier for product code. Assignment Checkpoints 1-4:
    # Accept a user input value, store it in a variable, and print it. Hint: use the input() function.
    # One at a time, iteratively accept a user input value, store it in a variable, and print it. Hint: use an infinite while loop. Note: you may have to press "control-c" to quit your script.
    # One at a time, iteratively accept a user input value, store it in a variable, and print it. But stop the loop if the user inputs the word "DONE". Hint: use an if statement in conjunction with the break keyword.
    # Repeat the previous step, but instead of printing each user input, store them all in a single list. Then print the list after the user is "DONE".

x = 0
product_ids=[]
while x == 0:
    prompt = input("Please input a product identifier, or 'DONE' if there are no more items:")
    try:
        if prompt.upper() == "DONE":
            break
        elif prompt != "DONE":
            if int(prompt)>20 or int(prompt)<1:
                prompt = input("Sorry, that ID is incorrect. Please try again!")
            else: product_ids.append(int(prompt))

    except ValueError:
        print("Sorry, that input doesn't seem correct. Try again!")

# Receipt Printing
print('''-------------------------------
Ben's Big Leaf Organic
 -------------------------------
Web: www.bensbigleaforganic.com
Phone: 1.212.543.6789
Checkout Time:''', time.strftime("%m/%d/%Y"), time.strftime("%I:%M"),'''
-------------------------------
Shopping Cart Items:\n''')

running_total = 0

for x in product_ids:
    print("+ ", products[x-1]["name"], '(${0:.2f})'.format(products[x-1]["price"], 2))
    running_total += products[x-1]["price"]

print('''
-------------------------------
Subtotal: $''', round(running_total, 2),'''
Plus NYC Sales Tax (8.875%): $''', round(running_total*.08875, 2),
'''\nTotal: $''', round(running_total+(running_total*.08875), 2),'''
-------------------------------
Thanks for your business! Please come again.
'''
)
