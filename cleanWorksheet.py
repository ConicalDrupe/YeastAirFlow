#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:29:57 2023

@author: boon
"""

## DONE ON FRIDAY NIGHT

#import pandas as pd
#from datetime import datetime, timedelta

# Create filename - cannot be done at 00:00

#now = datetime.now()
#monday = now - timedelta(days = now.weekday())
#monday_str = monday.date().strftime("%m-%d-%Y")
#filename = monday_str + ".xlsx"

# For Network storage, we must interact with API here

#filepath = "/home/boon/Python/AirFlowTest/"
#data = pd.read_excel(filepath + filename)

#%%
import pandas as pd
# directory to read weekly logs from
read_directory = r"/home/boon/Python/AirFlowTest/"
# directory to save master in
master_directory = r"/home/boon/Python/AirFlowTest/"

data = pd.read_excel(read_directory + "sample_date.xlsx")

# Fix datatypes
data['Focuser'] = data['Focuser'].fillna('')
data[['Photographer','Focuser']] = data[['Photographer','Focuser']].astype(str)

# Concat Photographer and Focuser
data['names'] = data['Photographer'] + " " + data['Focuser']
    # Removes trailing whitespace
data['names'] = data['names'].str.rstrip()

# Defining dictionary for mapping

#people = ["Jan","Christopher","Chelbie","Katie","Jessica","Aurora"]
# Try Combination list method to generate dic...

groupings = {
    "Jan Chistopher": 1,
    "Christopher Jan": 2,
    "Jan Aurora": 3,
    "Aurora Jan": 4,
    "Katie Chelbie": 5,
    "Chelbie Katie": 6,
    "Jessica Jan": 7,
    "Jan Jessica": 8,
    "Jan" : 9,
    "Jessica": 10,
    "Christopher": 11, 
    "Chelbie": 12,
    "Katie": 13,
    "Aurora": 14
    }

# Add New column groupid
data['groupID'] = data['names'].map(groupings)

if data['groupID'].isnull().values.any() == True:
    print("Name is not in dictionary for groupID; Check for mispelling")
    #Throw Airflow Error
else:
    print("groupID mapping was successful")
#%%
# Spell check names
# To add - Checks after dictionary is mapped, that all values are ints and none are nan

#%%

data = data[['Date','names','groupID','Species','Pictures Taken']]
#%%
# Transfer to master file

# Read master file that already exists
temp = pd.read_excel(master_directory + "org_master_sample.xlsx")

# Create new master data fram
new_master = pd.concat([temp,data])

# Create excel file of temp_master and new master
temp.to_excel(master_directory + "temp_master.xlsx" , index=False)
 #In practice org_master_xlsx would be names the same as master.xlsx
new_master.to_excel(master_directory + "master.xlsx" , index=False)

