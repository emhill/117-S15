# recursive tower
def tower(n):
  '''Tower of n'''
  if n == 0:
    return 1
  else:
    return 2**tower(n-1)

for i in range(5):
	print(tower(i))

#print(tower(5))