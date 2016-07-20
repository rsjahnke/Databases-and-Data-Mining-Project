# CodeToCalcAvgs.py
# Final Project
# CS 105
# 4/28/16

# uses a SQLite command to calculate the average change in internet use
# and average change in homicide count from 1990-2014 for each region
# of the globe

import sqlite3

db = sqlite3.connect('FinalProject.sqlite')

cursor = db.cursor()

# calculate average change in internet use and homicide count for
# EACH REGION by grouping by region
command = '''SELECT Region, AVG(InternetChange), AVG(HomRateChange)
             FROM Full_Regions
             GROUP BY Region;'''

cursor.execute(command)

# print resulting table to output file in order to access table to
# create data graphic
outfile = open('Average internet_homicide_change by region.csv', 'w')

# print column titles to file
print('Region,Avg. Change in Internet Use,Avg. Change in Hom. Count', file = outfile)

# print region, average change in internet use, and average change in
# homicide count to file
for row in cursor:
    print(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]), file = outfile)

db.commit()
db.close()
outfile.close()
