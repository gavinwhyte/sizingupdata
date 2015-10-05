__author__ = 'gavinwhyte'

import urllib2
import sys

import numpy as np

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)


# arrange the data into list for labels and list of list for attributes

xList=[]
labels =[]

for line in data:
    #split on comma
    row = line.strip().split(",")
    print row
    xList.append(row)

# Determine the number of rows and columns

# Dimensions of the Outer List
sys.stdout.write("Number of rows of Data " + str(len(xList)) + '\n')

# Dimension of the inner List[1] <- is the number of columns
sys.stdout.write("Number of columns of data = " + str(len(xList[1])) + '\n')


for line in data:
    row = line.strip().split(",")
    xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

# Determines the number of categorical variables and number of unique values for each

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0]*3

sys.stdout.write("Col " + '\t' + "Number" + '\t' + "Strings" + 't' + "Other\n")

iCol = 0

for types in colCounts:
    sys.stdout.write(str(iCol) + '\t\t' + str(types[0]) + '\t\t' + str(types[1]) +
                     '\t\t' + str(types[2]) + "\n")
    iCol += 1





