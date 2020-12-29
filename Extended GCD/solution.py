def extendgcd_algo(a, b):
    x= 0
    y= 1 
    u= 1 
    v= 0
    while a != 0:
        q =b//a
        r=  b%a
        m =x-u*q
        n =y-v*q
        b=a
        a=r
        x=u
        y=v
        u=m
        v = n
    gcd = b
    return gcd, x, y

print (extendgcd_algo(26513,32321))

k ,i =1,2

print(k,i)