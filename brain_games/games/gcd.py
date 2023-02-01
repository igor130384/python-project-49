import random


def brain_gcd():
    print('Find the greatest common divisor of given numbers.')
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Question: {num1} {num2}')

    def gcd2(a, b):
        if b == 0:
            return a
        else:
            return gcd2(b, a % b)
    result = gcd2(num1, num2)
    return result
