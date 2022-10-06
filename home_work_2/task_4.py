# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num1 = int(input("Enter number №1: "))
num2 = int(input("Enter number №2: "))

numbers = list(range(num1, num2 + 1))

ignore = 0
multyply = 1
for i in numbers:
    if (i == 0):
        ignore *= 0
    else: 
        multyply *= i
    
print (multyply)
