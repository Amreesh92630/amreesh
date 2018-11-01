'''
Given a number n, write an efficient function to print all prime factors of n. 
For example, if the input number is 12, then output should be “2 2 3”. 
And if the input number is 315, then output should be “3 3 5 7
'''
# a fuction for determining prime factor
# a given number n
import math
def prime_factor(n):
    
    while n % 2 == 0:
        print (2)
        n = n/2

# now n must be odd
# 2 not be used (i = i + 2)
    for i in range(3,int(math.sqrt(n)) + 1,2):
        # while i devides n
        while n % i == 0 :
            print (i)
            n = n/i

    if n > 2 :
        print (n) 

prime_factor(36)



    
