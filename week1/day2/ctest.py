def count_coins(arr_coins, jump, sum, pos=None):
    if pos is None:
        pos = [1]
    print(pos)
    for i in range(jump):
        if arr_coins[i+pos[-1]]>=0:
           pos += [i+1]
           sum += arr_coins[pos[-1]]
    if pos[-1] < len(arr_coins)-1:
        count_coins(arr_coins, jump, sum, pos)
    return sum, pos


n = [8, 3]
size_n = [2, -3, 5, -1, 5, -9, 8, 6]
revenue, jumps = count_coins(size_n, n[1], 0)
print(revenue)
print(len(jumps))
print(jumps)