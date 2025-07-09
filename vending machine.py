# Displaying the title
print("Aslam's Vending Machine !")

# Define the updated items in the vending machine
A1 = {"Item": "Water", "Price": "1.00", "Stock": "20"}
A2 = {"Item": "Lemonade", "Price": "2.00", "Stock": "15"}

B1 = {"Item": "Chips", "Price": "1.50", "Stock": "18"}
B2 = {"Item": "Nachos", "Price": "2.50", "Stock": "12"}

C1 = {"Item": "Candy Bar", "Price": "1.80", "Stock": "25"}
C2 = {"Item": "Gummy Bears", "Price": "1.50", "Stock": "22"}

D1 = {"Item": "Soda", "Price": "2.00", "Stock": "10"}
D2 = {"Item": "Iced Tea", "Price": "2.50", "Stock": "8"}

E1 = {"Item": "Juice Box", "Price": "1.30", "Stock": "14"}
E2 = {"Item": "Milkshake", "Price": "3.00", "Stock": "5"}

F1 = {"Item": "Cookies", "Price": "1.20", "Stock": "30"}
F2 = {"Item": "Brownie", "Price": "2.00", "Stock": "7"}

items = [A1, A2, B1, B2, C1, C2, D1, D2, E1, E2, F1, F2]

# Manually creating the table-like structure
print("Items Available for Purchase:")
print("+------------------------+--------+--------+")
print("| Item                   | Price  | Stock  |")
print("+------------------------+--------+--------+")

for item in items:
    print(f"| {item['Item']:<22} | {item['Price']:<6} | {item['Stock']:<6} |")

print("+------------------------+--------+--------+")

ITEMS = input("Enter the name of the item you want to buy: ")
item_code = None

for i in items:
    if ITEMS.lower() == i['Item'].lower():
        item_code = i
        break

if item_code is None:
    print("INVALID ITEM")
else:
    print(f"Awesome, {item_code['Item']} will cost you {item_code['Price']} $")

    price = float(input(f"Enter {item_code['Price']} dollars to purchase: "))
    
    if price > float(item_code['Price']):
        change = price - float(item_code['Price'])
        print(f"Thank you for your purchase. Here is your {item_code['Item']}.")
        print(f"Your change is: {change} $")
    elif price == float(item_code['Price']):
        print(f"Thank you for your purchase. Here is your {item_code['Item']}.")
    else:
        print(f"Please enter at least {item_code['Price']} $.")
