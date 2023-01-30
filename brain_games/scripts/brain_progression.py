import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0
    j = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nWhat number is missing in the progression?')
    while i < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(80, 100)
        n = random.randint(2, 10)
        numbers = []
        for r in range(num1, num2, n):
            numbers.append(r)
            numbers.sort()
        result = numbers[random.randint(1, 10)]
        string = " ".join(map(str, numbers[0:10]))
        string = string.replace(str(result), '..')
        print(f'Question: {string}')
        answer = prompt.string('Your answer: ')
        if answer.isdigit():
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
