import sys
arr_raw = input()
arr_list = arr_raw.split(" ")
arr = list(map(int, arr_list))
if not arr or len(arr) == 1:
	print("Yes")
else:
	f = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
	s = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
	for j in range(len(arr)):
		f[j][j] = arr[j]
		for i in range(j - 1, -1, -1):
			f[i][j] = max(arr[i] + s[i+1][j], arr[j]+s[i][j-1])
			s[i][j] = min(f[i+1][j], f[i][j-1])
	if(f[0][-1] >= s[0][-1]):
		print("Yes")
	else:
		print("No")



