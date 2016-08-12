#!/usr/bin/python

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

