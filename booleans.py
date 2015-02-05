'''
Created on Feb 2, 2015

@author: mart00n
'''
n = 0
print("Try to guess my name in three tries")
while n < 3:
    guess = input("Your name is...")
    if guess == "mart00n":
        print("Good guess, you're right!")
        n = 3
    elif guess != "mart00n":
        print(guess == "mart00n")
        n += 1
if n == 3 and guess == "mart00n":
    print("Game over, you win!")
else:
    print("Game over, you lose")