def is_prime_number(n) -> bool:
    """
    prime number determination function
    :param n: a positive integer
    :return: If it's a prime number, it returns True, if it's not a prime number, it returns False
    """
    #is_prime_number = True  # Change variable name from count to is_prime_number for readability.
    if k < 2:
        #is_prime_number = False
        return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                #is_prime_number = False  # Remove the plus operation
                #break
                return False
            i = i + 1
        return True
def power(b, e) -> int:
    """
    power function
    :param b: base number
    :param e: exponent number
    :return: power Result value
    """
    result = 1
    for _ in range(e):2
        #result  = result*b
    return result


while True:
    menu = input("1) prime number 2) power 3) divmod 4)quit: ")
    if menu =='1':
        start, end = list(map(int, input("input start & end number").split()))
        for k in range(start, end + 1):
            if is_prime_number(k): print(k, end=' ')
    elif menu =='2':
        base, exponent = map(int, input("input base & exponent number").split())
        print(f"{base}^{exponent} = {pow(base, exponent)}")
    elif menu =='3':
        dividend, divisor = map(int, input("input dividend & divisor number").split())
        print(f"{dividend} // {divisor} = {divmod(dividend, divisor)[0]}")
        print(f"{dividend} % {divisor} = {divmod(dividend, divisor)[1]}")
    elif menu == '4':
        print("exit program:...")
        break
    else:
        print("please choose from the menu.")
