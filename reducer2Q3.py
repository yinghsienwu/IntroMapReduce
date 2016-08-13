#!/usr/bin/python

import sys

oldKey=None
count=0
MaxCt=0
MaxKey=None
for line in sys.stdin:
    data_mapped=line.strip().split("\t")
    if len(data_mapped)!=2:
        continue
    
    thisKey,thisCount=data_mapped
    if oldKey and oldKey!=thisKey:
        if countTotal>=MaxCt:
            MaxCt=countTotal
            MaxKey=oldKey
        oldKey=thisKey
        countTotal=0

    oldKey=thisKey
    count+=int(thisCount)

if oldKey!=None:
    if countTotal>=MaxCt:
        MaxCt=countTotal
        MaxKey=oldKey


print "Most viewed website:\t",MaxKey
print "View count:\t",MaxCt
