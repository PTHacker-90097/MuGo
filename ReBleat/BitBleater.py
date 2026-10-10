#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Ignore this class it's not done cooking
If you see it I forgot to put it in the .gitignore
'''

from pathlib import Path
from bitarray import bitarray

class BINGen:
    
    '''
    #@
    '''
    def bleatintobeing(bits: int) -> list[str]:
      # 2 raised to the power of 'bits' gives total permutations (e.g., 16 for 4 bits)
      total_combinations = 2**bits
    
      # Format each integer as a zero-padded binary string of length 'bits'
      return [f"{i:0{bits}b}" for i in range(total_combinations)]
  

    def dothething():
        '''
        START DEBRA ZONE
        '''
        print("TST")
        bitrange = BINGen.bleatintobeing(16)
        
        tee = []
        
        for q in bitrange:
            print(q)
            
            
        curfolder = "output/rebleat"
        
        filepath = Path(curfolder + "/bitpatterns" + ".bin")
        
        #@ Create parent directories if they don't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)#@
        
        with open(filepath, "wb") as f:
                for q in bitrange:
                    num = int(q, 2)
                    # Determine how many bytes are needed for this specific integer
                    byte_len = (num.bit_length() + 7) // 8
                    
                    # Write 2-byte header (length of integer) + raw integer bytes
                    f.write(byte_len.to_bytes(2, byteorder="big"))
                    f.write(num.to_bytes(byte_len, byteorder="big"))
            
        print("TST")
        '''
        END   DEBRA ZONE
        ''' 