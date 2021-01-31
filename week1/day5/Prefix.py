def subs(limit):
    result = [0] * limit
    for index in range(1, limit):
        j = result[index-1]
        while j > 0 and s[index] != s[j]:
            j = result[j-1]
        if s[index] == s[j]:
            j += 1
        result[index] = j

    for index in range(limit):
        print(result[index], end=" ")

s = input()
limit = len(s)
subs(limit)


