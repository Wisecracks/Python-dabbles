# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:53:19 2017

@author: 1568925
"""

def listParams(params):
    return ";".join("%s = %s" % (k,v) for k,v in params.items())

if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    print(listParams(myParams))