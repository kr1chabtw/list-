from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
print(array)
array.reverse()
for j in range(1, len(array)): # без 0 индекса, так как у него нету левого соседа
    if array[j-1] < array[j] > array[j+1]:
        print(array[j])
        break
    else:
        continue
