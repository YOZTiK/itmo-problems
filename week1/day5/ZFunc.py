def zfunc(n):
    rt = 0
    lf = 0

    result = [0]*n
    
    for index in range(1, n):
        if index <= rt:
            result[index] = min(rt-index+1, result[index-lf])
        while index+result[index] < n and s[index+result[index]] == s[result[index]]:
            result[index] += 1
        if index+result[index]-1 > rt:
            rt = index+result[index]-1
            lf = index
    
    for index in range(1, n):
        print(result[index], end=" ")
    

s = input()
n = len(s)
zfunc(n)


