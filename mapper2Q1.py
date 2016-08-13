#!/usr/bin/python

# Write a MapReduce program which will display the number of hits
# for each different file on the Web site.
# How many hits were made to the page
# /assets/js/the-associates.js

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data)==10:
        continue

    h,I,u,t,z,method,path,protocol,s,b = data
    t=t[1:]
    z=z[:-1]
    method=method[1:]
    protocol=protocol[:-1]
    if path=='/assets/js/the-associates.js':
        print "{0}\t{1}".format(path,1)

