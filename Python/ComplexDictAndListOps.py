#!/usr/bin/env python3
# -*- coding: utf-8 -*-


########### Read a file and find how many emails are sent every hours of the day.

hoursDict = dict()
outputList = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    colPos = words[5].find(':')
    hour = words[5][:colPos]
    if hour not in hoursDict:
        hoursDict[hour] = 1
    else:
        hoursDict[hour] += 1

for key, val in list(hoursDict.items()):
    outputList.append((key, val))             

outputList.sort()                              

for key, val in outputList:
    print(key, val)
    
    

########### Read a file and calculate the count of every letter in the file. Then sort it and show the most occurring letter.

import string
letterCount = 0                          
countsDict = dict()
reverseList = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    
    words = line.split()
    for word in words:
        for letter in word:
            letterCount += 1
            if letter not in countsDict:
                countsDict[letter] = 1
            else:
                countsDict[letter] += 1

for key, val in list(countsDict.items()):
    reverseList.append((val/letterCount, key))  

reverseList.sort(reverse=True)         
for key, val in reverseList:
    print(key, val)



##### Regular expression search
 
import re
import os
x=input('Enter a regular expression:')

file = open(os.path.expanduser("~/Downloads/mbox.txt"))

count = 0

for line in file:
  if re.search(x, line):
    count=count+1
print ("mbox.txt had",count, "lines that matched" , x)




##### Use regular expression to find out all occurrences of a specific string and then parse the data for that string to find the average

import os
import re
count = 0
sum1 = 0
fname = input("Enter file name: ")
hand = open(fname)

for line in hand:
    x=re.findall("^New Revision: ([0-9.]+)", line)
    for item in range(len(x)):
        count += 1
        sum1 += float(x[item])
average = sum1/count
print(average)
  