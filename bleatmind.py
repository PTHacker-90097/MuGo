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
import resource

class yes:
    
    base = 2
    exponent = 1
    
    def __init__(self, b):
        self.base = b
    
    def get(self, e):
        return pow(self.base, e)



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
    
    return res




if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    
    # Get current soft and hard limits for virtual memory
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Syscall to raise the soft limit to the system's hard ceiling
    resource.setrlimit(resource.RLIMIT_AS, (hard, hard))
        
    pprint("Bleatmind say hello!")
    
    
    e = {}
    
    #We all know I was right to write the original pprint listed on this line, and also right to delete it from the internet.
    pprint("[Seeding numeric algorithm...]")
    inc = 2
    i = 2
    
    cap = (pow(10, 3) * 1) - 1
    
    pcap = pow(10, 2) #Max value of Q for N^Q
    
    rag = 3
    
    cooldown = 10
    restperiod = 5
    
    
    #blacklist = []
    
    vee = []
    
    nummy = None
    
    while inc <= cap:
        vee.clear()
        nummy = yes(inc)
        h = 0
        i = 3
       # while inc in blacklist:
         #   inc += 1
        
        e[inc] = [pow(inc, 2)]
        
        while i < pcap:
            h = nummy.get(i)
            e[inc].append(h)
            i += 1
        
        #e[inc] = vee
        if inc % cooldown == 0:
            #pprint(e[inc])
            #time.sleep(restperiod)
            print(f"Progress: {inc}/{cap}", end=" ", flush=True)
        inc += 1
        
    
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
                                for q in result:
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
                    for q in result:
                        prt = str(q)
                        if isprime(q):
                            prt += '*'
                        prt += ','
                        if not primeonly or isprime(q):
                            pprint(prt)
                                
        
        