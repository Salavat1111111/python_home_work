# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# odd_numbers = []
# even_numbers = []
# l = len(numbers)

# for i in range(l):
#     if ( i % 2 == 0):
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
# print(f'нечетные числа {odd_numbers}')


# for i in range(l):
#     if i%2==0:
#         even_numbers.append(numbers[i])
#     else:
#         odd_numbers.append(numbers[i])
# print(even_numbers)
# 

# while (i <= len(numbers)):
#     if ( i % 2 == 0):
#         num += 0
#     else:
#         num += numbers[i]
# i += 1
# print(num)




# i = 0
# for i in numbers:
#     if (i % 2 == 0):
#         num = num + 0
#     else:
#         num = num + numbers[i]
# print(num)


numbers =list(range(1, 11))
print(numbers)

i = 0
sum = 0

for i in numbers:
 if (numbers.index(i) % 2 != 0):
    sum += i
i+=1
print(sum)




