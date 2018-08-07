# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:47:07 2017

@author: 1568925
"""

def c1():
    a, b = 0, 0
    move = []
    while True:
        move = input("Enter direction, distance (blank to exit input mode): ").split(",")
        if not move[0]:
            break
        signage = pow(-1, 'UDRL'.find(move[0][0].upper()))
        if move[0].upper() in ['UP','DOWN']:
            a += int(move[1]) * signage
        elif move[0].upper() in ['RIGHT','LEFT']:
            b += int(move[1]) * signage

    return "Net distance moved: " + str(round(pow(a**2 + b**2, 0.5)  ))

def c2():
    freq = {}
    inputs = input("Enter sentence: ").split(" ")
    for word in inputs:
        freq[word] = freq.get(word,0)+1
#    
#    for word in sorted(freq.keys()):
#        print(word + ':', freq[word])
    print(*("{}: {}".format(word, freq[word]) for word in sorted(freq.keys())), sep="\n")
    
def printLongest(s1,s2):
    if len(s1) == len(s2):
        print("Both are of same length")
    elif len(s1) > len(s2):
        print("Longer string:", s1)
    else:
        print("Longer string:", s2)

def printDict(num_range):
    print({x: x**2 for x in num_range})


def printList(num_range):
    print([x**2 for x in num_range])


def printTup(num_range):
    print(tuple(x**2 for x in num_range))

def tupleInTwo(t):
    print(t[:(len(t)//2)])
    print(t[(len(t)//2):])
    
def evensIn(t):
    print(list(x for x in t if x%2 == 0))

def YesorNo():
    s = input("Will you? ").upper()
    if s == 'YES':
        print(s)
    else:
        print("No")

def SqofEvens(i):
    print(list(map(lambda x: x**2, filter(lambda y: y %2 == 0, i))))

class Indian(object):
    
    def Nationality(self):
        print("Indian")

class Tamilan(Indian):
    pass

class Circle(object):
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        print ("Area is", 2*3.14*self.radius)

class Rect(object):
    def __init__(self,l,b):
        self.length = l
        self.breath = b
        
    def area(self):
        print("Area of this rectangle is", self.length * self.breath)


def lcm(x,y):
    z = max(x,y)
    while True:
        if z % x == 0 and z % y == 0:
            lcm = z
            break
        z += 1
    return lcm

def lcd(x,y):
    lcd = 1
    z = min(x,y)
    for i in range(2,z+1):
        if z % x == 0 and z % y == 0:
            lcd = z
            break
        z += 1
    return lcd

def SolveSimulEqs(x1,y1,s1,x2,y2,s2):
    ''' (6 int)->[2 int]
    Return the values of x and y axis that satisfies these equations:
        x1A + y1B = s1
        x2A + y2B = s2
        
    '''
#    lcm_x = lcm(x1, x2)
#    lcm_y = lcm(y1, y2)
    A = (-x2 * s1 + x1 * s2) / (-x2 * y1 + x1 * y2)
    B = (s1 - y1 * A) / x1
    return A, B
