# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:02:26 2018

@author: karaw
"""

def mod_exp(b,n,m):
    x = 1
    power = b % m
    print(power)
    for i in range(0,len(n)):
        if n[i] == 1:
            x = (x * power) % m
        power = (power * power) % m
        print(power)
    return x
    
            
def Find_Private_Key_d(b,m):
# this function will find the inverse of b mod m 
    
    # find gcd of b and m
    r = m % b         # calc the initial j -> the remainder of m / b
    #while r > 1:    # while j > 1
        # 

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y