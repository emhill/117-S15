def sum(n):
	if n <= 1:
		return 1
	else:
		return n + sum(n -1)

print(sum(2))
print(sum(5))