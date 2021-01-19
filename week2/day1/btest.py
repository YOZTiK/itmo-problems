import sys

class SegmentTree:


    def __init__(self, num):
        global n
        global sum_arr
        self.n = num
        self.sum = [] * (4 * num)
        n = num
        sum_arr = [0] * (4 * num)

    def modify(self, i, x):
        self.internalModify(i, x, 0, n - 1, 1)

    def internalModify(self, i, x, a, b, node):

        if a == b:
            sum_arr[node] = x
            return

        middle = (a + b) / 2

        if i <= middle:
            self.internalModify(i, x, a, int(middle), node * 2)
        else:
            self.internalModify(i, x, int(middle + 1), b, node * 2 + 1)

        sum_arr[node] = int(sum_arr[node * 2]) + int(sum_arr[node * 2 + 1])

    def suma(self, l, r):
        return self.internalSum(l, r, 0, n - 1, 1)

    def internalSum(self, l, r, a, b, node):

        if l > b or a > r:
            # print("return 0")
            return 0

        if l <= a and b <= r:
            return sum_arr[node]

        return int(self.internalSum(l, r, int(a), int((a + b) / 2), node * 2)) + int(self.internalSum(l, r, int((a + b) / 2) + 1, int(b), node * 2 + 1))


in_arr = []
query_list = []
i = 0

in_arr.append(sys.stdin.readline().replace("\n", ""))
no_of_lines = int(in_arr[0])
in_arr.append(sys.stdin.readline().replace("\n", ""))

for i in range(no_of_lines*2+1):
    in_arr.append(sys.stdin.readline().replace("\n", ""))

tree = SegmentTree(int(in_arr[0]))
elements = list(in_arr[1].replace(" ", ""))

for i in range(len(elements)):
    tree.modify(i, elements[i])

for i in range(2, len(in_arr)):
    query_list.append([i for i in in_arr[i].split()])

for query in query_list:
    if query[0] == "sum":
        l = int(query[1]) - 1
        r = int(query[-1]) - 1
        print(tree.suma(l, r))
    else:
        y = int(query[1]) - 1
        x = int(query[-1])
        tree.modify(y, x)