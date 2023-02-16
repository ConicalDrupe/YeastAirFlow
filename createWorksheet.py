#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:02:12 2023

@author: boon
"""
# DONE WEEKLY ON FRIDAY (After master append)

import xlsxwriter
from datetime import datetime, timedelta

# Directory to save
directory = r"/home/boon/Python/AirFlowTest/"


# Create filename for next monday - cannot be done at 00:00
now = datetime.now()
next_monday = now + timedelta(days = 3)
next_monday_str = next_monday.date().strftime("%m-%d-%Y")
filename = next_monday_str + ".xlsx"


# Create workbook in directory with filename
workbook = xlsxwriter.Workbook(directory + filename)
worksheet = workbook.add_worksheet()

# Create formats
 # Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1}) 

# Create headers
worksheet.write('A1', 'Date', bold)
worksheet.write('B1', 'Photographer', bold)
worksheet.write('C1', 'Focuser', bold)
worksheet.write('D1', 'Species', bold)
worksheet.write('E1', 'Pictures Taken', bold)

# Creatre proper column spacing
worksheet.set_column(1, 1, 15)
worksheet.set_column(1, 2, 15)
worksheet.set_column(1, 3, 8)
worksheet.set_column(1, 4, 10)
worksheet.set_column(1, 5, 15)


workbook.close()