from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
print(array)
array.sort()
print(f'{array[0]} - наименьшее число в списке')
