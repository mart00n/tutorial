#! /usr/bin/env python3
'''
Created on Feb 1, 2015

@author: mart00n
'''
from random import randint

number = randint(0,99)
guess = -1
count = 0

print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))
 
    if guess == number:
        if count <= 3:
            print("Hooray! You guessed it right!")
        elif count > 3:
            print("That took you a while to figure out...")
    elif guess < number:
        print("It's bigger...")
        count += 1
    elif guess > number:
        print("It's not so big.")
        count += 1
