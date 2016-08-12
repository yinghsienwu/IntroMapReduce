#!/usr/bin/python

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

