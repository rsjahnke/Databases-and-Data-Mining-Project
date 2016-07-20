# CodeToJoinTables.py
# Final Project
# CS 105
# 4/20/16

# joins the population, internet, and homicide data tables into one large
# table with information for every country. Rows are joined on country and
# year (therefore only coountries with information on population, internet,
# AND homicide are entered into final table).

# tables stored as sqlite files
import sqlite3

db = sqlite3.connect('FinalProject.sqlite')

cursor = db.cursor()

# join command
command = '''SELECT P.Country, P.Year, P.Population, I.Value, H.Count, H.Rate
             FROM Population P, Internet I, Homicide H
             WHERE P.Country = I.Country
               AND I.Country = H.Country
               AND P.Year = I.Year
               AND I.Year = H.Year
             ORDER BY P.Country, P.Year;'''

cursor.execute(command)

# we want our final table to be stored as a .csv file so we may use
# it later for data mining
outfile = open('Full Table.csv', 'w')

# print column titles in output file
print('Country,Year,Population,Percent of Pop. Using Internet,Homicide Count per 100k,Homicide Rate per 100k', file = outfile)

# print all attributes for each row
for line in cursor:
    print(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5], file = outfile)

# close and commit database and output file
db.commit()
db.close()
outfile.close()
