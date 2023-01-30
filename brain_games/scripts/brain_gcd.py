import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0
    j = 0
    num1 = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')

    def gsd2(a, b):
        if b == 0:
            return a
        else:
            return gsd2(b, a % b)

    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')
        x = gsd2(num1, num2)
        answer = prompt.string('Your answer: ')
        if answer.isdigit():
            if int(answer) == int(x):
                print('Correct!')
            else:
                print(
                    f"'{answer}' is wrong answer ;(. Correct "
                    f"answer was '{x}'\nLet's try again, {name}!"
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
