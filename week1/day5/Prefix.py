s = input()

n = len(s)

res = [0] * n

for i in range(1, n):
    j = res[i-1]
    while j > 0 and s[i] != s[j]:
        j = res[j-1]
    if s[i] == s[j]:
        j += 1
    res[i] = j

for i in range(n):
    print(res[i], end=" ")
