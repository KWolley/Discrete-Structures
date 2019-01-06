"""
Created on Sat Oct 13 20:06:39 2018

@author: karaw
"""
import numpy as np
import pandas as pd
import pdb

def div_alg(a,d):
    # this function will compute the quotient and modulo of a divided by d where
    # a is the dividend and d is the divisor 
    # input variables
        # a - integer
        # d - integer
    # output:
        # q,r - quotient and remainder of a / d
    # notes:
    # this function was adapted from pg 253 of Rosen K, Discrete Mathematics...
    
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
    # this function perform fast modular exponentiation of integers b to some power
    # mod some integer m
    # form is b^k mod m 
    # input variables:
        # b - integer base 
        # n - binary expantion of exponent b is raised to (k)
        # m - integer b is divided by
    # output:
        # r - remainder
    # notes:
    # this function was adapted from pg 254 of Rosen K, Discrete Mathematics...
    
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
    # this function will convert a list of ascii numbers into a string of letters
    # input variables:
        # x - vector of ascii numbers to be converted to string
    # output:
        # string of characters
    
    # init section
    s = "" # init place to store characters
    
    # main section
    for i in range(0,len(x)):
        s = s + chr(x[i])
    return s

def Convert_Binary_String(x):
    # this function will convert an integer to binary digits
    # input variable:
        # a - integere
    # ouput:
        # string of the binary digits of the input integer
    # notes:
    # this function was adapted from project definintions
    return str(int(bin(x)[2:]))

def Find_Public_Key_e(p,q):
    # this function will calculate the public key (e) given two prime numbers
    # input variables:
    # p - prime integer
    # q - prime integer
    # output variables:
    # e - integer that is relatively prime to (p-1)(q-1)
    
    # init section
    n = p*q
    pq = (p-1) * (q-1) 
    
    e = []
    t = 2
    while t < n:
        tmp_e = Euclidean_Alg(t,pq) # calculate the gcd of e and pq
        if tmp_e == 1 and t != p and t != q: # if e is relatively prime and != to p and q
            e.append(t)
        t = t + 1
    return e

def Ext_Eucl(a, b): # this funtion will calculate the exteded euclideans algorithm
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
    # this function will calcualte the private key (d) using the Extended Euclidean
    # Algorithm
    # input variables:
    # e - integer -  public key
    # p - prime integer
    # q - prime integer
    # output:
    # d - integer of private key - inverse of e mod (p-1)(q-1)
    pq = (p-1)*(q-1)
    gcd, d, bez2 = Ext_Eucl(e,pq)
    if gcd != 1:
        print('***WARNING: ', e, ',',p-1,'*',q-1, ' are not relatively prime.')
        return 0
    return d

def Encode(m,pubkey):
    # this function will take a string and the public key and return a coded message
    # input variables:
    # m - string message to be encoded
    # pubkey - public key. the public key must 
    # output:
    # m_encoded - sring of coded message
    
    # --- init section --- 
    # none
    
    # --- main section --- 
    # convert message to list of numbers
    m_txt = Convert_Text(m)
    # convert list of numbers to binary string
    m_str = Convert_Binary_String(m_txt)
    
    # perform fast modular exponentiation of the public key and binary form of message
    m_encoded = FME(pubkey[0],m_str,pubkey[1])
    return  m_encoded

def Decode():
    # this function will take the list of coded numbers, public key and private key
    # and return the decrypted message
    # input variables:
    # x - list of numbers
    # pub_key - vec or public key
    # priv_key - vec of private key
    return
    
    
    
    
    
    
    
    