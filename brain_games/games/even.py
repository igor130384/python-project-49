import random


def brain_even():
    num = random.randint(1, 100)
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = f'Question: {num}'

    def is_even(num):
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        print('Question:', num)
        return result
