#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:01:28 2026

@author: pam

"""

'''
AUTHOR'S NOTE:
    
    Any comment of form '#@' denotes AI-Generated Comments / code snippets
    Any block comment of form '@@@' denotes use of AI-Generated code blocks left as-is or edited to a small amount for adaptation to human-written code.
    Any block comment of form '@#@' denotes use of AI-Generated code which has changed, Ship of Theseus-style, into human-written code via the passage of time.
    
'''


from bleattodisc import TeeStdout
from ReBleat.BitBleater import BINGen
from numerics import kung, yes

from sympy import pprint, isprime, symbols, sympify, solve
from pathlib import Path

from datetime import datetime

from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp


import numpy as np
import sys
import time
import resource
import array

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets formatting back to default


class BleatMind:
    TABLE_DIR = "tables/"
    
    DEV = {
            "PRIME"     : True,
            "OUT"       : True,
            "VBINAI"    : True, # "Verbose" Binai flag
            "OPRIME"    : True,  # "Output" Primes flag
            "SPICYCPU"  : True  # Leave as 'True' if you're OK with CPU temp spikes, otherwise set to "False" for slower runtime results but better CPU temp management
    }
    
    STORAGE = {
            "LOOP"  : 0,
            "LCHAIM": 0,
            "BINAI" : 0,
            "BLEAT" : 0,
        }
    
    TOFILEOUT = None
    
    NUM_CORES = mp.cpu_count()#@
    PROCESSES = []#@
    
    sleepgen = 5000
    sleepamt = 0.1
    
    E = {}
    P = []
    
    def __init__(self):
        P = [1, 3, 5, 7]
        E = {}
        pass
    
    def load_huge_ints_from_bin(self, filename: str) -> list[int]: #Method code by AI
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
    
    def load_base_on_demand(self, base: int) -> list[int]:
        """
        Reads a single base binary file on demand.
        Returns a list of arbitrary-precision integers.
        """
        file_path = self.TABLE_DIR + " / " + f"base_{base:03d}.bin"
        
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
    
    
    def mush(self, i, j):
        res = []
        
        for N in self.E[i]:
            r = N
            res.append(r + j)
        
        return res
    
    def binai(self, args, verbose=True):
        #Size (In bits) of values
        sz = kung(2, int(args[1]))
        #inc = int(args[2])
        
        nums = []
        
        fillprimes = (len(self.P)+1) // 10
        
        loopamt = 1
        
        if len(args) >= 3:
            loopamt = int(args[2])
        
        for a_ in range(loopamt):
            y = 0
            while y <= fillprimes:
                nums.append(yes(self.P[y]))
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
                    while len(r) < sz:
                        r += '0'
                        c_r += 1
                    ye.val = r
                    t = ye.get() + 1
                    t += self.STORAGE["BINAI"]
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
                    self.sleepcheck(c_sz)
                c_sz += 1
        return result
    
    '''
    Sort of a beautiful mixture of an equation;
    On the one hand, it's like a fine-toothed comb going over the sandy deserts of the number line
    and picking up primes in clusters/clumps.
    
    On the other hand, it's kind of inelegant and basically a buckshot fired into regions of the number line
    hoping it'll catch more fish than it obliterates.
    
    It's a very 'me' kinda algorithm, honestly.
    '''
    def lchaim(self, bound) -> list[int]:
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
            
            t1 += self.STORAGE["LCHAIM"]
            t2 += self.STORAGE["LCHAIM"]
            t3 += self.STORAGE["LCHAIM"]
            
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
                
            self.sleepcheck(ctr)
            
            ctr += 1
        
        result.sort()
        
        return result
    
    def sleepcheck(self, ctr):
        if not self.DEV["SPICYCPU"] and ctr % self.sleepgen == 0:
            time.sleep(self.sleepamt)
    
    def loop(self, a, b):
        r = a
        
        compiled = []
        
        while r <= b:
            result = self.mush(a, r + self.STORAGE["LOOP"])
            if len(result) == 0:
                pass
                #pprint("(No results! Is the number a power of another root number?")
            else:
                for q in result:
                    if not self.DEV["PRIME"] or isprime(q):
                        #not q in self.E is experimental;
                        #Intent is to immediately filter out a candidate--
                        #--Should it be found to be part of the Roots of the Exponent Set
                        if not q in self.E and q not in compiled:
                            compiled.append(q)
            r += 1
        ####
        compiled.sort()
        
        return compiled
    
    
    '''
    ARGS:
    Power of ten to start at,
    Power of ten to end at,
    Power of ten to increment by
    
    NOTES:
    Kindof a "what if" that had been rattling around in my head.
    I hope anyone looking at this code gets irritated enough at what I write--
    -- to start fixing it up or starting from scratch, inspired by my inefficiencies.
    
    Cheers to you if you can!
    '''
    
    def bleat(self, workerid, args):
        bass = pow(10, int(args[1]))+1
        
        inc = pow(10, int(args[3]))
        
        a = bass-((workerid+1)*inc)
        
        div = int(args[4])
        
        cap = pow(10, int(args[2]))-((workerid+1)*inc)
        
        a += self.STORAGE["BLEAT"]
        cap += self.STORAGE["BLEAT"]
        
        cands = [
                a,
                a+2,
                a+6,
                a+8
            ]
        
        result = []
        
        while a < cap:
            
            cands[0] += inc
            cands[1] += inc
            cands[2] += inc
            cands[3] += inc
            
            for i in range(len(cands)):
                if not cands[i] in result and isprime(cands[i]):
                    result.append(cands[i])
                cands[i] += 10#or inc, or make it its own arg        
            a += inc
        
        
        return workerid, result
        
    
    def seed(self, cap, pcap):
        self.E.clear()
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
            
            
            self.E[inc] = [kung(inc, 1)]
            
            while i < pcap:
                h = nummy.exp(i)
                self.E[inc].append(h)
                i += 1
            if inc % cooldown == 0:
                #pprint(e[inc])
                #time.sleep(restperiod)
                print(f"Progress: {inc}/{cap}", end=" ", flush=True)
            inc += 1
            
        
        pprint("[Seeding complete...]")
    
    def setflag(self, key):
        #print(f"DEBUG: key is {repr(key)}, type is {type(key)}")
        self.DEV[key] = (not self.DEV[key])
        
        if key == "OUT":
            if self.DEV[key]:
                self.TOFILEOUT.toggle()
                
    def printarraywithfiltration(self, arr,pr=True):
        
        print("@@@@@@@")
        print("Array Length: " + str(len(arr)))#@
        print("Total Primes In Memory: " + str(len(self.P)))#@
        print("@@@@@@@")
        
        for t in arr:
            prt = str(t)
            if isprime(t):
                prt += '*'
                if self.DEV["OPRIME"]:
                    if not t in self.P:
                        self.P.append(t)
                
            if pr and (not self.DEV["PRIME"] or isprime(t)):
                print(prt)
                
    def Console(self):
        res = ''
        cmdstart = datetime.now()
        
        P = [
                1 , 2 , 3 , 5 , 7
            ]
        
        while not res == "Q":
            if not res == '':
                pprint("Completed last command in " + str(datetime.now() - cmdstart))
            
            res = input("->").upper()
            
            cmdstart = datetime.now()
            
            pprint("Running command { " + res + " }")
            
            
            ###############################
            if res.startswith("CLR"):
                split = res.split(' ')
                if len(split) > 2:
                    if split[1] == "PRIMES":
                        P.clear()
                        P = [1, 3, 5, 7]
            ################################
            if res.startswith("FLAG"):
                split = res.split(' ')
                if len(split) >= 2:
                    self.setflag(split[1])
                    
                    pprint("Flag " + split[1] + " set to: " + str(self.DEV[split[1]]))
            ##########################
            if res.startswith('SET'):
                split = res.split(' ')
                if len(split) >= 3:
                    spf = sympify(split[2])
                    rr = int(spf)
                    self.STORAGE[split[1]] = (rr)
                    pprint(f"{BLUE}Set " + split[1] + " storage to " + str(self.STORAGE[split[1]]) + f"{RESET}")
            ###########################
            if res.startswith("SEED"):
                split = res.split(" ")
                pprint(split)
                if len(split) >= 2:
                    if split[1].isnumeric() and split[2].isnumeric():
                        cap = int(split[1])
                        pcap = int(split[2])
                        
                        self.seed(cap, pcap)
            #######################
            '''
            @@@
            '''
            if res.startswith("LD"): #Take a peek in a .bin file
                split = res.split(' ')
                if len(split) > 1 and split[1].isnumeric():
                    ree = self.load_huge_ints_from_bin("tables/" + str(int(split[1]) // 100) + "/p_" + split[1] + ".bin")
                    pprint(ree)
                elif split[1] == "PRIMES":
                    ree = self.load_huge_ints_from_bin("output/found_primes.bin")
                    self.printarraywithfiltration(ree)
                elif split[1] == "TABLE":
                    table_path = Path(self.TABLE_DIR)
                    
                    # Recursively find all .bin files across all subdirectories
                    bin_files = sorted(table_path.rglob("*.bin"))
                    print(f"Total .bin files: {len(bin_files)}")
                    
                    for file_path in bin_files:
                        # Extract the integer index from the filename (e.g., 'p_5.bin' -> 5)
                        # Assumes filenames follow 'p_<index>.bin'
                        try:
                            i = int(file_path.stem.split('_')[1])
                            if i >= 2:
                                self.E[i] = self.load_huge_ints_from_bin(str(file_path))
                        except (IndexError, ValueError):
                            continue
            '''
            @@@
            '''
            '''
            @#@
            '''
            if res.startswith("SV "): #Saving code by AI
                ctr = 0
                
                split = res.split(' ')
                
                if split[1] == "TABLE":#NOTE: Presently, this doesn't save multiples of ten. It's funnier to leave it like this, as the program is still deeply performant. What has One Zero ever done for me, anyways?
                    for q in self.E.keys():
                        curfolder = "" + str(ctr // 100)
                        
                        filepath = Path(self.TABLE_DIR + curfolder + "/p_" + str(q) + ".bin")
                        
                        #@ Create parent directories if they don't exist
                        filepath.parent.mkdir(parents=True, exist_ok=True)#@
                        
                        with open(filepath, "wb") as f:
                                v = self.E[q]
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
                    
                    P.sort()
                    
                    with open(filepath, "wb") as f:
                            for num in P:
                                # Determine how many bytes are needed for this specific integer
                                byte_len = (num.bit_length() + 7) // 8
                                
                                # Write 2-byte header (length of integer) + raw integer bytes
                                f.write(byte_len.to_bytes(2, byteorder="big"))
                                f.write(num.to_bytes(byte_len, byteorder="big"))
                    ctr += 1
            '''
            @#@
            '''
            ####################
            if res.startswith("INS"):
                split = res.split(' ')
                if len(split) > 2:
                    if split[1] == "PRIMES":
                        rang1 = 0
                        rang2 = len(P)
                        
                        if len(split) > 2:
                            rang1 = int(split[2])
                            if len(split) > 3:
                                rang2 = int(split[3])
                        print(f"Showing primes loaded in range:\n {rang1}, {rang2}")
                        while rang1 < rang2:
                            print(P[rang1])
                            rang1 += 1
                else:
                    print("Presently, there are " + str(len(P)) + " primes loaded in memory.")
            #######################
            if res.startswith("LCHAIM"):
                split = res.split(' ')
                if len(split) >= 4:
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
                            rezzy.append(pool.map(self.lchaim, [(bnd), (bnd+4), (bnd+8)]))
                        
                        #@ 2. Wait for all processes to complete before continuing
                        for p in self.PROCESSES:
                            p.join()
                            
                        #@@@
                        
                        for idx, rex in enumerate(rezzy):
                            '''
                            pprint(str(idx))
                            pprint(str(rex))
                            '''
                            self.printarraywithfiltration(rex[0])
                        self.PROCESSES.clear()
            ##########################
            if res.startswith("BINAI"):
                split = res.split(' ')
                if len(split) >= 2:
                    self.printarraywithfiltration(self.binai(split, self.DEV["VBINAI"]))
            ##########################
            if res.startswith("LOOP"):
                split = res.split(' ')
                if len(split) >= 2:
                    if split[1].isnumeric() and split[2].isnumeric():
                            self.printarraywithfiltration(self.loop(int(split[1]), int(split[2]))) 
            ########################
            if res.startswith("BLEAT"):
                split = res.split(' ')
                if len(split) >= 4:
                    result = []
                    if len(split) == 4:
                        split.append('1')
                        split.append('0')
                    
                        result = self.bleat(split)
                    else:
                        g = int(split[4])
                        #@
                        with ProcessPoolExecutor(max_workers=g) as executor:
                            # Submit tasks across the worker pool
                            futures = {
                                executor.submit(self.bleat, i, split): i
                                for i in range(g)
                            }
                        #\@
                        print("Workers done!?")
                        total_primes = 0
                        for future in as_completed(futures):
                            wid, result = future.result()
                            total_primes += len(result)
                            print(f"[+] Worker {wid} finished. Collected chunk results.")
                            print("Found " + str(len(result)) + " primes in range!")
                            uniq = 0
                            for q in result:#Assumes primality check in bleat
                                if not q in P:
                                    P.append(q)
                                    uniq += 1
                            print("Added " + str(uniq) + " primes to memory!")
                            print("Total primes in memory: " + str(len(P)))
            ########################
            
            ########################
            if res.isnumeric():#TODO rework into a discrete command; Checks for number entries loaded in memory, where LD checks number values saved to disk.
                result = self.mush(int(res), self.STORAGE["LOOP"])
                if len(result) == 0:
                    pprint("(No results! Is the number a power of another root number?")
                else:
                    pprint("RESULTS FOUND")
                    self.printarraywithfiltration(result)
                                    
            
    
if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    # Get current soft and hard limits for virtual memory
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Syscall to raise the soft limit to the system's hard ceiling
    resource.setrlimit(resource.RLIMIT_AS, (hard, hard))
    
    pprint("Bleatmind say hello!")
    
    #We all know I was right to write the original pprint listed on this line, and also right to delete it from the internet.
    pprint("Now this is someone we can trust with humanity's future!\nAm I Right, Gamers?")

    #@ Instantiate globally or attach to your DEV/config dict
    TOFILEOUT = TeeStdout("mugo_debug.log")
    TOFILEOUT.toggle(enable=True)
    
    console = BleatMind()
    
    console.Console()
    
    pprint("Program closing, thanks for playing!")
        