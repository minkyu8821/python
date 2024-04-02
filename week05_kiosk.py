# ISHS CAFE
# Americano 1500, Latte 2500

beverage = ["americano", "latte", "Iced tea"]
prices = [1500, 2500, 2300]
total_price = 0
quantity = [0, 0, 0]

menu_lists = ''
for m in range(len(beverage)):
    menu_lists = menu_lists + f"{m+1}) {beverage[m]} {prices[m]}won   "
menu_lists = menu_lists + f"{len(beverage)+1}) End order : "


while True:
    menu = input(menu_lists)
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        print("You ordered americano coffee. The price is 1500 won.")
        total_price = total_price + prices[0]
        quantity[0] = quantity[0] + 1
    elif menu == '2':
        print("You ordered a cafe latte. The price is 2500 won.")
        total_price = total_price + prices[1]
        quantity[1] = quantity[1] + 1
    elif menu == '3':
        print("You ordered a iced tea. The price is 2500 won.")
        total_price = total_price + prices[2]
        quantity[2] = quantity[2] + 1
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")
for i in range(len(beverage)):
    if quantity[i] !=0:
        print(f"{beverage[i]}\n\t{prices[i]}\tx{quantity[i]}\t{prices[i] * quantity[i]}")

print(f"The total amount is {total_price} won.")