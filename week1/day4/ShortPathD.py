constrain = (2 ** 10) + 1


def arr_min(arr, queueueue):
    m = constrain
    result = -1
    for index in queueueue:
        if m >= arr[index]:
            m = arr[index]
            result = index

    return result


dim = [int(item) for item in input().split()]

n = dim[0]
s = dim[1] - 1
d = dim[2] - 1

vector = []

for i in range(n):
    vector.append([int(item) for item in input().split()])

queue = []
dist = []

for i in range(n):
    dist.append(constrain)
    queue.append(i)

dist[s] = 0

while queue:
    u = arr_min(dist, queue)

    if u == d:
        queue = []
    else:
        queue.remove(u)

    for i in range(n):
        if vector[u][i] > 0:
            aux = dist[u] + vector[u][i]
            if aux < dist[i]:
                dist[i] = aux

if dist[d] == constrain:
    print(-1)
else:
    print(dist[d])