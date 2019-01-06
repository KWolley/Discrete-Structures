# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def greedy_money(cents):
    """this function will use a greedyd algorith to make change using only quaters, 
    dimes and pennies (no nickels)"""
    q = 0;  # initialize place to store number of quaters needed
    d = 0;  # initialize place to store number of dimes needed
    p = 0;  # initialize place to store number of pennies needed
    # while cents > 25
    while (cents >= 25):
        q = q + 1;
        cents = cents - 25;
    # while cents > 10
    while (cents >= 10):
        d = d + 1;
        cents = cents - 10;
    # for the remainder of change required
    while (cents > 0):
        p  = p + 1;
        cents = cents - 1;
    print(" Quaters ", q);
    print(" Dimes ", d);
    print(" Pennies ", p);
    print( " Number of coins used ", q+d+p)

def greedy_money2(denoms,cents): 
    """ this function is right of the book"""
    num_coins = 0
    for i in range(0,len(denoms)):
        while (cents >= denoms[i]):
            num_coins = num_coins + 1
            cents = cents - denoms[i]
    return num_coins
    