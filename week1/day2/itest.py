target = int(input())

if target == 1:
    print(0)
    print(1)
else:
    sum = 1
    arr = []
    arr.append(sum)
    for i in range(sum, target):
        if (sum*3) <= target:
            sum = sum * 3
            arr.append(sum)
        elif (sum * 2) <= target:
            sum = sum * 2
            arr.append(sum)
        elif (sum + 1) <= target:
            sum += 1
            arr.append(sum)
        else:
            break

    print((len(arr)-1))
    for i in range(0,len(arr)):
        print(arr[i], end=' ')