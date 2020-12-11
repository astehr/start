a = [int(i) for i in input('Введите числа через пробел: ').split()]

for x in range(len(a) - 1):
    for y in range(len(a) - x - 1):
        if a[y] > a[y + 1]:
            a[y] , a[y + 1] = a[y + 1] , a[y]

print(a)

