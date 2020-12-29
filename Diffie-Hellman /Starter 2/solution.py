p =28151
g = 2
found = False

while not found:
    for n in range(2,p):
    #g ^ n mod p1

        if pow(g,n ,p) ==g:
            break
        if n == p-2:
            print(g)
            found = True
    g = g+1