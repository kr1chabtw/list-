from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
print(array)
s = 0
for j in range(len(array)):
    s += array[j]
print(f'{s} - сумма чисел в списке')