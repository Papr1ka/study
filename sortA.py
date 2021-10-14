from operator import le
from random import randint
import re
from typing import List, Sequence, Union
from time import time


def quicksort(array: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    length = array.__len__()
    if length <= 1:
        return array

    cursor = length - 1
    q_ind = length // 2
    q = array[q_ind]

    for i in range(length):
        if i >= cursor:
            print(i, cursor, '-выход')
            if array[i] >= q:
                i -= 1
            print(array[:i + 1], array[i + 1:])
            return quicksort(array[:i + 1]) + quicksort(array[i + 1:])
            break
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