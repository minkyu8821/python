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

#def square(n) -> int:
    #return n * n
#number = int(input())

#for i in range(number+1):
   # print(square(i))
#temp = list()
#for i in range(number+1):
    #temp.append(i)
#temp = [i for i in range(number+1)]
#print(list(map(lambda i: i * i, temp)))
#print(list(map(square, temp)))


base, exponent = map(int, input("input base & exponent number").split())
print(f"{base}^{exponent} = {base**exponent}")
print(f"{base}^{exponent} = {pow(base, exponent)}")