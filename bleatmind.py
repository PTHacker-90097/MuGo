#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:01:28 2026

@author: pam

"""

from bleattodisc import TeeStdout

from sympy import pprint, isprime, symbols, sympify, solve
from pathlib import Path

from datetime import datetime

import multiprocessing as mp
import numpy as np
import sys
import time
import resource
import array

class yes:
    
    base = 2
    val = ''
    
    def __init__(self, b):
        self.base = b
    
    def exp(self, e):
        return kung(self.base, e)
    
    def get(self):
        res = 0
        ctr = 8
        for c in self.val:
            if c != '0':
               res += kung(self.base, ctr)
            ctr -= 1
        return res
    
    def AND(self, otherself) -> int:
        t = 0
        
        ctr = 0
        for c in self.val:
            if c == '1':
                t += kung(self.base, ctr)
        ctr = 0
        for c in otherself.val:
            if c == '1':
                t += kung(otherself.base, ctr)
        
        return t


# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets formatting back to default

TABLE_DIR = "tables/"

DEV = {
        "PRIME" : True,
        "OUT"   : True,
        "VBINAI": True, #"Verbose" Binai flag
        "OPRIME": True # "Output" Primes flag
}

FOUND_PRIMES = [
        1 , 2 , 3 , 5 , 7
    ]

STORAGE = {
        "LOOP"  : 0,
        "LCHAIM": 0,
        "BINAI" : 0,
    }

TOFILEOUT = None

NUM_CORES = mp.cpu_count()#@
PROCESSES = []#@


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

def load_base_on_demand(base: int) -> list[int]:
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

'''
This method brought to you by mathematical spite.
Why does (2 ^ 2) == ( 2 * (2) ) == (4) ?
This confuses even the very wise.

To call forth an operation at all is to agree something is happening;

(2 ^ 1) == (2 * 1) == (2) is pure lunacy.
(2 ^ 0) == (2 / 2) == (1) ...

?????????

We've been had.

kung(2, 1) == (2 * ('two, one time')) == (2 * 2) == (4)

Now that's better!

Mostly because we can just say, "Two to the first power is equal to two times itself"
Then, kung(2, 2) == (8) == (2 * 2 * 2)

In the last example, we call forth an operation twice upon the first subject, or 'argument'

See Also:

kung(7, 2) == (7) * ( (7) * (7) ) == (7 * 49) == (343)

This is relevant for set theory as it pertains to symmetry within input & output, and interrelation of numbers across large scales.


And yes, 'kung' as an alternative to 'pow' because it's one of my favorite dishes.
'''
def kung(v, e, pao=pow(10, 10)):
    v = int(v)
    e = int(e)
    try:
        return pow(v, e+1, mod=pao)
    except ValueError:
        return -1



def binai(args, verbose=True):
    #Size (In bits) of values
    sz = kung(2, int(args[1]))
    #inc = int(args[2])
    
    nums = []
    
    fillprimes = FOUND_PRIMES.__len__()-1
    
    loopamt = 1
    
    if args.__len__() >= 3:
        loopamt = int(args[2])
    
    for a_ in range(loopamt):
        y = 0
        while y <= fillprimes:
            nums.append(yes(FOUND_PRIMES[y]))
            y += 1
        
        bval = '00000000'
        
        val = bval
        
        result = []
        
        lt = yes(2)
        
        c_sz = 0
        
        
        while c_sz <= sz:
            r = ''
            t = 1
            for ye in nums:
                
                c_r = 0
                
                while c_r < sz-c_sz:
                    r += '1'
                    c_r += 1
                while r.__len__() < sz:
                    r += '0'
                    c_r += 1
                ye.val = r
                t = ye.get() + 1
                t += STORAGE["BINAI"]
                if verbose:
                    if not t in result:
                        result.append(t)
                    g = yes(ye).AND(lt)
                    if not g in result:
                        result.append(g)
                    h = t + lt.get()
                    if not h in result:
                        result.append(h)
                        lt.val = r
            c_sz += 1
            time.sleep(0.01)
    
    FOUND_PRIMES.sort()
    
    return result

'''
Sort of a beautiful mixture of an equation;
On the one hand, it's like a fine-toothed comb going over the sandy deserts of the number line
and picking up primes in clusters/clumps.

On the other hand, it's kind of inelegant and basically a buckshot fired into regions of the number line
hoping it'll catch more fish than it obliterates.

It's a very 'me' kinda algorithm, honestly.
'''
def lchaim(bound) -> list[int]:
    #"((2 ^ a) ^ r) + ((3 ^ b) ^ s)"
    result = []
    
    ctr = 0
    
    cap = bound // pow(10, 9)
    
    while ctr <= cap:
        
        a = (kung(2, ctr+1, bound))
        b = (kung(3, ctr+1, bound))
        
        p = (3 / a)
        q = (2 / b)
        
        t = a + b
        
        t1 = kung(t, p)
        t2 = kung(t, q)
        
        t1 = round(kung(t1, 2, bound))
        t2 = round(kung(t2, 3, bound))
        
        t3 = t1+t2
        
        t1 += STORAGE["LCHAIM"]
        t2 += STORAGE["LCHAIM"]
        t3 += STORAGE["LCHAIM"]
        
        while t1 % 2 == 0 or t1 % 3 == 0 or t1 % 5 == 0 or t1 % 7 == 0:
            t1 += 1
        while t2 % 2 == 0 or t2 % 3 == 0 or t2 % 5 == 0 or t2 % 7 == 0:
            t2 += 1
        while t3 % 2 == 0 or t3 % 3 == 0 or t3 % 5 == 0 or t3 % 7 == 0:
            t3 += 1
        
        if not t1 in result:
            result.append(t1)
        if not t2 in result:
            result.append(t2)
        if not t3 in result:
            result.append(t3)
        
        ctr += 1
    
    result.sort()
    
    return result

def loop(a, b):
    r = a
    
    compiled = []
    
    while r <= b:
        result = mush(a, r + STORAGE["LOOP"])
        if result.__len__() == 0:
            pass
            #pprint("(No results! Is the number a power of another root number?")
        else:
            for q in result:
                if not DEV["PRIME"] or isprime(q):
                    if q not in compiled:
                        compiled.append(q)
        r += 1
    ####
    compiled.sort()
    
    return compiled
    

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
        i = 2
        
        
        e[inc] = [kung(inc, 1)]
        
        while i < pcap:
            h = nummy.exp(i)
            e[inc].append(h)
            i += 1
        if inc % cooldown == 0:
            #pprint(e[inc])
            #time.sleep(restperiod)
            print(f"Progress: {inc}/{cap}", end=" ", flush=True)
        inc += 1
        
    
    pprint("[Seeding complete...]")

def setflag(key):
    #print(f"DEBUG: key is {repr(key)}, type is {type(key)}")
    DEV[key] = (not DEV[key])
    
    if key == "OUT":
        if DEV[key]:
            TOFILEOUT.toggle()
            
def printarraywithfiltration(arr,prt=True):
    
    print("@@@@@@@")
    print(len(arr))
    print(len(FOUND_PRIMES))
    print("@@@@@@@")
    
    for t in arr:
        prt = str(t)
        if isprime(t):
            prt += '*'
            if DEV["OPRIME"]:
                if not t in FOUND_PRIMES:
                    FOUND_PRIMES.append(t)
            
        if prt and (not DEV["PRIME"] or isprime(t)):
            print(prt)

if __name__ == "__main__":    
    sys.set_int_max_str_digits(0)
    # Get current soft and hard limits for virtual memory
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Syscall to raise the soft limit to the system's hard ceiling
    resource.setrlimit(resource.RLIMIT_AS, (hard, hard))
    
    pprint("Bleatmind say hello!")
    
    #We all know I was right to write the original pprint listed on this line, and also right to delete it from the internet.
    pprint("Now this is someone we can trust with humanity's future!\nAm I Right, Gamers?")
    
    
    '''
    AUTHOR'S NOTE:
        Any comment of form '#@' denotes AI-Generated Comments.
    '''
    
    #@ Instantiate globally or attach to your DEV/config dict
    TOFILEOUT = TeeStdout("mugo_debug.log")
    TOFILEOUT.toggle(enable=True)
    e = {}
    res = ''
    cmdstart = datetime.now()

    while not res == "Q":
        if not res == '':
            pprint("Completed last command in " + str(datetime.now() - cmdstart))
        
        res = input("->").upper()
        
        cmdstart = datetime.now()
        
        pprint(res)
        
        if res.startswith("FLAG"):
            split = res.split(' ')
            if split.__len__() >= 2:
                setflag(split[1])
                
                pprint("Flag " + split[1] + " set to: " + str(DEV[split[1]]))
        
        ##########################
        if res.startswith('SET'):
            split = res.split(' ')
            if split.__len__() >= 3:
                spf = sympify(split[2])
                rr = int(spf)
                STORAGE[split[1]] = (rr)
                pprint(f"{BLUE}Set " + split[1] + " storage to " + str(STORAGE[split[1]]) + f"{RESET}")
        
        if res.startswith("SAV "): #Saving code by AI
            ctr = 0
            
            split = res.split(' ')
            
            if split[1] == "TABLE":
                for q in e.keys():
                    curfolder = "" + str(ctr // 100)
                    
                    filepath = Path(TABLE_DIR + curfolder + "/p_" + str(q) + ".bin")
                    
                    #@ Create parent directories if they don't exist
                    filepath.parent.mkdir(parents=True, exist_ok=True)#@
                    
                    with open(filepath, "wb") as f:
                            v = e[q]
                            for num in v:
                                # Determine how many bytes are needed for this specific integer
                                byte_len = (num.bit_length() + 7) // 8
                                
                                # Write 2-byte header (length of integer) + raw integer bytes
                                f.write(byte_len.to_bytes(2, byteorder="big"))
                                f.write(num.to_bytes(byte_len, byteorder="big"))
                    ctr += 1
            elif split[1] == "PRIMES":
                curfolder = "output"
                
                filepath = Path(curfolder + "/found_primes" + ".bin")
                
                #@ Create parent directories if they don't exist
                filepath.parent.mkdir(parents=True, exist_ok=True)#@
                
                FOUND_PRIMES.sort()
                
                with open(filepath, "wb") as f:
                        for num in FOUND_PRIMES:
                            # Determine how many bytes are needed for this specific integer
                            byte_len = (num.bit_length() + 7) // 8
                            
                            # Write 2-byte header (length of integer) + raw integer bytes
                            f.write(byte_len.to_bytes(2, byteorder="big"))
                            f.write(num.to_bytes(byte_len, byteorder="big"))
                ctr += 1
                
        ##########################
        
        if res.startswith("SEED"):
            split = res.split(" ")
            pprint(split)
            if split.__len__() >= 2:
                if split[1].isnumeric() and split[2].isnumeric():
                    cap = int(split[1])
                    pcap = int(split[2])
                    
                    seed(cap, pcap)
        
        if res == 'TABLE':#@
            table_path = Path(TABLE_DIR)
            
            # Recursively find all .bin files across all subdirectories
            bin_files = sorted(table_path.rglob("*.bin"))
            print(f"Total .bin files: {len(bin_files)}")
            
            for file_path in bin_files:
                # Extract the integer index from the filename (e.g., 'p_5.bin' -> 5)
                # Assumes filenames follow 'p_<index>.bin'
                try:
                    i = int(file_path.stem.split('_')[1])
                    if i >= 2:
                        e[i] = load_huge_ints_from_bin(str(file_path))
                except (IndexError, ValueError):
                    continue
        #######################
        
        if res.startswith("LD"): #Take a peek in a .bin file
            split = res.split(' ')
            if split.__len__() > 1 and split[1].isnumeric():
                ree = load_huge_ints_from_bin("tables/" + str(int(split[1]) // 10) + "/p_" + split[1] + ".bin")
                pprint(ree)
            elif split[1] == "PRIMES":
                ree = load_huge_ints_from_bin("output/found_primes.bin")
                printarraywithfiltration(ree)
        ##########################
        if res.startswith("LCHAIM"):
            split = res.split(' ')
            if split.__len__() >= 4:
                bnd = int(split[1])
                bnd *= int(split[2])
                bnd *= pow(10, 10)
                
                loopies = int(split[3])
                
                rezzy = []
                
                
                #@@@
                
                #@ Create a pool of worker processes
                ctr_ = 1
                with mp.Pool(processes=loopies) as pool:
                    for y in range(1, loopies):
                        #@ pool.map runs count_to_ten for each core ID and collects return values
                        rezzy.append(pool.map(lchaim, [(bnd*y), (bnd * y * 2)]))
                    
                    #@ 2. Wait for all processes to complete before continuing
                    for p in PROCESSES:
                        p.join()
                        
                    #@@@
                    
                    for idx, rex in enumerate(rezzy):
                        '''
                        pprint(str(idx))
                        pprint(str(rex))
                        '''
                        printarraywithfiltration(rex[0])
                    PROCESSES.clear()
        ##########################
        if res.startswith("BINAI"):
            split = res.split(' ')
            if split.__len__() >= 2:
                printarraywithfiltration(binai(split, DEV["VBINAI"]))
        ##########################
        if res.startswith("LOOP"):
            split = res.split(' ')
            if split.__len__() >= 2:
                if split[1].isnumeric() and split[2].isnumeric():
                        printarraywithfiltration(loop(int(split[1]), int(split[2]))) 
        ########################
        if res.isnumeric():
            result = mush(int(res), STORAGE["LOOP"])
            if result.__len__() == 0:
                pprint("(No results! Is the number a power of another root number?")
            else:
                pprint("RESULTS FOUND")
                printarraywithfiltration(result)
                                
        
        