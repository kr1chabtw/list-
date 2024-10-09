stroka = str(input())
array = list(stroka)
str2 = ''

for i in range(len(stroka)):
    if stroka[i] == 'a' or stroka[i] == 'а':
        continue
    elif stroka[i] == 'e' or stroka[i] == 'е':
        continue
    elif stroka[i] == 'о' or stroka[i] == 'o':
        continue
    else:
        str2 += stroka[i]
print(str2)





