from random import randint
array = []
for i in range(10):
    x = randint(1,100)
    array.append(x)
    print(x)
    if len(array) == 10:
        print(f'Список до: {array}')
        break
array.clear()
print(f'Список после: {array}')