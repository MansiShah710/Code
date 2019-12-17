#!/usr/bin/env python3
# -*- coding: utf-8 -*-


######## Read a file and count the occurrences of a specific string. Also, parse and calculate the average based on the extracted values from this file.

filename = input("Enter file name: ")
try:
    fhand = open(filename)
    count = 0
    total = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            y = line.split(':')
            try:
                total = total + float(y[1])
            except:
                print('Cannot convert to float', y[1])
                continue
            count = count + 1
    if count > 0:
        avg = total/count
        print('total: ', total, ' count: ', count)
        print('Average spam confidence: ', avg)
    else:
        print('No entries found in file')
except:
    print('Exception thrown. File may not exist - ', filename)

        

######## Open a file and count the occurrences of a specific line and print that out. If a specific file name is entered, just print an error message.

fname = input('Enter the file name:  ')
try:
    if(fname == "na na boo boo"):
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        fhand = open(fname)
        count = 0
        for line in fhand:
            if line.startswith('Subject:') :
                count = count + 1
        print('There were', count, 'subject lines in', fname)

except:
        print("File cannot be opened: ", fname)
 



######### Read a file and count the number of lines starting with "From"
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith('From '):
            splitLine = line.split(' ')
            count = count + 1
            print(splitLine[1])
    print("There were", count,"lines in the file with From as the first word")
except:
    print("File cannot be opened", fname)



######## Accept inputs from the user and store them in a list and calculate the minimum and maximum of the list

maximum = 0
minimum = 0
x = list()
while True:
    number = input("Enter a number: ")
    try:
         value = float(number)
         x.append(value)
    except:   
        if (number == "done" or number == "Done"):
            if(len(x) > 0):
                maximum = max(x)
                minimum = min(x)
            break
        else:
            print("Invalid input!")
            continue
print("maximum =", maximum, "minimum =", minimum)

