#!/usr/bin/python

import sys

oldKey=None
count=0
data={}
for line in sys.stdin:
    data_mapped=line.strip().split("\t")
    if len(data_mapped)!=2:
        continue
    
    thisKey,thisCount=data_mapped
    if oldKey and oldKey!=thisKey:
        data[oldKey]=count
        oldKey=thisKey
        countTotal=0
    oldKey=thisKey
    count+=int(thisCount)

if oldKey!=None:
    data[oldKey]=count

ct=data.values()
path=data.keys()
max_value=max(ct)
max_ind=ct.index(max_value)
print "Most viewed website:\t",path[max_ind]
print "View count:\t",max_value
