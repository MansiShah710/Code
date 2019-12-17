#!/usr/bin/env python3
# -*- coding: utf-8 -*-


######### Read a file and find the account which has sent the maximum emails.

maximumCount = 0
maximumEmail = ''
x = dict()
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith('From '):
            new = line.split(' ')
            x[new[1]] = x.get(new[1], 0) + 1
    for email in x:
        if x[email] > maximumCount:
            maximumCount = x[email]
            maximumEmail = email
    print("email =", maximumEmail, " count =", maximumCount)
except:
    print("File cannot be opened", fname)




########## Read a file and count the number of emails sent from all email addresses.

countMap = dict()
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith('From '):
            new = line.split(' ')
            new2 = new[1].split('@')[1]
            countMap[new2] = countMap.get(new2, 0) + 1 
    print(countMap)
except:
    print("File cannot be opened", fname)








