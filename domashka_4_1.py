# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

first_numbers = [int(i) for i in input("Введите первую строку чисел: ").split()]
second_numbers = [int(j) for j in input("Введите вторую строку чисел: ").split()]

print("Повторяются числа: ", *sorted(set(first_numbers).intersection(second_numbers)))