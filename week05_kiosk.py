# ISHS CAFE
# Americano 1500, Latte 2500

beverage = ["americano", "latte"]
prices = [1500, 2500]

while True:
    menu = int(input("1) Americano 2) Latte 3) End order : " ))
    if menu == 3:
        print("Exit program")
        break
    elif menu == 1:
        print("You ordered Americano Coffee. The price is 1500 won.")
    elif menu == 2:
        print("You ordered a Cafe Latte. The price is 2500 won.")


