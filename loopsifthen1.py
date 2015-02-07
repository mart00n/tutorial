#! /usr/bin/env python
'''
Created on Feb 1, 2015

@author: mart00n

'''
import hashlib
print("Please set a username and password:")
username = input('username:')
password = hashlib.sha224(input('password:').encode('utf-8')).digest()
print("Enter a command:")

command = 'lock'

while command != "terminate":
    if command == "lock":
        print("System is locked, please enter your username and password:")
        usrentry = input("Username:")
        pwentry =  hashlib.sha224(input("Password:").encode('utf-8')).digest()
        if usrentry == username and pwentry == password:
            print("System unlocked!")
        else:
            print("Incorrect username or password")
            continue
    elif command == "fibonacci":
        a = 0
        b = 1
        n = 0
        nmax = int(input("Maximum iterations:"))
        while n < nmax:
            n += 1
            print(a)
            print(b)
            a = a + b
            b = a + b
    command = input("$")

print("Ending program")
