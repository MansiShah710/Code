#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    hours = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    pay = float(hours) * float(rate)
    print("Pay: ", pay)
except:
    print("Invalid input")

##################################

print("Celsius to Fahrenheit conversion")
try:
    celsius = float(input("Enter celcius temperature: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit temperature: ", str(fahrenheit))
except:
    print("Not a number")
