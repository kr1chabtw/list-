a = [1, 3, 4, 5]
b = [4, 5, 6, 7]
for i in b:
    for j in a:
        print(f'{i} - i')
        print(f'{j} - j')
        if i == j:
            b.remove(i)
            print(b)
print(b)