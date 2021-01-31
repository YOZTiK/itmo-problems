t = int(input())
for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()[:n]]
    count = 0
    flag = -1
    for j in range(n):
        if (a[j] > 1):
            flag = j
            break
        count += 1

    if (flag == -1):
        if (n % 2 == 0 and count == n):
            print('Second')
        elif (n % 2 != 0 and count == n):
            print('First')
    else:
        if (flag % 2 == 0):
            print('First')
        else:
            print('Second')
