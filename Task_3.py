# 3. Напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
a = input('Введите что считаем: ')
def second_in(list, for_check):
    new_list = []
    for i in range(len(list)):
        if for_check == list[i]:
            new_list.append(i)
    if len(new_list) <= 1:
        return -1
    return new_list[1] # возвращаем второй элемент списка вхождений

print(second_in(my_list, a))
# второй вариант ниже
def fun(list, for_check):
    
    count = 0
    for k in range(len(list)):
        if list[k] == for_check:
            count += 1
            if count == 2:
                return k
    return -1


print(fun(my_list, a))
