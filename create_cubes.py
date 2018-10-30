'''
Create a function which calculates cubes of given any range of numbers
'''
def create_cubes(n): # a function which calculates cube of given range of number
    result = []
    for x in range(n):
        result.append(x**3)# result will be stored in list
    return result
for num in create_cubes(10):
	print(num)
