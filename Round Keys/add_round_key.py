from Crypto.Cipher import AES
import binascii
from random import randint
from operator import ixor  
from itertools import chain 


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    return bytes(sum(matrix, []))


    
def add_round_key(a, b):
    for x in range(4):
        for y in range(4):
            a[x][y] = a[x][y] ^ b[x][y]
    return a        
print(matrix2bytes(add_round_key(state, round_key)))

