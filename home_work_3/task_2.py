# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.




numbers = list(range(1, 10))
print(numbers)
i = 0
j = len(numbers)
num = 0
while i < j:
    num = numbers[i] * numbers[j - 1]
    print(num)
    i+=1
    j-=1
else: print ("Stop")
