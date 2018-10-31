'''
Generate a sequence in which next number would be the sum of last two numbers that is last two numbers
'''
def gen_fibon(n): # a function for generating fibon.. sequence
    a = 1  # assigned initial value of a
    b = 1  # assigned initial value of b

    for i in range(n):
    	yield a
    	a,b = b,a+b

for num in gen_fibon(10):
	print(num)