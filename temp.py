"""
Spyder Editor

This is a temporary script file.
"""
#import time

def is_valid_sequence(dna):
    """ (str)->str
    
    Validates if input is a valid DNA string returns if the input is valid or not.

    >>> is_valid_sequence("ABCD")
    u'ABCD is invalid sequence!!'
    >>> is_valid_sequence("GGATACGCAT")
    u'GGATACGCAT is a valid DNA sequence!!!'
    
    """
    i = 0
    for nucleotide in dna:
        if nucleotide not in 'ACGT':
            try:
                return dna.strip() + " is invalid sequence!!"
            except TypeError:
                return "Input is not a valid string literal!"
                
        i += 1
        
    return dna + " is a valid DNA sequence!!!"
    

def is_palindrome3(s):
#    t1 = time.time()    
    i = 0
    j = -1
    while i < len(s) // 2 and s[i] == s[j]:
        i += 1
        j -= 1
    
#   print('Half length = {},  i = {} and j = {}'.format(len(s)//2, i,j))
    print i == len(s) // 2
#    print (time.time() - t1 ) * 10000000

def is_palindrome4(s):
    '''
    >>> is_palindrome4('teliottopbardnotesputridtangemanatingissadIdassignitanamegnatdirtupsetondrabpottoilet')
    True
    '''
    i = 0
    while i < len(s) // 2 and s[i] == s[-i-1]:
        i += 1

    print i == len(s) // 2    
    
def sum_sq(r):    
    '''(list of int)->int
    >>> sum_sq(range(6))
    55
    '''    
    return sum(reduce(lambda x,y:x+y**2,r,0))    

def sum_cubes(r):    
    '''(list of int)->int
    '''
    return sum(reduce(lambda x,y:x+y**3,r,0))
    
def primes_between(x,y):
    for i in range(2,8):
        print( filter(lambda x: x == i or x % i, range(x,y+1)) )
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)