# size_n = int(input())
# n = [int(item) for item in input().split()]

size_n = 2
n = [1, 2]

if n[0] > n[1] or n[0] > 0 and n[1] > 0:
    suma = n[0]
    counter = 0
    for i in range(0, size_n):
        try:
            if n[counter + 1] < 0:
                e1 = n[counter + 1] if (counter+1) < size_n-1 else 0
                e2 = n[counter + 2] if (counter+2) <= size_n-1 else 0
                if e1 > e2:
                    suma += e1
                else:
                    suma += e2
                    counter += 1
            else:
                suma += n[counter+1]
        except IndexError:
            if (counter-1) < size_n and n[counter - 1] < 0:
                suma += n[counter-1]
        counter += 1
else:
    suma = n[1]
    counter = 1
    for i in range(1, size_n):
        try:
            if n[counter + 1] < 0:
                e1 = n[counter + 1] if (counter + 1) < size_n - 1 else 0
                e2 = n[counter + 2] if (counter + 2) <= size_n - 1 else 0
                if e1 > e2:
                    suma += e1
                else:
                    suma += e2
                    counter += 1
            else:
                suma += n[counter + 1]
        except IndexError:
            if (counter - 1) < size_n and n[counter - 1] < 0:
                suma += n[counter - 1]
        counter += 1

print(suma, end=' ')