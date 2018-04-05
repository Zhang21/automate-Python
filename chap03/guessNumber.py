#!/bin/python3
# coding: utf-8

#猜一个1-20的数字


import random

number= random.randint(1, 20)

print('A number between 1 and 20.')


for times in range(1, 5):
    print('Please input a number: ')
    guess = int(input())
    
    if guess < number:
        print('your guess is too low!')
    elif guess > number:
        print('your guess is too high!')
    else:
        break

if guess == number:
    print('Congratulation! you guessed ' + str(times) + ' times')
else:
    print('Pity! the number is ' + str(number))



