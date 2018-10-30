'''
Create a function which calculates cubes of given any range of numbers
'''
def create_cubes(n): # a function which calculates cube of given range of number
   
    for x in range(n):
        yield x**3   # result will be memory efficient
    
for num in create_cubes(10):
	print(num)
