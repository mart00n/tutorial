'''
Created on Feb 1, 2015

@author: mart00n

'''
print("Please set a username and password:")
username = input('username:')
password = input('password:')
print("Enter a command:")
state = 1

while state == 1:
    command = input("$")
    if command == "lock":
        print("System is locked, please enter your username and password:")
        usrentry = input("Username:")
        pwentry = input("Password:")
        if usrentry == username and pwentry == password:
            print("System is unlocked!")
        else:
            print("Incorrect username or password")
    elif command == "terminate":
        print("Ending program")
        state = 0
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
