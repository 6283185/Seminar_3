# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
def sum_of_not_even_position(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]                    
    return sum

print(f"Сумма элементов на нечётных индексах списка{my_list} = {sum_of_not_even_position(my_list)}")