# import random
# numbers = list()
# for _ in range(7):
#    numbers.append(random.randint(1, 6))
# print(numbers)
# rps = ["가위","바위","보"]
# pick = [random.choice(rps) for _ in range(2)]
# print(pick)
# a = [5,7,11]
# b = a
# print(a, b)
# b[1] = 999
# print(a, b)

# import copy
# a = [5, 7, 11] #
# b = a.copy()
# c = list(a)
# d = a[:]
# e = copy.deepcopy(a)
# print(a, b, c, d, e)
# b[1] = 999
# print(a, b, c, d, e)

import copy
a = [5, [-7, 23], 11] #
b = a.copy() #얕은 복사
c = list(a) #얕은 복사
d = a[:] # 얕은 복사
e = copy.deepcopy(a) # 깊은 복사
print(a, b, c, d, e)
b[1][1] = 999
print(a, b, c, d, e)