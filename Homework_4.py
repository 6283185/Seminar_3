# Напишите программу, которая будет преобразовывать десятичное число
#  в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите число: "))
def from_ten_to_binary(num):
    s = ""
    while num != 0:
        s = str(num % 2) + s
        num //=2
    return s

print(f"Число {number} в двоичной системе счисления будет выглядеть как -> {from_ten_to_binary(number)}")