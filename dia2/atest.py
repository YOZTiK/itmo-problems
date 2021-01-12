size_n = 0
suma = 0
n = []

size_n = input()
n = [int(item) for item in input().split()]

for i in range(0, int(size_n)):
    suma += n[i]

print("res= ", suma, end=' ')