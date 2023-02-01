import random


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num1 = random.randint(1, 100)
    print('Question:', num1)

    def is_prime(num):
        if num == 1:
            return 'no'
        for i in range(2, num):
            if num % i == 0:
                return 'no'
        return 'yes'
    result = is_prime(num1)
    return result
