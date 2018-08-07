# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 13:43:24 2017

@author: Sathya Sivam
"""
from grades import *
import tkFileDialog as fd

# get the name of grades file and the file to write to
#f_grades = open(input("Name of file with grades: "),'r')
#f_gradeshisto = open(input("Create histogram in: "),"w")

f_grades = fd.askopenfile('r')
f_gradeshisto = fd.askopenfile('w')

#f_grades = open("stud_grades.txt",'w')
#f_gradeshisto = open("grades_histo.txt","w")

#mockup_grades(f_grades.name)
#f_grades.close()
#f_grades = open("stud_grades.txt",'r')

# from grdes file create a list of grades
grades = list_grades(f_grades)

# count the number of grades in each range
grade_counts = count_grades(grades)

# create histrogram file
create_histo(grade_counts,f_gradeshisto)

# close files
f_grades.close()
f_gradeshisto.close()

print('\n' + "************* Histogram of grades created ************** \n")
