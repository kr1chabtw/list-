from random import randint
array = []
n = int(input("Сколько чисел будет в списке? "))
for i in range(n):
    array.append(randint(0,100))
print(array)
array.reverse()
for j in range(1, len(array)): # без 0 индекса, так как у него нету левого соседа
    if array[j-1] < array[j] > array[j+1]:
        print(f'Индеĸс лоĸального маĸсимума - {len(array) - j - 1}') # -1 из-за 0 индекса, который не идет в учет
        break
    else:
        continue
