import random


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num1 = random.randint(1, 100)
    print('Question:', num1)

    def is_prime(num1):
        for i in range(2, int(num1/2)+1):
            if (num1 % i) == 0:
                return 'no'
                break
            else:
                return 'yes'

    result = is_prime(num1)
    return result
