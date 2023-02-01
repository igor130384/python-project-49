import random


def brain_progression():
    print('What number is missing in the progression?')
    list = []
    step = random.randint(1, 10)
    num1 = random.randint(0, 100)
    while len(list) < 10:
        list.append(num1)
        num1 += step
    index = random.randint(0, 9)
    result = list[index]
    b = ".."
    list[index] = b
    a = ''
    for i in list:
        a += f'{i} '
    print('Question:', a)
    return result
