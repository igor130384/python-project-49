import random


def brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = random.randint(1, 100)
    question = f'Question: {num}'

    def is_even(num):
        if num % 2 == 0:
            return 'yes'
        else:
            return 'no'
    result = is_even(num)
    return result, task, question
