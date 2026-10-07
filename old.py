#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:01:28 2026

@author: pam

A backup before I admitted a git repository was a good idea for this one
"""

from sympy import pprint, isprime

import numpy as np



# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets formatting back to default


e = None


def mush(i, j):
    res = []
    
    for N in e[i]:
        r = N
        res.append(r + j)
    
    return np.array(res, np.int32)




if __name__ == "__main__":
    pprint("Bitbleat say hello!")
    
    e = {}
    inc = 2
    i = 2
    
    cap = 10000 * 3
    
    pcap = pow(10, 9)#Max value for a power of N
    
    rag = 3
    
    blacklist = []
    
    while inc <= cap:
        vee = []
        r = inc
        i = 2
        
        while r <= pcap:
            if not r in blacklist:
                vee.append(r)
                blacklist.append(r)
            r = inc**(i)
            i += 1
        
        e[inc] = np.array([vee], np.int32)
        inc += 1
    
    pprint("[Seeding complete...]")
    pprint("Now this is someone we can trust with humanity's future!\nAm I Right, Gamers?")
    
    res = ''
    stored = 0
    out = True
    primeonly = True
    
    while not res == "Q":
        res = input("->").upper()
        
        
        
        ##########################
        if res.startswith('SET'):
            split = res.split(' ')
            if split[1].isnumeric():
                stored = int(split[1])
                
                if out:
                    pprint(f"{BLUE}Set storage to " + str(stored) + f"{RESET}")
        
        
        ##########################
        if res.startswith("LOOP"):
            split = res.split(' ')
            if split.__len__() >= 2:
                if split[1].isnumeric():
                    if split[2].isnumeric():
                        a = int(split[1])
                        b = int(split[2])
                        
                        r = a
                        
                        while r <= b:
                            result = mush(a, r + stored)
                            if result.__len__() == 0:
                                pass
                                #pprint("(No results! Is the number a power of another root number?")
                            else:
                                for p in result:
                                    for q in p:
                                        prt = str(q)
                                        if isprime(q):
                                            prt += '*'
                                        if not primeonly or isprime(q):
                                            pprint(prt)
                            r += 1
        
        
        
        
        ########################
        if res.isnumeric():
            result = mush(int(res), stored)
            
            if out:
                if result.__len__() == 0:
                    pprint("(No results! Is the number a power of another root number?")
                else:
                    pprint("RESULTS FOUND")
                    for p in result:
                        for q in p:
                            prt = str(q)
                            if isprime(q):
                                prt += '*'
                            if not primeonly or isprime(q):
                                pprint(prt)
                        
        
        