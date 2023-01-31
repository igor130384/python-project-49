import prompt


def brain_logics(brain_logic):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 0
    while i < 3:
        result = brain_logic()
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            i += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct "
                f"answer was '{result}'\nLet's try again, {name}!"
            )
            break

        if i == 3:
            print(f'Congratulations, {name}!')
