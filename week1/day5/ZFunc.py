s = input()

n = len(s)

left = 0
right = 0

res = [0]*n

for i in range(1, n):
    if i <= right:
        res[i] = min(right-i+1, res[i-left])
    while i+res[i] < n and s[i+res[i]] == s[res[i]]:
        res[i] += 1
    if i+res[i]-1 > right:
        right = i+res[i]-1
        left = i

for i in range(1, n):
    print(res[i], end=" ")
