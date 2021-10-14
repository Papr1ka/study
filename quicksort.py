from typing import List, Union

def quicksort(array: List[Union[int, float]]) -> List[Union[int, float]]:
    """алгоритм быстрой сортировки "на месте" python"""
    #подсчитываем количество элементов в массиве
    length = array.__len__()

    #делаем выход из рекурсии
    if length <= 1:
        return array

    #выбираем опорный элемент q и индекс правого курсора cursor
    q = array[length // 2]
    cursor = length - 1
    
    #left - индекс левого курсора
    for left in range(length):
        #если курсоры перешли друг друга, выходим из цикла
        if left > cursor:
            break
        #ведём курсор до того, пока элемент меньше опорного
        if array[left] >= q:
            #остановили левый курсор, выбираем элемент от правого курсора для обмена, right - индекс правого курсора
            for right in range(cursor, left - 1, -1):
                #запоминаем место старта правого курсора для следующего прохода
                cursor = right
                #нашли элемент для обмена, меньше или равен опорному
                if array[right] <= q:
                    #меняем элементы от курсоров
                    array[left], array[right] = array[right], array[left] 
                    #переводим правый курсор на следующий элемент, если курсор не находится с левого края и выходим из цикла
                    cursor -= 1 if cursor > 0 else 0
                    break
    
    #выбираем точку разбиения массива на подмассивы, если элемент от правого курсора больше, то он попадёт в число больших, иначе в число маленьких
    if array[cursor] > q:
        cursor -= 1
    #вызываем функцию для подмассивов
    return quicksort(array[:cursor + 1]) + quicksort(array[cursor + 1:])
