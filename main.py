# some_dict = {'apple': 'яблоко', 'grape': 'виноград'}
# str, int, float, bool, tuple, frozenset

# some_str = 'привет'
# print(id(some_str))
# some_str += '!'
# print(id(some_str))

# print(some_dict['apple'])
# some_dict['orange'] = 'апельсин'
# print(some_dict)
#
# for el in some_dict:
#     print(el, some_dict[el])
#
# for value in some_dict.values():
#     print(value)


# Задача на Скрабл

# text = str(input('Введите слово '))
# dictionary1 = {'A': '1', ...}
# summ = 0
# for i in text:
#     summ = summ + int(dictionary1[i.upper()])
# print(summ)

# Напишите программу, которая принимает на вход
# строку, и выводит количество повторов каждого символа
# Input: aaabcaadcdd
# Output: a: 5, b: 1, c: 2, d: 3

# some_dict = {}
#
# some_str = 'aabc'
# for s in some_str:
#     if s in some_dict:
#         some_dict[s] = some_dict[s] + 1
#     else:
#         some_dict[s] = 0
#
# for s in some_dict:
#     value = some_dict[s]
#     if value > 0:
#         print(f'Буква {s} встречается {value} раз')


# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(N):
#     if N == 0:
#         return 0
#     elif N ==1:
#         return 1
#     else:
#         fib(N-1) + fib(N-2)

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# arr = [1,4,3,5,2,3,2]
#
# max = 0
# min = 5
# for i in range(len(arr)):
#     val = arr[i]
#     if val < min:
#         min = val
#     if val > max:
#         max = val
#
# for i in range(len(arr)):
#     if arr[i] == max:
#         arr[i] = min
#
# print(arr)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def isSimply(N):
#     i = 2
#     while i < N:
#         if N % i ==0:
#             return False
#         i +=1
#     return True
#
# for i in range(100):
#     if isSimply(i):
#         print(i)
#

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def f(count):
#     if count == 0:
#         return
#     else:
#         x = int(input('Input number: '))
#         f(count-1)
#         print(x)
# f(4)

# Задача 2
# Создайте список из случайных чисел. Найдите номер его последнего локального максимума.
# Локальный максимум - элемент, который больше любого из своей соседей.

# import random
# n = int(input('Введите количество элементов: '))
# list = [random.randint(-50, 50) for item in range(n)]
# print(list)
# local_max = 0
# for i in range(1, len(list) - 1):
#     if list[i] > list[i - 1] and list[i] > list[i + 1]:
#         local_max = list[i]
# print(local_max)
# print(i)

# Задача 4
# Создайте список из случайных чисел. Найдите второй максимум.

# import random
# n = int(input('Введите количество элементов: '))
# list = [random.randint(-50, 50) for item in range(n)]
# print(list)
# list.sort()
# print(list[-2])

# Задача 3

# import random
# numbers = [random.randint(1, 10) for _ in range(20)]
# count_dict = {}
#
# for num in numbers:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1
#
# max_count = max(count_dict.values())
#
# print("Максимальное количество одинаковых элементов:", max_count)