import random


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num1 = random.randint(1, 100)
    print(f'Question: {num1}')

    def is_prime():
        k = 0
        string = ''
        for p in range(2, num1 // 2 + 1):
            if (num1 % p == 0):
                k = k + 1
        if (k <= 0):
            return 'yes'
        else:
            return 'no'
    result = is_prime(num1)
    return result
