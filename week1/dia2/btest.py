import math

def grasshopper(cells, max_jump):
    number_solutions = 0
    solutions = []
    if cells == 1 and max_jump == 1:
        return 1
    for jump_size in range(max_jump,0,-1):
        for s in solutions:
            total = 0
            for elements in s:
                total += elements
            for n in range((cells-total)//jump_size,0,-1):
                solutions.append(s+[jump_size for i in range(n)])

        for n in range(cells-1//jump_size,0,-1):
            solutions.append([jump_size for i in range(n)])

    solutions.sort()

    s_last = []
    for s in solutions:
        total = 0
        count = 0
        if s_last == s:
            continue
        for elements in s:
            total += elements
            count += 1
        if total == cells - 1:
            # print(s , total)
            permutations = math.factorial(count)
            for unique in set(s):
                permutations = permutations // math.factorial(s.count(unique))
            # print("permutations:", permutations)
            # print()
            number_solutions += permutations
        s_last = s

    if(max_jump <= cells):
        return number_solutions
    else:
        return 1


# n = [int(item) for item in input().split()]
# answer = grasshopper(n[0],n[1])
answer = grasshopper(10,4)

print(answer)
