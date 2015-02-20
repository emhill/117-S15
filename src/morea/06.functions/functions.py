# #######################################
# Function definitions 
# #######################################

def dbl(x):
  return 2 * x

def dbl_var(myArgument):
  myResult = 2 * myArgument 
  return myResult

def quad(x):
  print("quad")
  return 4 * x

def quad_compose(x):
  print("quad_compose")
  return dbl(dbl(x))


# #######################################
# The main program execution begins here 
# #######################################

print(dbl(5))
print(quad_compose(5))