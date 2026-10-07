#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:01:28 2026

@author: pam
"""

from sympy import pprint, isprime
from pathlib import Path

import numpy as np
import sys
import time
import resource
import array

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

TABLE_DIR = "tables/"


e = None

def load_huge_ints_from_bin(filename: str) -> list[int]: #Method code by AI
    results = []
    with open(filename, "rb") as f:
        while True:
            # Read 2-byte length header
            header = f.read(2)
            if not header:
                break  # End of file
            
            byte_len = int.from_bytes(header, byteorder="big")
            
            # Read exact integer bytes
            num_bytes = f.read(byte_len)
            num = int.from_bytes(num_bytes, byteorder="big")
            results.append(num)
            
    return results

def load_base_on_demand(base: int) -> list[int]:#Method code by AI
    """
    Reads a single base binary file on demand.
    Returns a list of arbitrary-precision integers.
    """
    file_path = TABLE_DIR / f"base_{base:03d}.bin"
    
    if not file_path.exists():
        raise FileNotFoundError(f"Binary table for base {base} not found at {file_path}")

    integers = []
    with open(file_path, "rb") as f:
        while True:
            # Read 2-byte length header
            header = f.read(2)
            if not header:
                break  # Reached EOF
            
            byte_len = int.from_bytes(header, byteorder="big")
            num_bytes = f.read(byte_len)
            integers.append(int.from_bytes(num_bytes, byteorder="big"))
            
    return integers


def mush(i, j):
    res = []
    
    for N in e[i]:
        r = N
        res.append(r + j)
    
    return res


def seed(cap, pcap):
    e.clear()
    pprint("[Seeding numeric algorithm...]")
    inc = 2
    i = 2
    rag = 3
    
    cooldown = 10
    restperiod = 5
    
    
    #blacklist = []
    nummy = None
    
    while inc <= cap:
        nummy = yes(inc)
        h = 0
        i = 3
        
        
        e[inc] = [pow(inc, 2)]
        
        while i < pcap:
            h = nummy.get(i)
            e[inc].append(h)
            i += 1
        if inc % cooldown == 0:
            #pprint(e[inc])
            #time.sleep(restperiod)
            print(f"Progress: {inc}/{cap}", end=" ", flush=True)
        inc += 1
        
    
    pprint("[Seeding complete...]")

def bleatgeometry(size, sets, start, end):
    candidates = []
    lq = []
    
    result = []
    
    counter = start
    
    while counter < end:
        
        lq.clear()
        candidates.clear()
        
        for i in range(size):
            candidates.append(0)
        
        for i in range(size):
            lq.append(0)
        
        for i in range(candidates.__len__()):
            candidates[i] = e[sets[i]]
        #pprint(candidates)
        
        v = 0
        
        for q in candidates:
            for p in lq:
                for i in range(size):
                    v = (q[i] + p)
                    if not v in result:
                        result.append(v)
            lq = q
        
        counter += 1
        
    result.sort()
    return result


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    
    # Get current soft and hard limits for virtual memory
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Syscall to raise the soft limit to the system's hard ceiling
    resource.setrlimit(resource.RLIMIT_AS, (hard, hard))
        
    pprint("Bleatmind say hello!")
    
    
    e = {}
    
    #We all know I was right to write the original pprint listed on this line, and also right to delete it from the internet.
    pprint("Now this is someone we can trust with humanity's future!\nAm I Right, Gamers?")
    
    res = ''
    stored = 0
    out = True
    primeonly = False
    
    while not res == "Q":
        res = input("->").upper()
        
        if res.startswith("GEOM"):
            split = res.split(' ')
            if split.__len__() >= 2:
                rlow = int(split[1])
                rhigh = int(split[2])
                
                cands = []
                
                for i in range(split.__len__()-2):
                    cands.append(int(split[i+2]))
                
                ree = bleatgeometry(cands.__len__()-1, cands, rlow, rhigh)
                
                pprint("RESULTS FOUND")
                for q in ree:
                    prt = str(q)
                    if isprime(q):
                        prt += '*'
                    prt += ','
                    if not primeonly or isprime(q):
                        pprint(prt)
        
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
        
        if res == ('SAV'): #Saving code by AI
            for q in e.keys():
                with open(TABLE_DIR + "/p_" + str(q) + ".bin", "wb") as f:
                        v = e[q]
                        for num in v:
                            # Determine how many bytes are needed for this specific integer
                            byte_len = (num.bit_length() + 7) // 8
                            
                            # Write 2-byte header (length of integer) + raw integer bytes
                            f.write(byte_len.to_bytes(2, byteorder="big"))
                            f.write(num.to_bytes(byte_len, byteorder="big"))
        ##########################
        
        if res.startswith("SEED"):
            split = res.split(" ")
            pprint(split)
            if split.__len__() >= 2:
                if split[1].isnumeric() and split[2].isnumeric():
                    cap = int(split[1])
                    pcap = int(split[2])
                    
                    seed(cap, pcap)
        
        if res == ('TABLE'): #Command created with AI assistance
            # Count only .bin files
            bin_count = len(list(Path(TABLE_DIR).glob("*.bin")))
            
            print(f"Total .bin files: {bin_count}")
            
            for i in range(bin_count):
                if i >= 2:
                    e[i] = load_huge_ints_from_bin(TABLE_DIR + "/p_" + str(i) + ".bin")
        ##################
        
        if res.startswith("LD"): #Take a peek in a .bin file
            split = res.split(' ')
            if split.__len__() > 1 and split[1].isnumeric():
                ree = load_huge_ints_from_bin("tables/p_" + split[1] + ".bin")
                pprint(ree)
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
                                
        
        