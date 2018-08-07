# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:59:36 2018

@author: 1568925
"""

# This is shorthand and not friendly with memory on very large files, but it works.

splitLen = 1000000         # lines per file
filePath = "C:/Users/1568925/Documents/Projects/Nostro Remediation/SIT/"
inputFile = "EDMP_FINETL_NAMS_IN_20180531.dat"
outputFileBase = 'EDMP_FINETL_NAMS_IN_20180531_' # output1.txt, output2.txt, etc.


input = open(filePath + inputFile, 'r').read().split('\n')

at = 1

for lines in range(0, len(input), splitLen):

    # Open the output file, add header, write block of lines and close it
    output = open(filePath + outputFileBase + str(at) + '.dat', 'w')
    if at > 1: output.write(input[0] + '\n')
    output.write('\n'.join(input[lines:lines+splitLen]))
output.close()

    # Increment the counter
    at += 1