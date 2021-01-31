dim = list(map(int, input().split()))
n = dim[0]
x = dim[1] - 1

table = []
visited = []

for i in range(n):
    table.append([int(item) for item in input().split()])
    visited.append(-1)

visited[x] = 0

q = [x]
steps = 0

while q:
    v = q.pop(0)

    for i in range(n):
        if table[v][i] == 1 and visited[i] < 0:
            q.append(i)

            visited[i] = visited[v] + 1

for i in range(n):
    print(visited[i], end=" ")