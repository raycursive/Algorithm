from random import randint


def randomselection(array, stat):
    pivot = randint(0, len(array) - 1)
    scope = array[:pivot] + array[pivot + 1:]
    leftpart = [i for i in scope if i <= array[pivot]]
    rightpart = [i for i in scope if i > array[pivot]]
    if len(leftpart) == stat - 1:
        return array[pivot]
    elif len(leftpart) > stat - 1:
        return randomselection(leftpart, stat)
    else:
        return randomselection(rightpart, stat - len(leftpart) - 1)


def randomselection2(array, stat):
    rand = randint(0, len(array) - 1)
    array[0], array[rand] = array[rand], array[0]
    pivot = array[0]
    i = 0
    for j in range(1, len(array)):
        if (array[j] < pivot):
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i], array[0] = array[0], array[i]
    if i == stat - 1:
        return array[i]
    elif i > stat - 1:
        return randomselection2(array[:i], stat)
    else:
        return randomselection2(array[i + 1:], stat - i - 1)