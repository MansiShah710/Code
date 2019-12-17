#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###### Use NumPy to create a 3x3x3 array with random values and find the minimum and maximum values.

import numpy as np
x = np.random.rand(3,3,3)
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum: ",xmin, "\nMaximum: ", xmax)


##### Use NumPy to create a 10x4 array with random values and extract the first five rows of the array and store them into a variable.


import numpy as np
x = np.random.rand(10, 4)
print(x)
y= x[:5, :]
print("First 5 rows of the array:\n", y)



##### 3. Use Pandas to read WorldCountries.csv (available on Blackboard) into Pandas DataFrame, display the data information (use info() method) and first five rows (use head() method), and show the simple statistics (use describe() method). 

import pandas as pd
df = pd.read_csv('~/Downloads/WorldCountries.csv') 
print(df.info())
print(df.head())
print(df.describe())
