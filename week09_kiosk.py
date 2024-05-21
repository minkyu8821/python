# ISHS CAFE
# Americano 1500, Latte 2500
def select_menu(key):
    """
    display menu, calculate eoeal price and count quantity
    :param key: key of dictionary
    :return:
    """
    global total_price
    print(f"You ordered {key}. The price is {beverage_price_quantity.get(key)[0]} won.")
    total_price = total_price + beverage_price_quantity.get(key)[0]
    beverage_price_quantity.get(key)[1] = beverage_price_quantity[key][1] + 1


beverage_price_quantity = {"americano coffee": [1500,0],
                  "caffe latte": [2500,0],
                  "iced tea": [2300,0]
                  }
total_price = 0

menu_lists = ''
i = 1
for k, v in beverage_price_quantity.items():
    menu_lists = menu_lists + f"{i}) {k} {v[0]}won  "
    i += 1
menu_lists = menu_lists + f"{i}) End order : "


while True:
    menu = input(menu_lists)
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        select_menu("americano coffee")
    elif menu == '2':
        select_menu("caffe latte")
    elif menu == '3':
        select_menu("iced tea")
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")
for k, v in beverage_price_quantity.items():
    if v[1] !=0:
        print(f"{k}\n\t{v[0]}\tx{v[1]}\t{v[0] * v[1]}")

print(f"The total amount is {total_price} won.")


