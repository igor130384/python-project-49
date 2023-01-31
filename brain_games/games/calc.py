import prompt

import random


def brain_calc():
    operand = ['+', '-', '*']
    oper = random.choice(operand)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'Question: {num1} {oper} {num2}'
    answer = prompt.string('Your answer: ')
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    else:
        result = num1 * num2
        return result, answer, question
