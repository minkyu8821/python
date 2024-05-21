import random

numbers = list()
for _ in range(7):
    numbers.append(random.randint(1, 6))

print(numbers)

rps = ["가위","바위","보"]
pick = [random.choice(rps) for _ in range(2)]
print(pick)
