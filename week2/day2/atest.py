def get_min(l, r):
    k = maxp[r - l]
    return min(sparse[l][k], sparse[r - (1 << k)][k])


sparse = [[0] * 2] * 2
maxp = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

n = a[0]
# Biggest power
bp = 1
while 1 << bp <= n:
    bp += 1

sparse = [[] * n] * bp

for k in range(0, bp):
    for i in range(0, (n - (1 << k))):
        sparse[i][k] = min(sparse[i][k - 1], sparse[i + (1 << (k - 1))][k - 1])

maxp = [] * (n + 1)

for i in range(2, (n + 1)):
    maxp[i] = maxp[i // 2] + 1

for i in range(0, ):

print(maxp)