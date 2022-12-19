# 2. Задайте список. Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'
for_check = input("Введите число: ")
my_list = ['sdf13', 'fds66', '34']
def in_list(list, is_in_list):
    result = False
    for i in list:
        if is_in_list in i:
            print(i)
            return True
    return result

print(in_list(my_list, '1'))
