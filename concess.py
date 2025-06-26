# Menu of the Stand
menu={"pizza": 3.00,
      "nachos": 4.50,
      "popcorn": 6.00,
      "fries": 2.50,
      "chips": 1.00,
      "pretzel": 3.00,
      "lemonade": 4.25}
# Cart where all items will be added
cart = []
# total of all items in cart
total = 0

# show of menu which will be selected

print("--------MENU------------")

for key , value in menu.items():
    print(f"{key:10} : Rs.{value:.2f}")

print("--------------------------")

# selection of items from menu

while True:
    food = input("select an item from menu (q to quit!): ").lower()
    if food == "q":
        break  
    elif menu.get(food) is not None: #when there is no food item match to menu
        cart.append(food)

# order of food which is selected from cart and total bill

print("-----Your Order-----")
for food in cart:

    total += menu.get(food)

    print(food,end=" ")

print()

print(f"Total is: Rs.{total:.2f}")

print("----------------------")