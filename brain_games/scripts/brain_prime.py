import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0

    name = prompt.string('May I have your name? ')
    print(
        f'Hello, {name}!\n "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:

        num1 = random.randint(1, 100)

        print(f'Question: {num1}')
        answer = prompt.string('Your answer: ')

        k = 0
        string = ''
        for p in range(2, num1 // 2 + 1):
            if (num1 % p == 0):
                k = k + 1
        if (k <= 0):
            string = 'yes'
        else:
            string = 'no'
        if string == answer:
            print('Correct!')
        else:

            print(
                f"'{answer}' is wrong answer ;(. Correct "
                f"answer was '{string}'\nLet's try again, {name}!"
            )
            break

            i += 1
        if i == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
