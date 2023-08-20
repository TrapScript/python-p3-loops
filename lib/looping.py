#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy new year")
    

def square_integers(int_list):
    return int_list * int_list
    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("Buzz")