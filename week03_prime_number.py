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


start, end = list(map(int, input("input start & end number").split()))
#print(int(test[0]),int(test[1]))


for k in range(start, end+1):
         if is_prime_number(k): print(k, end=' ')



