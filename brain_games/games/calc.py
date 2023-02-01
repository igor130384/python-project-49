

import random


def brain_calc():
    print('What is the result of the expression?')
    operand = ['+', '-', '*']
    oper = random.choice(operand)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Question: {num1} {oper} {num2}')

    def is_calc(oper, num1, num2):
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        else:
            return num1 * num2
    result = is_calc(oper, num1, num2)
    return result
