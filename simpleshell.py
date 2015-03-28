#! /usr/bin/env python
'''
Created on Feb 1, 2015

@author: mart00n

'''
import hashlib

#define user/pw dictionary object
userdata = {}

print("Welcome to initial setup, please set an administrative password:")

#username = input('username:')
adminpw = hashlib.sha224(input('password:').encode('utf-8')).digest()

print("Setup completed, you are signed in as admin. Type 'help' for options")
print("Enter a command:")
command = input("$")

#command = 'lock'

while command != "terminate":
    if command == "useradd":
        print("Please add new users username and password.")
        user = input("username:")
        userpw = hashlib.sha224(input("password:").encode('utf-8')).digest()
        userdata[user] = userpw
    elif command == "userdel":
        print("Please type user to be removed")
        deluser = input("username:")
        if deluser in userdata:
            del userdata[deluser]
        else:
            print("User not found")
            exit
    elif command == "lock":
        print("System is locked, please enter your username and password:")
        usrentry = input("Username:")
        pwentry =  hashlib.sha224(input("Password:").encode('utf-8')).digest()
        if usrentry == user in userdata and pwentry == userdata[user]:
            print("System unlocked!")
        elif usrentry == 'admin' and pwentry == adminpw:
            print("System unlocked!")
        else:
            print("Incorrect username or password")
            continue
    elif command == "fibonacci":
        a = 0
        b = 1
        n = 0
        nmax = int(input("Maximum iterations:"))
        if nmax > 1000:
            print('Please try again with fewer than 1000 iterations.')
            exit
        else:
            while n < nmax:
                n += 1
                print(a)
                print(b)
                a = a + b
                b = a + b
    command = input("$")

print("Ending program")
