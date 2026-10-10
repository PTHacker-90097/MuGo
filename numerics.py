#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:14:06 2026

@author: pam
"""
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



