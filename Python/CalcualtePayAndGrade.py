#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Calculate pay based on hours and rate
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if(hours < 0 or rate < 0):
        print("Please enter positive value")
    else:
        pay = hours * rate
        print("Pay: ", pay)
except:
    print("Error, please enter numeric input")




##### Basic function to calculate rate and overtime
        
def computePay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        overtime = hours - 40
        pay = (overtime * (rate * 1.5) + (40 * rate))
    print("pay: ", pay)
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if (hours < 0 or rate < 0):
        print("Please enter positive value")
    else:
        computePay(hours, rate)
except:
    print("Please enter valid input")



  

# Assign grades based on scores
# Considering 0.0 and 1.0 as bad scores since the question explicitly says 
# values between 0.0 and 1.0 
ip = input("Please enter a score between 0.0 and 1.0: ")
try:
  score = float(ip)
  if (score >= 1.0):
    print("Bad score.")
  elif score >= 0.9:
    print("A")
  elif score >= 0.8:
    print("B")
  elif score >= 0.7:
    print("C")
  elif score >= 0.6:
    print("D")
  elif score > 0:
    print("F")
  else:
    print("Bad score.")  
except: 
    print("Bad score.")
    
        

########### Basic function to calculate the grade
# Considering 0.0 and 1.0 as bad scores since the question explicitly says 
# values between 0.0 and 1.0 
    
def calculateGrade(score):
  if (score >= 1.0):
    print("Bad score.")
  elif score >= 0.9:
    print("A")
  elif score >= 0.8:
    print("B")
  elif score >= 0.7:
    print("C")
  elif score >= 0.6:
    print("D")
  elif score > 0:
    print("F")
  else:
    print("Bad score.")  
try:       
    ip = input("Please enter a score between 0.0 and 1.0: ")
    score = float(ip)
    calculateGrade(score)
except: 
    print("Bad score.")