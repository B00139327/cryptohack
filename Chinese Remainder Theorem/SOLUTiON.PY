import functools
from Crypto.Util.number import inverse

def chinese_remainder(a, m):
    sum = 0
    prod = functools.reduce(lambda x, y: x * y, m)
    for ai, mi in zip(a, m):
        Mi = prod // mi
        sum += ai * Mi * inverse(Mi, mi)
    return sum % prod

print(chinese_remainder(a, 935))