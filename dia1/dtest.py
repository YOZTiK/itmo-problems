size_n = 0
n = []

size_n = input()
n = [int(item) for item in input().split()]

print(size_n)
print(n)


# max_element = int(max(n))
# min_element = int(min(n))
# range_of_elements = max_element - min_element + 1
#
# count_arr = [0 for _ in range(range_of_elements)]
#
# for i in range(0, len(m)):
# 	for j in range(0, len(n)):
# 		if m[i] == n[j]:
# 			count_arr[n[j] - min_element] += 1
#
# for i in range(0, len(count_arr)):
# 	print(count_arr[i], end=' ')