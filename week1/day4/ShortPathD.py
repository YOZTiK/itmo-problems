lim = (2 ** 10) + 1


def min_in_arr(arr, queue):
    m = lim
    res = -1
    for index in queue:
        if m >= arr[index]:
            m = arr[index]
            res = index

    return res


dim = [int(item) for item in input().split()]

n = dim[0]
s = dim[1] - 1
d = dim[2] - 1

table = []

for i in range(n):
    table.append([int(item) for item in input().split()])

q = []
dist = []

for i in range(n):
    dist.append(lim)
    q.append(i)

dist[s] = 0

while q:
    u = min_in_arr(dist, q)

    if u == d:
        q = []
    else:
        q.remove(u)

    for i in range(n):
        if table[u][i] > 0:
            aux = dist[u] + table[u][i]
            if aux < dist[i]:
                dist[i] = aux

if dist[d] == lim:
    print(-1)
else:
    print(dist[d])