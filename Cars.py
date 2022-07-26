# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:23:02 2022

@author: Shubham
"""

import pandas as pd

import os

os.chdir(r"D:\Data Analyst\Python Project")
os.listdir()

cars = pd.read_csv("Cars.csv")
cars

cars.shape

# Find all Null value in the dataset. If there is any nul value in any column,
# then fill the mean of that column.

cars.isnull().sum()

cars.mean()

cars.fillna(cars.mean(), inplace=True)

cars.drop(index=30, inplace=True)
cars.drop(index=39, inplace=True)
cars.drop(index=121, inplace=True)
cars.drop(index=173, inplace=True)
cars.drop(index=161, inplace=True)

# Check what are the different types of Make are there in our dataset.
# And, what is the count (occurrence) of each Make in the data ?

cars['Make'].value_counts()

# Show all the records where Origin is Asia or Europe:
    
cars.head(2)

cars[cars['Origin'].isin(['Asia','Europe'])]

# Remove all the records (rows) where Weight is above 4000

cars.head(2)

cars[cars["Weight"]>4000]

cars[~(cars['Weight']>4000)]

# Increase all the values of"MPG_City" column by 3.

cars.head()

cars["MPG_City"]= cars["MPG_City"].apply(lambda x:x+3)

cars
