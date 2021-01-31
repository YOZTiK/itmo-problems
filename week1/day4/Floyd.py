lim = (2**31)-1


def min_in_arr(arr, queue):
    m = lim
    r = -1
    for index in queue:
        if m > arr[index]:
            m = arr[index]
            r = index

    return r


n = int(input())

table = []

for i in range(n):
    table.append([int(item) for item in input().split()])

res = []

for s in range(n):
    q = []
    dist = []

    for i in range(n):
        dist.append(lim)
        q.append(i)

    dist[s] = 0

    while q:
        u = min_in_arr(dist, q)
        q.remove(u)

        for i in range(n):
            if table[u][i] != 0:
                aux = dist[u] + table[u][i]
                if aux < dist[i]:
                    dist[i] = aux

    res.append(dist)

for i in range(n):
    for j in range(n):
        print(res[i][j], end=" ")
    print("")
