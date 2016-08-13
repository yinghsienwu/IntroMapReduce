#!/usr/bin/python

# Find the most popular file on the website: that is, the file whose path
# occurs most often in access_log. Your reducer should output the file's
# path and the number of times it appears in the log. 
# IMPORTANT: Some pathnames in the log begin with "http://www.the-associates.co.uk". 
# Be sure to remove the portion "http://www.the-associates.co.uk" from 
# pathnames in your mapper so that all occurrences of a file are counted together.


import sys

header="http://www.the-associates.co.uk"
n=len(header)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data)==10:
        continue

    h,I,u,t,z,method,path,protocol,s,b = data
    t=t[1:]
    z=z[:-1]
    method=method[1:]
    protocol=protocol[:-1]
    if path[:n]==header:
        path=path[n-1:]

    print "{0}\t{1}".format(path,1)

