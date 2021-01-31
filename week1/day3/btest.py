def count_edges(matrix):
    total = 0
    for horizontal in matrix:
        for vertical in horizontal:
            if vertical == 1:
                total += 1
    return total


# arr = np.array(
#     [
#         [0, 1, 1],
#         [1, 0, 1],
#         [1, 1, 0]
#     ])
#
# print(int(count_edges(arr)/2))


n = input()
matrix = []
for i in range(int(n)):
    matrix.append([int(item) for item in input().split()])

print(int(count_edges(matrix) / 2))

