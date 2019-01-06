"""
Created on Sat Oct 13 20:06:39 2018

@author: karaw
"""
import math
import numpy as np

def div_alg(a,d):
    """this function will compute the quotient and modulo of a divided by d where
    # a is the dividend and d is the divisor 
    # input variables
        # a - integer
        # d - integer
    # output:
        # q,r - quotient and remainder of a / d
    # notes:
    # this function was adapted from pg 253 of Rosen K, Discrete Mathematics...
    """
    # initialization section
    q = 0  # set the value of the quotient to 0
    r = abs(a)  # set the value of the remainder to 0
    
    # while the greater than the divisor continue to subtract d and increment q
    while r >= d:
        r = r - d       # subtract d from r
        q = q + 1       # increment q
    if a < 0 and r > 0: # if a is negative and the remainder is > 0
        r = d - r       # adjust the remainder for the negative value of a
        q = -(q + 1)    # adjust q
    return (q,r)        # return quotient and remainder


def FME(b,n,m):
    """this function perform fast modular exponentiation of integers b to some power
    # mod some integer m
    # form is b^k mod m where k is the binary expansion of n
    # input variables:
        # b - integer base 
        # n - binary expantion of exponent b is raised to (k)
        # m - integer b is divided by
    # output:
        # r - remainder
    # notes:
    # this function was adapted from pg 254 of Rosen K, Discrete Mathematics...
    """
    # init section
    r = 1  # set initial remainder r
    power = b % m # calculate the first value of power, the b mod m
    
    # main section
    for i in range(0,len(n)):   # for every value of the binary expansion of the b^some exponent
        if n[i] == 1:           # if the binary value == 1
            r = (r * power) % m # change the value of r
        power = (power * power) % m # change the value of power
    return r # return the remainder

def Euclidean_Alg(a,b):
    # this function will calculate the greatest common divisor (gcd) of two integers
    # input variables
        # a - integer
        # b - integer
    # output:
        # gcd of a and b
    # notes:
    # this function was adapted from pg 269 of Rosen K, Discrete Mathematics...
    
    # init section
    x = a
    y = b
    
    # main section
    while y!=0:  # while y does not equal 0 
        r = x % y   # calc the remainder of x mod y
        x = y       # set x to y
        y = r       # set y to r
    return x        # return x - gcd of a,b

def Convert_Text(x):
    # this function will convert a string of letters into a list of ascii numbers 
    # input variables:
        # x - string of letters - ony standard letters and spaces are allowed
    # output:
        # n - vector of numbers that is the ascii representation of the string
    
    # init section
    n = [] # init vector to store ascii nums
    
    # main section
    for i in x: # for each element in x
        n.append(ord(i)) # append ascii number for character
    return n 

def Convert_Num(x):
    """this function will convert a list of ascii numbers into a string of letters
    # input variables:
        # x - vector of ascii numbers to be converted to string
    # output:
        # string of characters
    """
    # init section
    s = '' # init place to store characters
    
    # main section
    for i in range(0,len(x)):
        s = s + chr(x[i])
    return s

def Convert_Binary_String(x):
    """this function will convert an integer to binary digits
    # input variable:
        # x - integer
    # ouput:
        # string of the binary digits of the input integer
    # notes:
    # this function was adapted from project definintions
    """
    bin_list = [int(i) for i in list(bin(x)[2:])];
    return bin_list

def Find_Public_Key_e(p,q):
    """this function will calculate the public key (e) given two prime numbers
    # input variables:
    # p - prime integer
    # q - prime integer
    # output variables:
    # e - integer that is relatively prime to (p-1)(q-1)
    """
    # init section
    n = p*q             # calc
    pq = (p-1) * (q-1)  # calc 
    e = []  # initiate list to store possibles e's
    c = 2   # initiate counter
    while c < n:
        tmp_e = Euclidean_Alg(c,pq)             # calculate the gcd of e and pq
        if tmp_e == 1 and c != p and c != q:    # if e is relatively prime and != p or q
            e.append(c)                         # append int to e
        c = c + 1                               # incremnet counter
    return e[3]


