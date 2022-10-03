# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num1 = input("Enter a number: ")
num2 = num1.split(".")

num3 = int(num2[0])
num4 = int(num2[1])

sum1 = 0
sum2 = 0

while (num3 != 0):
    sum1 = sum1 + (num3 % 10)
    num3 = num3 // 10

while (num4 != 0):
    sum2 = sum2 + (num4 % 10)
    num4 = num4 // 10

print(sum1 + sum2)




