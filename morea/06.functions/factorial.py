# recursive factorial
def factorial(n):
  '''This computes n!'''
  if n == 0:	# base case
    return 1
  else:			# induction
    return n*factorial(n-1)

print(factorial(3))
print(factorial(5))