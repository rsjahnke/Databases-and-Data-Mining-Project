# CodeToAddRegion.py
# Final Project
# CS 105
# 4/20/16

# joins the 'Full' and 'Region' sqlite tables from the FinalProject.sqlite file.
# i.e. adds a country's region as the final column in the full table

import sqlite3

db = sqlite3.connect('FinalProject.sqlite')

cursor = db.cursor()

# Left outer join on the Full and Region tables
command = '''SELECT F.Country, F.Year, F.Population, F.PercentPopUsingInternet, F.HomicideCountper100k, F.HomicideRateper100k, F.PopChangeIndicator, F.InternetUseChangeIndicator, F.HomCountChangeIndicator, F.HomRateChangeIndicator, F.AvgChangePop, F.AvgChangeInternet, F.AvgChangeHomCount, F.AvgChangeHomRate, R.Region
             FROM Full F LEFT OUTER JOIN Region R ON F.country = R.Country;'''

cursor.execute(command)

# we want the output file to be saved as a .csv file
# so we may use it later for data mining
outfile = open('Full Table with Regions.csv', 'w')

# add column titles to output file
# (titles split among multiple lines here for visual clarity)
print('Country,Year,Population,Percent of Pop. Using Internet,Homicide Count per 100k,Homicide Rate per 100k,', end = "", file = outfile)
print('Pop. Change Indicator,Internet Use Change Indicator,Hom. Count Change Indicator,Hom. Rate Change Indicator,', end = "", file = outfile)
print('Avg. Change in Pop.,Avg. Change in Internet Use,Avg. Change in Hom. Count,Avg. Change in Hom. Rate,', end = "", file = outfile)
print('Region', file = outfile)

# print all attributes (separated by commas) of all rows to output file
for row in cursor:
    # loop through all attributes except last one so that we do not print extra comma at the end
    for n in range(len(row) - 1):
        print(row[n], end = ',', file = outfile)
    # print last attribbute without a comma after it
    print(row[len(row) - 1], file = outfile)

db.commit()
db.close()
outfile.close()
