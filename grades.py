# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 13:43:00 2017

@author: Sathya Sivam
"""
import random

def list_grades(f_grades):
    ''' (grades file) -> list of float
        
    Return the grades present in input file as list of grades

    >>>get_grades(f_grades)
    [78.5, 81, 66.5, 45, 20, 99, 100, 89, 99]
    '''
    grades = []

    for line in f_grades:
        if line != '':
            start = line.find(' ')
            grade = line[start+1:]
            if grade != 'Grade':
                grades.append(float(grade))
                
    return grades
    
def count_grades(grades):
    '''(list of float)->list of int
    
    Return the count of grades in 10 marks range
    >>>count_grades(grades)
    [0, 0, 1, 0, 1, 0, 1, 1, 2, 2, 1]
    '''
    grade_count = map(lambda x: x*0, range(11))
    for grade in grades:
        range_index = grade // 10
        grade_count[int(range_index)] += 1
        
    return grade_count
    
def create_histo(grade_counts, f_gradeshisto):
    '''(list of int, output file)->NoneType
    
    Create histogram in output file based on list of grades count.
    
    >>>create_histo(grade_counts)
     0-09: 
    10-19:
    20-29: *
    :
    :
    80-89: **
    90-99: **
      100: *
    '''
#    f_gradeshisto.write(' 0-09: ')
#    f_gradeshisto.write('*' * grade_counts[0] + '\n')
    
    for i in range(10):
        low = i*10
#        f_gradeshisto.write(str(low) + '-' + str(low+9) + ': ')
        f_gradeshisto.write('{:02d}-{:02d}: '.format(low, low+9))
        f_gradeshisto.write('*' * grade_counts[i] + '\n')

    f_gradeshisto.write('  100: ')
    f_gradeshisto.write('*' * grade_counts[10] + '\n')
    
def mockup_grades(f_studgrades):
    '''(grades file)->Nonetype
    
    Mocksup grades and writes them to grades file.
    >>>mockup_grades(f_grades)
    None
    '''
    f_studgrades.truncate(0)
    for i in range(100):
        f_studgrades.write('{:04d} {:06.2f}\n'.format(i,random.random()*100))