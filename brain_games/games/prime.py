import random
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    num1 = random.randint(1, 100)
    return num1, prime(num1)


def prime(num):
    if num == 1:
        result = 'no'
    for i in range(2, num):
        if num % i == 0:
            result = 'no'
        result = 'yes'

    return result
