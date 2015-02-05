'''
Created on Feb 1, 2015

@author: mart00n
'''
def fibonacci(maxn):
    a = 0
    b = 1
    n = 0
    while n <= maxn:
        print(a)
        print(b)
        a += b
        b += a
        n += 1

spec = int(input("Enter the max iterations:"))

fibonacci(spec)