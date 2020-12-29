def euclid_algo(x, y ):  #  where n > m
    
    r = x % y
    if r == 0:
        print ("gcd(%d, %d) = %d" %(a, b, y))
    else:
        euclid_algo(y, r)

a = 66528
b = 52920

euclid_algo(a, b)