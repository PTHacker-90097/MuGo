# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 01:09:53 2026

@author: pam

Unused, left as-is out of dadaistic spite.
"""

from sympy import pprint, isprime

from bitarray import bitarray

import numpy as np


set1 = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        129,   
    ]


set2 = [
        4,
        6,
        8,
        9,
        10,
        12,
        14,
        15,
        16,
        18,
        20,
        21,
        22,
        24,
        25,
        26,
        27,
        28,
        30,
        32,
        33,
        34,
        35,
        36,
        38,
        39,
        40,
        42,
        44,
        45,
        46,
        48,
        49,
        50,
        51,
        52,
        54,
        55,
        56,
        57,
        58,
        60,
        62,
        63,
        64,
        65,
        66,
        68,
        69,
        70,
        72,
        74,
        75,
        76,
        77,
        78,
        80,
        81,
        82,
        84,
        85,
        86,
        87,
        88,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        98,
        99,
        100,
        102,
        104,
        105,
        106,
        108,
        109,
        110,
        111,
        112,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
        125,
        126,
        127,
        128,
        130
    ]

set3 = [
        0,
        1
    ]

def populate():
    for i in range(1024):
        if i >= 2:
            if isprime(i):
                set1.append(i)
            else:
                set2.append(i)
    set3[0] = 0
    set3[1] = 1


def func1():
    val = 0
    
    for i in range(13*10):
        #pprint("*Bleat* you")
        
        val += 1
        
    val = 0
    
    baa = bitarray()
    
    with open("munchslag.txt", "rb") as fi:
        baa.fromfile(fi)
        
        bits = baa.to01()
        
        pprint(baa.__len__())
        
        for i in range(baa.__len__()):
            
            bitstring = bits[i:i+10]
            #pprint(bitstring)
            
            if not bitstring.__len__() == 10:
                break
            
            val = int(bitstring, 2)
            
            flag = isprime(val)
            
            pprint(val)
            
            if flag:
                pval = set1.index(val)
                pprint("#### -> " + str(pval))
                
                fval = bitarray()
                
                while not pval <= 1:
                    if pval >= 2:
                        if pval in set1:
                            pval = set1.index(pval)
                            pprint("pval1 " + str(pval))
                            fval.append(0)
                        elif pval in set2:
                            pval = set2.index(pval)
                            pprint("pval2 " + str(pval))
                            fval.append(1)
                pprint("fval -> " + str(fval))
                
            elif val > 1:
                cval = set2.index(val)
                pprint("@@@@ -> " + str(cval))
                
                fval = bitarray()
                
                while not cval <= 1:
                    if cval >= 2:
                        if cval in set1:
                            cval = set1.index(cval)
                            pprint("cval1 " + str(cval))
                            fval.append(0)
                        elif cval in set2:
                            cval = set2.index(cval)
                            pprint("cval2 " + str(cval))
                            fval.append(1)
                pprint("fval -> " + str(fval))
        
        pprint("$$$$$$$$$$$$$$$$$$$$$$")
        pprint(baa)


if __name__ == "__main__":
    set1.clear()
    set2.clear()
    
    populate()
    
    pprint(set1)
    pprint(set2)
    pprint(set3)
    
    
    func1()
    