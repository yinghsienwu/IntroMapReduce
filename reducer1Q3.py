#!/usr/bin/python

import sys

salesTotal=0
finalKey=0

for line in sys.stdin:
    data_mapped=line.strip().split("\t")
    if len(data_mapped)!=2:
        continue

    thisKey,thisSale=data_mapped
    salesTotal+=float(thisSale)
    finalKey+=float(thisKey)

print finalKey,"\t",salesTotal
