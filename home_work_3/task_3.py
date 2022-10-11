#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

a = int(input("Enter new number: "))
list = []
 
for i in range(a):
    list.append(random.uniform(1.5 , 10.5));
print(list)

num = 0
list_2 = []

for i in list:
    num = i - int(i)
    list_2.append(num)

    print(num)
    print(list_2)

print(max(list_2) - min(list_2))




