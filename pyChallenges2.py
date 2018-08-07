# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:53:49 2017

@author: 1568925
"""

from operator import itemgetter

def c1():
    input_str = input("Enter comma-separated binary numbers:").split(",")
#    for i in input_str:
#        if int(i) % 5 == 0:
#           input_str.remove(i)
#    return ",".join(map(str,input_str))
    print(",".join(map(str, (x for x in input_str if int(x) % 5 == 0))))


def c3():
    input_str = input("Enter sentence:")
    d = {"letters": 0, "digits": 0}
    for c in input_str:
        if c.isalpha():
            d["letters"] += 1
        elif c.isdigit():
            d["digits"] += 1
    print("Letters:", d["letters"])
    print("Digits:", d["digits"])


def c5(x):
    t = 0
    for i in range(1, 5):
        t += x * int('1'*i)
    print (t)


def c6():
    input_str = input("CSV numbers:").split(',')
    return ",".join(str(x) for x in input_str if int(x) % 2 != 0)


def c8():
    input_pwds = input("Enter passwords(csv):").split(',')
    valid_pwds = []
    for pwd in input_pwds:
        if len(pwd) > 5 and len(pwd) < 13:
            has_lowercase = False
            has_uppercase = False
            has_number = False
            has_special_char = False
            for char in pwd:
                if not has_lowercase and char.islower():
                    has_lowercase = True
                elif not has_uppercase and char.isupper():
                    has_uppercase = True
                elif not has_number and char.isdigit():
                    has_number = True
                elif not has_special_char and char in '$#@':
                    has_special_char = True
                else:
                    pass
            if has_lowercase and has_uppercase and has_number and has_special_char:
                    valid_pwds.append(pwd)
    return ",".join(valid_pwds)

                    
def c81():
    input_pwds = input("Enter passwords(csv):").split(',')
    valid_pwds = []
    for pwd in input_pwds:
        if len(pwd) > 5 and len(pwd) < 13 and \
        any(c.islower for c in pwd) and \
        any(c.isupper for c in pwd) and \
        any(c.isdigit for c in pwd) and \
        set('@#$').intersection(pwd):
            valid_pwds.append(pwd)
    return ",".join(valid_pwds)


def c82():
    pwd = input("Enter password to validate:")
    return_val = ''
    if len(pwd) < 5 or len(pwd) > 12:
        return_val = "Password should be between 5 to 12 characters long.\n"
#        continue
    if not any(c.islower() for c in pwd):
        return_val += "Password should have atleast 1 lowercase character.\n"
#        continue
    if not any(c.isupper() for c in pwd):
        return_val += "Password should have atleast 1 uppercase character.\n"
    if not any(c.isdigit() for c in pwd):
        return_val += "Password should have atleast 1 number.\n"
    if not set('@#$').intersection(pwd):
        return_val += "Password should have atleast 1 of these special characters: @#$."
    if return_val == '':
        return_val = "Password is valid!"
    print( return_val)


def c9():
    register = []
#    candidate = ''
    while True:
        candidate = input("Enter candidate info (blank to exit input mode): ")
        if not candidate:
            break
        register.append(tuple(candidate.split(",")))
    return sorted(register, key=itemgetter(0,1,2))

def c9():
    print("Duplicate def name!!")
    print(pwd)


    