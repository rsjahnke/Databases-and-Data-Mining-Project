# CodeToAdd_Indicators_Averages.py
# Final Project
# CS 105
# 4/19/16

# Reads in a .csv file containing a table with information on countries
# and their population size, percent of population using the internet,
# homicide count per 100k people, and homicide rate per 100k people
# per year, for years from 1990 - 2014. (Not all countries have information
# for all years). For each row in the table, this program calculates the
# difference in population, internet use, and homicide count/rate between
# each row and the row before it. If the population/internet use/homicide
# increases, an indicator variable of 1 is assigned to the appropriate
# indicator variable for the row. If the attribute deccreases, -1 is
# assigned to the indicator. If there is no change, 0 is assigned to the
# indicator. Then, for each row in the table, the program calculates the
# average change of each  attribute per year. (The average change is
# calculated instead of the raw change from row to row because not all
# coutries have information for each sequential year. i.e. For some
# countries, sequential rows on the table do not have information for
# sequential years. An average is taken to normalize the change in each
# attribute.)

infile = open('Full Table.csv', 'r')
outfile = open('Full Table with Indicators.csv', 'w')

# skip over columns titles in input file
infile.readline()

# add previous column titles to output file
print('Country,Year,Population,Percent of Pop. Using Internet,Homicide Count per 100k,Homicide Rate per 100k,', end = "", file = outfile)
# add new column titles to output file
# (indictor columns to indicate increase/decrease)
# (average columns to indicate average change in attribute PER YEAR)
# we are adding indicator and average variables for our data mining processes
print('Pop. Change Indicator,Internet Use Change Indicator,Hom. Count Change Indicator,Hom. Rate Change Indicator,Avg. Change in Pop.,Avg. Change in Internet Use,Avg. Change in Hom. Count,Avg. Change in Hom. Rate', file = outfile)

# initialize indicator variables
pop_indicator = 0
internet_indicator = 0
homCount_indicator = 0
homRate_indicator = 0

# initialize average variables
avgPopChange = 0
avgInternetChange = 0
avgHomCountChange = 0
avgHomRateChange = 0

# We will calculate increase/decrease and average by making pairwise
# comparisons of rows.
# We read in the first line of the file to make the first comparison, then
# for every comparison thereafter, we loop through all rows of the file
line1 = infile.readline()
# the SQL command to join tables left extraneous quotation marks around
# every value, so we trim the line to remove the quotation marks (and
# the newline character)
line1 = line1[:-1]
# we trim internal (extraneous) quotation marks by splitting the line at
# both the comma and the quotation marks
components1 = line1.split(',')

# loop through all rows of table to make pairwise comparisons
for line in infile:
    # trim outer quotation marks
    line = line[:-1]
    # split line and trim inner quotation marks
    components2 = line.split(',')
    # test to make sure we are comparing rows of the same country
    if components1[0] == components2[0]:
        yeardiff = int(components2[1]) - int(components1[1])
        # test to make sure we are not looking at repeat years
        # (there are repeat years in the original file)
        if yeardiff != 0:
            # calculate the change in each attribute
            popdiff = float(components2[2]) - float(components1[2])
            internetdiff = float(components2[3]) - float(components1[3])
            homCountDiff = float(components2[4]) - float(components1[4])
            homRateDiff = float(components2[5]) - float(components1[5])
            # determine whether there was an increase, decrease, or no
            # change and assign proper indicator.
            # change in population:
            if popdiff > 0:
                pop_indicator = 1
            elif popdiff == 0:
                pop_indicator = 0
            else:
                pop_indicator = -1
            # change in internet use:
            if internetdiff > 0:
                internet_indicator = 1
            elif internetdiff == 0:
                internet_indicator = 0
            else:
                internet_indicator = -1
            # change in homicide count per 100k people
            if homCountDiff > 0:
                homCount_indicator = 1
            elif homCountDiff == 0:
                homCount_indicator = 0
            else:
                homCount_indicator = -1
            # change in homicide rate per 100k people
            if homRateDiff > 0:
                homRate_indicator = 1
            elif homRateDiff == 0:
                homRate_indicator = 0
            else:
                homRate_indicator = -1
            # calculate average change in each attribute per year
            avgPopChange = popdiff / yeardiff
            avgInternetChange = internetdiff / yeardiff
            avgHomCountChange = homCountDiff / yeardiff
            avgHomRateChange = homRateDiff / yeardiff
            # create complete array with all components
            newComponents = components2 + [str(pop_indicator), str(internet_indicator), str(homCount_indicator), str(homRate_indicator), str(avgPopChange), str(avgInternetChange), str(avgHomCountChange), str(avgHomRateChange)]
            # join  new components into single line
            newline = ','.join(newComponents)
            # print full row with all attribute to output file
            print(newline, file = outfile)
    # assign 2nd comparator to 1st comparison variable to continue the
    # process of pairwise comparisons
    components1 = components2

infile.close()
outfile.close()
