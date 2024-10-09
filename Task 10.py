from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
print(array)
s = 0
ar = 0
for j in range(len(array)):
    s += array[j]
    ar += 1
print(f'{s/ar} - среднее арифметическое чисел в списке')