# CodeToCleanPop.py
# Final Project
# CS 105
# 4/18/16

# reads .csv files containing UN database info about population sizes of countries
# around the world from ~1960 - 2014. Extracts population totals from 1990 - 2014
# and writes them to a new file

# edits to original UN database files before opening files in program:
# footnotes deleted from end of original files,
# footnote values column deleted (to ensure population number in last column),
# year column moved to index -2

# all input files
# (multiple input files needed to download all data -- UN database
# website only allows us to download 100,000 lines at a time)
a = open('popA.csv', 'r')
b1 = open('popB1.csv', 'r')
b2 = open('popB2.csv', 'r')
c1 = open('popC1.csv', 'r')
c2 = open('popC2.csv', 'r')
d = open('popD.csv', 'r')
e = open('popE.csv', 'r')
f = open('popF.csv', 'r')
g = open('popG.csv', 'r')
h = open('popH.csv', 'r')
i = open('popI.csv', 'r')
jk = open('popJK.csv', 'r')
l = open('popL.csv', 'r')
m = open('popM.csv', 'r')
n = open('popM.csv', 'r')
o = open('popO.csv', 'r')
pq = open('popPQ.csv', 'r')
r = open('popR.csv', 'r')
s1 = open('popS1.csv', 'r')
s2 = open('popS2.csv', 'r')
t = open('popT.csv', 'r')
uvwyz = open('popUVWYZ.csv', 'r')

# join all input file handles into an array
fileArray = [a, b1, b2, c1, c2, d, e, f, g, h, i, jk, l, m, n, o, pq, r, s1, s2, t, uvwyz]

# open output file
outfile = open('CLEANED POPULATION.csv', 'w')

# print column titles to output file
# these are the attributes selected from input files to print to new file
print("Country, Year, Population", file = outfile)

# we want to process every row in every input file, so we loop through the file array
for file in fileArray:
    # skip over column titles in input file
    file.readline()
    for line in file:
        line = line[:-1] # strip newline character
        components = line.split(',')
        # input files contain A LOT of data, we only want TOTAL population for years >= 1990
        if int(components[-2]) >= 1990 and components[1] == "Total" and components[2] == "Both Sexes" and components[3] == "Total":
            newline = ','.join([components[0], components[-2], components[-1]])
            print(newline, file = outfile)

# close all input files
for file in fileArray:
    file.close()
    
# close output file
outfile.close()
