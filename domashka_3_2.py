# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

list_nums = [randint(1, 21) for _ in range(int(input("Введите количество элементов в массиве: ")))]

print(list_nums)
num = int(input("Задайте число: "))
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num - right_num):
        right_num = i

print("Самый близкий по величине элимент: ", right_num)