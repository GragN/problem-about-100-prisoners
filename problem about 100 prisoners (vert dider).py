# задача о 100 заключенных

from random import *
from pprint import pprint

count_prisoners_and_boxes = 100
for_statistics = 100

def boxes():
    l = []
    l1 = []
    for i in range(1, count_prisoners_and_boxes+1):
        l.append(i)

    while len(l1) < count_prisoners_and_boxes:
        number = randint(1, count_prisoners_and_boxes)
        if number not in l1:
            l1.append(number)
        else:
            continue

    l2 = dict(zip(l, l1))
    return l2

def prisoners():
    p = []
    while len(p) < count_prisoners_and_boxes:
        number = randint(1, count_prisoners_and_boxes)
        if number not in p:
            p.append(number)
        else:
            continue
    return p

def example_hundred():
    b = boxes()
    p = prisoners()
    count = 0
    array = []
    array1 = []

    for i in range(0, count_prisoners_and_boxes):
        def recursion(n):
            nonlocal count
            number = b.get(n)
            if p[i] != number:
                count += 1
                return recursion(number)
            elif p[i] == number:
                count += 1
                if count <= 50:
                    array1.append((f"Заключенный под номером {number} нашел свой номер с {count} попытки"))
                    array.append(count)
                    count = 0
                else:
                    array1.append((f"Заключенный под номером {number} проиграл со значением {count}"))
                    array.append(count)
                    count = 0
        recursion(b.get(p[i]))
    return array, array1

def statistics():
    array = []
    for i in range(for_statistics):
        if max(example_hundred()[0]) <= 50:
            array.append("Победа")
        else:
            array.append("Поражение")
    return f"Шанс на победу {(array.count('Победа'))/for_statistics}"

pprint(example_hundred()[1])
print(statistics())
