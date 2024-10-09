from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
    print(array)
s = 0
for j in range(len(array)):
    for g in range(len(array)):
        if array[j] == array[g]:
            s += 1
        else:
            continue
print(f'{s - len(array)} - столько одинаковых элементов в списке')