def Ext_Eucl(a, b): 
    """this funtion will calculate the exteded euclideans algorithm
    # of two integers a and b
    # input variables
    # a - integer
    # b - integer
    # form a mod b
    # ouput
    # gcd - integer of the greatest common divisor of a and b
    # x - integer of the bezout coeff
    # y - integer of the bezout coeff

    # example: a mod b = 4 mod 9

    # Euclideans Algorithm for gcd is in the form
    # 9 = 2 * 4 + 1 9 = m, 2 = s, 4 = q , 1 = 4
    # 4 = 2 * 2 + 0
    # Ext. Eucl Alg
    # 1 = 9 – 2*4 1 = m, x = 9, s = 2, q = 4
    """
    # initialization section
    m,n = 0,0
    x,y = 0,1 # set variable to store Bezout coefficients
    s,t = 1, 0 # set variable for multiplier of Bezout coefficients
    # main section
    while a != 0:   # the program will terminate with the divisor is == 0
        q = b // a      # calc the quotient of b divided by a
        r = b % a       # calc the remainder of b divided by a
        m = x - s * q   # calc ext eucl of x
        n = y - t * q   # calc ext eucl of y
        # increment previously defined variables
        b,a,x,y = a,r,s,t # set new div to a, a to remainder,bez coeffs to multipliers
        s,t = m,n       # set multiplier to ext euc of x
    gcd = b         # once while loop is exited, gcd = b
    return gcd, x, y # return gcd and two Bezout coefficients x and y


def Find_Private_Key_d(e,p,q):
    """this function will calcualte the private key (d) using the Extended Euclidean
    # Algorithm
    # input variables:
    # e - integer -  public key
    # p - prime integer
    # q - prime integer
    # output:
    # d - integer of private key - inverse of e mod (p-1)(q-1)
    """
    pq = (p-1)*(q-1)
    gcd, d, bez2 = Ext_Eucl(e,pq)
    if gcd != 1:
        print('***WARNING: ', e, ',',p-1,'*',q-1, ' are not relatively prime.')
        return 0
    if d < 0:
        print('OUCH')
        d = pq - abs(d) % pq
    return d

def Encode(n,e,m):
    """this function will take a string and the public key and return a coded message
    # input variables:
    # m - string message to be encoded
    # pub_key - public key - in form [e,n]
    # output:
    # m_encoded - sring of coded message
    """
    # --- init section --- 
    c = []
    bin_e = Convert_Binary_String(e)
    # --- main section --- 
    # convert message to list of numbers
    for i in m:
        m_txt = Convert_Text(i)
        c.append(FME(m_txt[0],bin_e,n))
    return  c

def Decode(n,d,cipher_text):
    """this function will take the list of coded numbers, public key and private key
    # and return the decrypted message
    # input variables:
    # cipher_text - list of numbers
    # n - int of public key portion n
    # d - int of private key (d)
    # output
    # string of decoded message
    """
    # init section
    m = []
    bin_d = Convert_Binary_String(d)    
    bin_d = bin_d[::-1]
    for i in cipher_text:
        m.append(FME(i,bin_d,n))
    m = Convert_Num(m)
    return m

def test_code():
    """ this main function will perform the following:
    
    1. Asks the user to Get Keys, Encode or Decode.
    2. If Getting keys, it will need to ask for p and q. 
    3. If Encoding, it will need the message and public keys.
    3. If Decoding it will need the coded message, and public and private keys.
    """
    
    # ask user if encoding or decoding
    tmp = input('Would you like to encode or decode? (type e or d respectively): ')
    if tmp == 'e':
        keys = input('Do you need to get public and private keys? (type y/n):  ')
        if keys == 'y':
            p = int(input('please enter the integer of p: '))
            q = int(input('please enter the integer of q: '))
            n = p*q
            e = Find_Public_Key_e(p,q)
            d = Find_Private_Key_d(e,p,q)
        else:
            e = int(input('please enter integer of public key e: '))
            n = int(input('please enter integer of public key n: '))
        m = input('please enter srting to encode (do not include quotations): ')
        message = Encode(n,e,m)
        return n,e,d,message
    else:
        m = input('please enter ecoded message as list of integers: ')
        n = int(input('please enter public key n: '))
        d = int(input('p;ease enter private key d: '))
        
        message = Decode(n,d,m)
        return n,d,message
    
def factorize(n):
    # init storing factores
    all_factors = []
    # start with if the number n is even
    while n % 2 == 0:
        all_factors.append(2)
   
    for i in range(3,int(n),2):
        #print(i)
        while int(n) % i == 0: # while divisible by next odd int (3,5...)
            all_factors.append(i) # add to list
            n = n//i  # divide by i
    return np.unique(all_factors)
            
    
def break_codes(e,n,cipher_text):
    # find factors
    factors = factorize(n)
    print(factors)
    for i in range(0,len(factors)): # for each factor - p
        p = factors[i] 
        q = int(n/p)  # calculate q (n/p)
        d = int(Find_Private_Key_d(e,p,q)) # calculate d
        print(p,q,d,n)
        if d != 0: # if d != 0  
            m = Decode(n,d,cipher_text) # run decode with Decode(n,d,cipher_text)
            print(m)
            check = input('is this English? (y/n)')
            if check == 'y':
                return m
    return 'no solution found'
    
            
    
    
    
    
    
    
    
    
    
    
    