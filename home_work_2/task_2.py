# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
num = int(input("Enter a number: "))
numbers = list(range(1, num + 1))
i = 1
 
 
while (i < len(numbers)):
    numbers[i] = numbers[i] * numbers[i - 1]
    i+=1
else: print(numbers)


