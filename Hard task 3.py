from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
    print(array)
array.sort(reverse=True)
print(array)
print(f'{array[1]} - второй максимум в списке')