#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:01:28 2026

@author: pam
"""

from sympy import pprint, isprime, root
from pathlib import Path
from datetime import datetime

import numpy as np
import sys
import time
import resource
import array

class yes:
    
    base = 2
    exponent = False
    primality = False
    queen = False
    lineage = None
    
    
    def __init__(self, b, e, p, l):
        self.base = b
        
        if e:#Sanity check
            p = False
        
        self.exponent = e
        self.primality = p
        self.lineage = l
        self.queen = e.exponent == 1
    
    def get(self, e):
        return pow(self.base, e)



# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets formatting back to default

TABLE_DIR = "tables/"

DEV = {
       "PRIME": True,
       "OUT": False
      }


e = None


def loadtable():
    # Count only .bin files
    bin_count = len(list(Path(TABLE_DIR).glob("*.bin")))
    
    print(f"Total .bin files: {bin_count}")
    
    for i in range(bin_count):
        if i >= 2:
            e[i] = load_huge_ints_from_bin(TABLE_DIR + "/p_" + str(i) + ".bin")

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
        pflag = primelitmus(inc)
        nummy = yes(inc, 1, pflag, inc)
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

def bleatfrag(ia, ib, mres, fine=False):
    results = []
    
    aa = e[ia]
    ab = e[ib]
    
    cres = 0
    
    for a in aa:
        for b in ab:
            c = a + b
            if not c in results:
                results.append(c)
                c += a
                c += b
                c -= 1
                if not c in results:
                    results.append(c)
            if fine:
                c = a // b
                if not c in results:
                    results.append(c)
                    c = pow(c, 2)
                    if not c in results:
                        results.append(c)
            cres += 1
            if cres >= mres:
                break
        cres = 0
    results.sort()
    return results


ltms = []

def primelitmus(cand) -> bool:
    flag = True
    
    cap = 17 + (cand // 100)
    
    for k in e:
        if k[0].primality:
            l = k[0]
            if l % cand == 0:
                flag = False
            if l > cap:
                break
    
    if flag:
        flag = isprime(cand)
    
    return flag

def countlineage(finality):
    e["PRIME"] = []
    e["COMPO"] = []
    
    counter = 2
    
    while counter <= finality:
        while primelitmus(counter):
            e["PRIME"].append(counter)
            counter += 1
        e["COMPO"].append(counter)
        counter += 1
    

def printselect(ef, cmd):
    
    pprint(ef)
    
    if DEV["OUT"]:#Print to console, not a file
        for q in ef:
            prt = str(q)
            if primelitmus(q):
                prt += '*'
            prt += ','
            if DEV["PRIME"] and primelitmus(q):
                pprint(prt)
            elif not DEV["PRIME"]:
                pprint(prt)
    else:
        with open("output/printedcommand_" + str(datetime.now()) + ".txt", "w") as f:
            for q in ef:
                prt = str(q)
                if primelitmus(q):
                    prt += '*'
                prt += ','
                if DEV["PRIME"] and primelitmus(q):
                    print(prt, file=f)
                elif not DEV["PRIME"]:
                    pprint(prt, file=f)
            print("###############", file=f)
            print("Command Used:", file=f)
            print(cmd, file=f)


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    
    # Get current soft and hard limits for virtual memory
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Syscall to raise the soft limit to the system's hard ceiling
    resource.setrlimit(resource.RLIMIT_AS, (hard, hard))
    
    e = {}
    
    pprint("Bleatmind say hello!")
    
    #loadtable()
    
    pprint("Now this is someone we can trust with humanity's future!\nAm I Right, Gamers?")
    
    res = ''
    stored = 0
    
    while not res == "Q":
        res = input("->").upper()
        
        cmdstart = datetime.now()
        
        if res.startswith("FRAG"):
            split = res.split(' ')
            if split.__len__() > 3:
                ree = bleatfrag(int(split[1]), int(split[2]), int(split[3]))
                printselect(ree, res)
                
        
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
                printselect(ree, res)
        ########
        
        
        if res.startswith("FLAG"):
            split = res.split(' ')
            if split.__len__() == 2:
                    DEV[split[1]] = not DEV[split[1]]
                    pprint("Prime-Only Output set to: " + str(DEV[split[1]]))
        ##########################
        if res.startswith('SET'):
            split = res.split(' ')
        ####
            if split[1].isnumeric():
                stored = int(split[1])
            ####
                if DEV["OUT"]:
                    pprint(f"{BLUE}Set storage to " + str(stored) + f"{RESET}")
                ####
        if res == ('SAV'): #Saving code by AI
        ####    
            for q in e.keys():
            #### 
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
        ############
        if res == ('TABLE'): #Command created with AI assistance
            loadtable()
        ##################
        if res.startswith("LD"): #Take a peek in a .bin file
            split = res.split(' ')
            if split.__len__() > 1 and split[1].isnumeric():
                ree = load_huge_ints_from_bin("tables/p_" + split[1] + ".bin")
                pprint(ree)
        ##########################
        if res.startswith("LINEAGECALC"):
            split = res.split(' ')
            if split.__len__() >= 2:
                pprint(split[1])
                countlineage(int(split[1]))
                with open(TABLE_DIR + "/LIN_PRIME.bin", "wb") as f:
                        v = e["PRIME"]
                        for nun in v:
                            # Determine how many bytes are needed for this specific integer
                            byte_len = (nun.bit_length() + 7) // 8
                            
                            # Write 2-byte header (length of integer) + raw integer bytes
                            f.write(byte_len.to_bytes(2, byteorder="big"))
                            f.write(nun.to_bytes(byte_len, byteorder="big"))
                        w = e["COMPO"]
                with open(TABLE_DIR + "/LIN_COMPO.bin", "wb") as g:
                        for num in w:
                            # Determine how many bytes are needed for this specific integer
                            byte_len = (num.bit_length() + 7) // 8
                            
                            # Write 2-byte header (length of integer) + raw integer bytes
                            g.write(byte_len.to_bytes(2, byteorder="big"))
                            g.write(num.to_bytes(byte_len, byteorder="big"))
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
                                    if DEV["PRIME"] and primelitmus(q):
                                        if q not in compiled:
                                            compiled.append(q)
                                    elif not DEV["PRIME"]:
                                        if q not in compiled:
                                            compiled.append(q)
                            r += 1
                        ####
                        compiled.sort()
                        printselect(compiled, res)
        ########################
        if res.isnumeric():
            ree = mush(int(res), stored)
            pprint("RESULTS FOUND")
            printselect(ree, res)
        ###########################
        ###########################
        ###########################
        ###########################
        ###########################
        pprint("Completed command in:")
        pprint(datetime.now() - cmdstart)
                                
        
        