#!/usr/bin/python

# Format of each line is:
# data\ttime\tstore name\titem description\tcost\tmethod of payment
#
# What is the total number of sales and the total sales
# value from all the stores? Assume there is only one reducer. 

import sys
ct=0
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data)==6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(1,cost)

