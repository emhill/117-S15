def f(x): 
	x = x-1
	return g(x)+1

def g(x):
	return x*2

def h(x):
	if x%2 == 1:      # x odd
		return f(x) + x
	else:             # x even
		return f(f(x))

print(h(4))
print(h(3))