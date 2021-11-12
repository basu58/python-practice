# factorials
num = int(input())


# solution1
def fact(num):
    return 1 if (num == 1 or num == 0 or num < 0) else num * fact(num - 1)


print(fact(num))


# solution2
def fact1(num):
    number = 1
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        while num > 1:
            number *= num
            num -= 1
    return number


print(fact1(num))

# solution3
import math


def fact3(num):
    return math.factorial(num)


print(fact(num))
