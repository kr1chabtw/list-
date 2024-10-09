from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
    print(array)
s = len(array)
print(s)
for j in range(len(array)):
    for g in range(len(array)):
        if array[j] == array[g]:
            s -= 1
        else:
            continue
print(f'{len(array) + s} - столько уникальных элементов в списке')