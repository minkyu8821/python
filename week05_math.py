def print_fx(fx):
    texts = "f(x) = "
    expo = len(fx) - 1

    for i in range(len(fx)):
        coef = fx[i]
        if coef > 0 and i != 0:
            texts = texts + "+"
        if coef ==0:
            expo = expo - 1
            continue
        texts = texts + f"{coef}x^{expo} "

        expo = expo - 1
    return texts

coefficient = [5,-2,0,6]

print(print_fx(coefficient))


x = int(input("input x value:"))
def cal_fx(fx, x):
    expo = len(fx) - 1
    result = 0

    for k in range(len(fx)):
        coef = fx[k]
        result = result + coef * x ** expo
        expo = expo - 1

    return result

print(cal_fx(coefficient,x))
