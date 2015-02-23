# Add two numbers
# 
# Emily Hill
# CSCI 117

def add(x, y):
	print("I will add the numbers %d and %d" % (x, y))
	return x + y

sum = add(5, 7)
print("=", sum)

"""
Next step: write a function that multiplies two numbers
WITHOUT printing anything
"""
def multiply(x, y):
	return x * y

print("%s: %d * %d = %.2f" % ("multiply", 4, 5, multiply(4, 5)))
#### OR ####
print(4, "*", 5, "=", multiply(4, 5) )