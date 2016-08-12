#!/usr/bin/python

import sys

oldKey=None
countTotal=0
for line in sys.stdin:
    data_mapped=line.strip().split("\t")
    if len(data_mapped)!=2:
        continue
    
    thisKey,thisCount=data_mapped
    if oldKey and oldKey!=thisKey:
        print oldKey,"\t",countTotal
        oldKey=thisKey
        countTotal=0
    oldKey=thisKey
    countTotal+=float(thisCount)

if oldKey!=None:
    print oldKey,"\t",countTotal
