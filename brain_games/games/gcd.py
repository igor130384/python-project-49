import random


def brain_gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'Question: {num1} {num2}'
    task = 'Find the greatest common divisor of given numbers.'

    def gcd2(a, b):
        if b == 0:
            return a
        else:
            return gcd2(b, a % b)
    result = gcd2(num1, num2)
    return result, task, question
