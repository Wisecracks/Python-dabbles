#!/usr/bin/python
# "C:\Anaconda2\Python.exe" -r "$(FULL_CURRENT_PATH)"


total = 0  # This is global variable.
# Function definition is here


def sum(arg1, arg2):

    # Add both the parameters and return them
    # Here total is local variable
    total = arg1 + arg2
    print "Inside the function local total : ", total

# Now you can call sum function
sum(10, 20)
print "Outside the function global total : ", total
