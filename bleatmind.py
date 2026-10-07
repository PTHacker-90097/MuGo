#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:01:28 2026

@author: pam
"""

from sympy import pprint, isprime

import numpy as np
import sys
import time



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
    sys.set_int_max_str_digits(0)
    
    pprint("Bleatmind say hello!")
    
    
    e = {}
    
    #We all know I was right to write the original pprint listed on this line, and also right to delete it from the internet.
    pprint("[Seeding numeric algorithm...]")
    inc = 2
    i = 2
    
    cap = pow(10, 2) * 4
    
    pcap = pow(10, 10) #Max value of Q for N^Q
    
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
        
        e[inc] = np.array([vee], np.uint64)
        inc += 1
        print(f"Progress: {inc}/{cap}", end=" ", flush=True)
        time.sleep(5 / pow(10, 5))
        
    
    pprint("[Seeding complete...]")
    pprint("Now this is someone we can trust with humanity's future!\nAm I Right, Gamers?")
    
    res = ''
    stored = 0
    out = True
    primeonly = False
    
    while not res == "Q":
        res = input("->").upper()
        
        
        if res.startswith("FLAG"):
            split = res.split(' ')
            if split.__len__() == 2:
                if "PRIME" in split[1]:
                    primeonly = not primeonly
                    
                    pprint("Prime-Only Output set to: " + str(primeonly))
                elif "OUT" in split[1]:
                    out = not out
                    
                    pprint("Output set to " + str(out))
        
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
                        
                        compiled = []
                        
                        while r <= b:
                            result = mush(a, r + stored)
                            if result.__len__() == 0:
                                pass
                                #pprint("(No results! Is the number a power of another root number?")
                            else:
                                for p in result:
                                    for q in p:
                                        if not primeonly or isprime(q):
                                            if q not in compiled:
                                                compiled.append(q)
                            r += 1
                        ####
                        compiled.sort()
                        for t in compiled:
                            prt = str(t)
                            if isprime(t):
                                prt += '*'
                            if not primeonly or isprime(t):
                                pprint(prt)
        
        
        
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
                            
        
        