
array = []
n = int(input("Введите любое число: "))
for i in range(n, n+20):
    if i % 2 == 0:
        array.append(i)
        if len(array) == 10:
            print(array)
            break
