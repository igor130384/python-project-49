import random


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = random.randint(1, 100)

    print(f'Question: {num}')

    def is_even(num):
        if num % 2 == 0:
            return 'yes'
        else:
            return 'no'
    result = is_even(num)
    return result
