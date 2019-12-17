#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
###### Keep accepting input from the user till done is entered and then output the average
total = 0
count = 0
average = 0
while True:
    number = input("Enter a number: ")
    try:
         value = float(number)
         total += value
         count += 1
         average = total/count
    except:   
        if (number == "done" or number == "Done"):
            break
        else:
            print("Invalid input!")
            continue
print("total = ", total,"; count = ", count, "; average = ", average)

    


##### Keep accepting input till the user enters done and calculate min and max of the inputs

total = 0
count = 0
maximum = 0
minimum = 0
x = list()
while True:
    number = input("Enter a number: ")
    try:
         value = float(number)
         x.append(value)
         total = total + value
         count += 1
    except:   
        if (number == "done" or number == "Done"):
            if(len(x) > 0):
                maximum = max(x)
                minimum = min(x)
            break
        else:
            print("Invalid input!")
            continue
print("total =", total,"count =", count, "maximum=", maximum, "minimum = ", minimum )



#### Basic counting function for characters

word = "banana"
count = word.count('a')
print("The count is " , count)



###### Basic substring code
str = 'X-DSPAM-Confidence:0.8475'
colpos = str.find(':')
var = float(str[colpos+1:])
print("The extracted string is", var, "and it is converted to", type(var))

 

