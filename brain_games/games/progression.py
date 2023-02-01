import random


def brain_progression():
    print('What number is missing in the progression?')
    num1 = random.randint(1, 10)
    num2 = random.randint(80, 100)
    n = random.randint(2, 10)
    numbers = []
    for r in range(num1, num2, n):
        numbers.append(r)
        numbers.sort()
    result = numbers[random.randint(1, 10)]
    numbers.insert(result, "..")
    string = " ".join(map(str, numbers[0:10]))
    string = string.replace(str(result), '..')
    print(f'Question: {string}')
    return result
