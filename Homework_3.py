# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 10.01]

def diff_between_decimal(list):
    new_list = [round(i % 1, 2) for i in list if i % 1 != 0]
    return max(new_list) - min(new_list)

print(diff_between_decimal(my_list))