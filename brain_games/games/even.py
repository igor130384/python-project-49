import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    num = random.randint(1, 100)

    return even(num)


def even(num):
    result = ""
    if num % 2 == 0:
        result = "yes"
    else:
        result = "no"

    return num, result
