'''
Created on Mar 1, 2015

@author: mart00n
'''
'''
Give the program a number, print that number minus 1 recursively until 0
is reached.
'''

def iter(n):
    if n >= 1:
        print(n)
        n -= 1
        iter(n)
    else:
        exit
        
usr = int(input('Enter an integer value.'))

iter(usr)