# Реализуйте один или несколько видов алгоритмов сортировки.

import random

def bubble_sort(arr): # сортировка пузырьком
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): # это сортировка в обратном порядке
            if arr[j] > arr[j + 1]: # если текущий элемент больше следующего
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # меняем их местами
    return arr

def insertion_sort(arr): # сортировка вставками
    n = len(arr)
    for i in range(1, n): # начинаем с 1, так как первый элемент уже отсортирован
        key = arr[i] # текущий элемент
        j = i - 1 # индекс предыдущего элемента
        while j >= 0 and arr[j] > key: # пока предыдущий элемент больше текущего
            arr[j + 1] = arr[j] # сдвигаем его вправо
            j -= 1 # уменьшаем индекс
        arr[j + 1] = key # вставляем текущий элемент
    return arr

def selection_sort(arr): #
    n = len(arr)
    for i in range(n): # перебираем все элементы
        min_idx = i
        for j in range(i + 1, n): # перебираем оставшиеся элементы
            if arr[j] < arr[min_idx]: # если текущий элемент меньше минимального
                min_idx = j # обновляем минимальный индекс
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # меняем местами`
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # находим середину
        left_half = arr[:mid] # создаем левую половину
        right_half = arr[mid:] # создаем правую половину

        merge_sort(left_half) # рекурсивно сортируем левую половину
        merge_sort(right_half) # рекурсивно сортируем правую половину

        i = j = k = 0 # индексы

        while i < len(left_half) and j < len(right_half): # пока не закончились элементы
            if left_half[i] < right_half[j]: # если левый элемент меньше правого
                arr[k] = left_half[i] # записываем его в итоговый массив
                i += 1 # увеличиваем индекс
            else: # если правый элемент меньше левого
                arr[k] = right_half[j] # записываем его в итоговый массив
                j += 1 # увеличиваем индекс
            k += 1 # увеличиваем индекс

        while i < len(left_half): # пока не закончились элементы
            arr[k] = left_half[i] # записываем его в итоговый массив
            i += 1 # увеличиваем индекс
            k += 1 # увеличиваем индекс

        while j < len(right_half): # пока не закончились элементы
            arr[k] = right_half[j]  # записываем его в итоговый массив
            j += 1 # увеличиваем индекс
            k += 1 # увеличиваем индекс
    return arr

def quick_sort(arr): # быстрая сортировка
    if len(arr) <= 1: # если массив пустой или содержит один элемент
        return arr
    pivot = arr[len(arr) // 2] # выбираем опорный элемент
    left = [x for x in arr if x < pivot] # элементы меньше опорного
    middle = [x for x in arr if x == pivot] # элементы равные опорному
    right = [x for x in arr if x > pivot] # элементы больше опорного
    return quick_sort(left) + middle + quick_sort(right)

arr = [random.randint(0, 100) for _ in range(20)]
print("Исходный массив:", arr)

sorted_arr = bubble_sort(arr.copy())
print("Пузырьковая сортировка:", sorted_arr)

sorted_arr = insertion_sort(arr.copy())
print("Сортировка вставками:", sorted_arr)

sorted_arr = selection_sort(arr.copy())
print("Сортировка выбором:", sorted_arr)

sorted_arr = merge_sort(arr.copy())
print("Сортировка слиянием:", sorted_arr)

sorted_arr = quick_sort(arr.copy())
print("Быстрая сортировка:", sorted_arr)

