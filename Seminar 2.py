#Циклы

# используем для итерации по коллекциям (списки, кортежи, словари, множества)
# a = [1,2,3,4]
#
# for element in a:       # пример 1 просто получить элементы(не важно где и как он находится)
#     print(element)
#
# for i in range(len(a)):    # пример 2 найти элемент, сравнение
#     print(a[i])
#
#
#
# # while . . .
#
#
# print(list(range(4)))
#
#
# n = 10
# while n >= 0:
#     if n % 2 == 0:
#         print('event')
#     else:
#         print('not even')
#     n -= 1

# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
# ...
# def factorial(n):
#     counter = 1
#     res = 1
#     while counter <= n:
#         res *= counter
#         counter +=1
#     return res
#
# a = int(input('Введите число: '))
# print(f'Факториал числа {a}: {factorial(a)}')
# ...

# n = int(input("Введите целое неотрицательное число: "))
# res = 1
# i = 1
#
# while i <= n:
#     res *= i
#     i += 1
# print(res)


# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

...
# def fibo(input_num):
#     n1, n2 = 0, 1
#     fibo_id = 2
#     while n2 < input_num:
#         n1, n2 = n2, n1 + n2
#         fibo_id += 1
#     if input_num != n2:
#         fibo_id = -1
#     return fibo_id
#
#
# a = int(input('Введите число: '))
# print(f'Номер числа Фибоначчи: {fibo(a)}')

...

# num = int(input('Введите число: '))
# first = 0
# second = 1
# counter = 2
# while second <= num:
#     if second == num:
#         print(counter)
#         break
#     first, second = second, first + second
#     counter+=1
# else:
#     print(-1)


...


