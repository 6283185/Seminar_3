# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input("Введите количество чисел последовательности Фибоначчи: "))
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a            
        a, b = b, a + b

data = list(fibonacci(number))
data_negative = data[::-1] # создаём список негативного Фибоначчи
for i in range(len(data_negative)):
    data_negative[i] = data_negative[i] * -1 # делаем значения отрицательными

res_fibonacci_list = [] # создаём новый(результирующий) список, куда сложим обе последовательности и ноль посередине
for i in range(len(data_negative)):
    res_fibonacci_list.append(data_negative[i]) 

res_fibonacci_list.append(0) # добавляем ноль

for i in range(len(data)):
    res_fibonacci_list.append(data[i]) # добавляем обычную Фибоначчи
print(res_fibonacci_list)