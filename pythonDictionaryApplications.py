#Task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({"Beverages": {"Iced Tea": 2.99, "Pineapple Mango Lemonade": 3.99}})
steak = restaurant_menu.get("Main Course").get("Steak")
print(steak)
if steak != None:
    print("steak!")
    restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)
starters = restaurant_menu.get("Starters")
if starters != None:
    starters.pop("Bruschetta")
    restaurant_menu.update(starters)
    print(restaurant_menu)

