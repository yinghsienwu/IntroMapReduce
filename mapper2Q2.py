#!/usr/bin/python

# Write a MapReduce program which determines the number of 
# hits to the site made by each different IP address. 
# How many hits were made by the IP address
# 10.99.99.186?

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
    if h=='10.99.99.186':
        print "{0}\t{1}".format(h,1)


