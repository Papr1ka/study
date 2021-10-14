from operator import le
from random import randint
import re
from typing import List, Sequence, Union
from time import time


def quicksort(array: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    length = array.__len__()
    if length <= 1:
        return array
    elif length == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        return [array[0], array[1]]

    cursor = length - 1
    q_ind = length // 2
    q = array[q_ind]

    for i in range(length):
        if array[i] >= q:
            for j in range(cursor, i, -1):
                cursor = j
                if array[j] <= q:
                    array[i], array[j] = array[j], array[i]
                    cursor -= 1
                    print(i, cursor)
                    print(array)
                    break
                print(i, cursor)
        print(i, cursor)

        if i >= cursor -1:
            print(i, cursor, '-выход')
            if array[i] >= q:
                i -= 1
            print(array[:cursor], array[cursor:])
            return quicksort(array[:cursor]) + quicksort(array[cursor:])
    

a = [randint(-1000, 1000) for i in range(10)]
a = [-557, 503, -488, 664, 951, 757, 251, -308, 704, -751]
#a = [250, 454, 865, 888, 691]
print(a)
b = quicksort(a)
a.sort()
print(b)
print()
print(a)
print(b == a)