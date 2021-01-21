from math import sqrt

class Node:

    def __init__(self, inum):
        self.idnum = inum

class Graph:
    def __init__(self, num, d):
        self.source = num
        self.adjlist = d


    def PrimsMST(self):
        priority_queue = {Node(self.source): 0}
        added = [False] * len(self.adjlist)
        min_span_tree_cost = 0

        while priority_queue:
            node = min(priority_queue, key=priority_queue.get)
            cost = priority_queue[node]

            del priority_queue[node]

            if added[node.idnum] == False:
                min_span_tree_cost += cost
                added[node.idnum] = True

                for item in self.adjlist[node.idnum]:
                    adjnode = item[0]
                    adjcost = item[1]
                    if added[adjnode] == False:
                        priority_queue[Node(adjnode)] = adjcost

        return min_span_tree_cost


def euclidean_distance(a, b):
    return sqrt(sum((a - b) ** 2 for a, b in zip(a, b)))

n_vertex = int(input())
points = [[0 for column in range(2)] for row in range(n_vertex)]
for col in range(n_vertex):
    line = list(map(int, input().split()))
    points[col][0] = line[0]
    points[col][1] = line[1]

adjacency_matrix = [[0 for column in range(n_vertex-1)] for row in range(n_vertex)]
x = 0
y = 0
for actual_vertex in range(0, len(points)):
    for next_vertex in range(0, len(points)):
        if actual_vertex != next_vertex:
            adjacency_matrix[x][y] = (next_vertex, euclidean_distance(points[actual_vertex], points[next_vertex]))
            y += 1
    y = 0
    x += 1

keys = []
for element in range(len(points)):
    keys.append(element)

g1_edges_from_node = dict(zip(keys, adjacency_matrix))

g1 = Graph(0, g1_edges_from_node)
cost = g1.PrimsMST()
print(str(cost))