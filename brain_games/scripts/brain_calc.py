import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0
    j = 0
    operand = ['+', '-', '*']
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    while i < 3:
        oper = random.choice(operand)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {oper} {num2}')
        answer = prompt.string('Your answer: ')
        if answer.isdigit():
            if oper == '+':
                result = num1 + num2
            elif oper == '-':
                result = num1 - num2
            else:
                result = num1 * num2
            if int(answer) == int(result):
                print('Correct!')
            else:
                print(
                    f"'{answer}' is wrong answer ;(. Correct "
                    f"answer was '{result}'\nLet's try again, {name}!"
                )
                break
        else:
            print('Введите число')
            j += 1
            if j == 3:
                print("Вы проиграли!!!")
                break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
