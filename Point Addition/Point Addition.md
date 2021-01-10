a = 497
b = 1768
p = 9739

O = (0, 0)

def div(u, v):
    return u*pow(v, -1, p)

def add(P, Q):
    if P == O:
        return Q
    if Q == O:
        return P
    if P[0] == Q[0] and (P[1]+Q[1]) % p == 0:
        return O
    if P != Q:
        l = div(Q[1]-P[1], Q[0]-P[0]) % p
    else:
        l = div(3*P[0]**2+a, 2*P[1]) % p
    x = l**2-P[0]-Q[0]
    y = l*(P[0]-x)-P[1]
    return (x % p, y % p)

X = (5274, 2841)
Y = (8669, 740)
print(add(X, Y))
print(add(X, X))

P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)
print(add(add(add(P, P), Q), R))
