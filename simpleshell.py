#! /usr/bin/env python
'''
Created on Feb 1, 2015

@author: mart00n

'''
import hashlib

def priverr():
    print("You do not have the correct privileges for the specified command")

#define user/pw dictionary object
userdata = {}

print("Welcome to initial setup, please set an administrative password:")

#username = input('username:')
adminpw = hashlib.sha224(input('password:').encode('utf-8')).digest()
# necessary to make easy control structure in lock function, adminpw still has separate var
userdata['admin'] = adminpw

print("Setup completed, you are signed in as admin. Type 'help' for options")
print("Enter a command:")
command = input("$")
activeuser = "admin"

#command = 'lock'

while command != "terminate":
    
    if command == "useradd":
        if activeuser == 'admin':
            print("Please add new users username and password.")
            user = input("username:")
            userpw = hashlib.sha224(input("password:").encode('utf-8')).digest()
            userdata[user] = userpw
        else:
            priverr()
            exit
    
    elif command == "logout":
        print("Welcome, please log in to the system")
        loguser = input("Username:")
        if loguser == "admin":
            logpw = hashlib.sha224(input("Password:").encode('utf-8')).digest()
            if logpw == adminpw:
                print("Welcome admin!")
                activeuser = "admin"
                exit
            elif logpw != adminpw:
                print("Incorrect password")
                continue
        elif loguser in userdata:
            logpw = hashlib.sha224(input("Password:").encode('utf-8')).digest()
            if logpw == userdata[loguser]:
                activeuser = loguser
                print("Welcome {}".format(activeuser))
            else:
                print("Incorrect password")
                command = 'logout'
                continue
        else:
            print("User not found")
            continue
# restrict to admin usage    
    elif command == "userdel":
        if activeuser == 'admin':
            print("Please type user to be removed")
            deluser = input("username:")
            if deluser in userdata:
                del userdata[deluser]
            else:
                print("User not found")
                exit
        else:
            priverr()
            exit
# make lock only allow the activeuser to unlock    
    elif command == "lock":
        print("System is locked, please enter your username and password:")
        usrentry = input("Username:")
        pwentry =  hashlib.sha224(input("Password:").encode('utf-8')).digest()
        if usrentry == activeuser and pwentry == userdata[usrentry]:
            print("System unlocked!")
            exit
        elif usrentry == 'admin' and pwentry == adminpw:
            print("System unlocked!")
            exit
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
