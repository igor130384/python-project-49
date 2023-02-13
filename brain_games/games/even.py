import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    num = random.randint(1, 100)

    return is_even(num)


def is_even(num):
    return num % 2 == 0


def even():
    result = ""
    res = is_even()
    if res:
        result = "yes"
    else:
        result = "no"

    return result
