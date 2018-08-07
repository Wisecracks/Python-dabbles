# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:33:24 2017

@author: SathyaSivam
"""


def py_challenge1():
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0:
            print('{},'.format(i)),


def py_challenge2(num):
    return reduce(lambda x, y: x*y, range(1, num+1))


def pc3(n):
    return {i: i*i for i in range(1, n+1)}

def pc4():
    l = raw_input("Enter list of numbers:").split(",")
    print(l)
    print(tuple(l))


def pc6():
    l = raw_input("Enter list of numbers:").split(",")
    for i in l:
        print('{}'.format(int(pow(2*50*float(i)/30, 0.5)))),


def pc7():
    input_str = raw_input("Enter dimensions:").split(',')
    output = []
    for i in range(int(input_str[0])):
#        lst = []
#        lst = [i*j for j in range(int(input_str[1]))]
        output.append([i*j for j in range(int(input_str[1]))])
#        for j in range(int(input_str[1])):
#            lst.append(i*j)
#        output.append(lst)
    return output


def pc8():
    input_str = raw_input("Enter comma-separated list:").split(",")
#    input_str.sort()
    return sorted(input_str)


def pc9():
    lines = ''
    while True:
        s = raw_input("Enter a sentence:")
        if s:
            lines += s.upper() + '\n'
        else:
            break
    return lines


def pc10():
    words = raw_input("Enter space-separated words:").split(" ")
    print(",".join(sorted(list(set(words)))))
