n = []
n = [int(item) for item in input().split()]

max_element = int(max(n))
min_element = int(min(n))
range_of_elements = max_element - min_element + 1

count_arr = [0 for _ in range(range_of_elements)]

for i in range(0, len(n)):
	count_arr[n[i] - min_element] += 1

start = min_element
for i in range(0, len(count_arr)):
	if count_arr[i] != 0:
		for i in range(0, count_arr[i]):
			print(start, end=' ')
	start += 1