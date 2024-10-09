array = []
n = int(input("Введите любое число: "))
for i in range(n, n+10):
    array.append(i)
    if len(array) == 5:
        print(f'Сам список = {array}')
        print(f'Срез от i[2] до i[4] = {array[2:4]}')
        break