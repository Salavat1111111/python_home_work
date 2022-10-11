# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers =list(range(1, 11))
print(numbers)

num = 0
i = 0
for i in numbers:
    if (i % 2 == 0):
        num = num + 0
    else:
        num = num + numbers[i]
print(num)

# while (i <= len(numbers)):
#     if ( i % 2 == 0):
#         num += 0
#     else:
#         num += numbers[i]
# i += 1
# print(num)













