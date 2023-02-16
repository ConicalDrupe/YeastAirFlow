#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:12:48 2023

@author: boon
"""
#DONE WEEKLY FRIDAY NIGHT
import pandas as pd

# Read Files
temp = pd.read_excel(r"/home/boon/Python/AirFlowTest/temp_master.xlsx")
new_master = pd.read_excel(r"/home/boon/Python/AirFlowTest/master.xlsx")

# Compare Rows
rows = temp.shape[0]
new_master_reduced = new_master.iloc[:rows]
compare_past = temp.compare(new_master_reduced)

if compare_past.empty == True:
    print("Original row data is retained")
else:
    print("ERROR: past row data has changed")
    
    
# Compare that new data was appended correctly
# Use current week data

from datetime import datetime, timedelta

#Create filename - cannot be done at 00:00

now = datetime.now()
monday = now - timedelta(days = now.weekday())
monday_str = monday.date().strftime("%m-%d-%Y")
filename = monday_str + ".xlsx"

# For Network storage, we must interact with API here

filepath = "/home/boon/Python/AirFlowTest/"
week_log = pd.read_excel(filepath + filename)

## Compare new data was appended

master_appended = new_master.iloc[rows:]
compare_new = week_log.compare(master_appended)

if compare_new.empty == True:
    print("New data was appended correctly")
else:
    print("ERROR: new row data was not appended correctly")
