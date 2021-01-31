constrain = (2**31)-1

def arr_min(arr, queue):
    m = constrain
    r = -1
    for index in queue:
        if m > arr[index]:
            m = arr[index]
            r = index

    return r


n = input()

matrix = []

for i in range(int(n)):
    matrix.append([int(item) for item in input().split()])

result = []

for s in range(int(n)):
    q = []
    dist = []

    for i in range(int(n)):
        dist.append(constrain)
        q.append(i)

    dist[s] = 0

    while q:
        u = arr_min(dist, q)
        q.remove(u)

        for i in range(int(n)):
            if matrix[u][i] != 0:
                aux = dist[u] + matrix[u][i]
                if aux < dist[i]:
                    dist[i] = aux

    result.append(dist)

for i in range(int(n)):
    for j in range(int(n)):
        print(result[i][j], end=" ")
    print("")
