We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo p = 29. We can take the integer a = 11 and calculate a2 = 5 mod 29.

As a = 11, a2 = 5, we say the square root of 5 is 11.

This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a2 = 18

Your first idea might be to start with a = 1 and loop to a = p-1. In this discussion p isn't too large and we can quickly look.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a ∈ Fp* you never find an a such that a2 = 18.

What we are seeing, is that for the elements of F*p, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp*, there is no square root.

We say that an integer x is a Quadratic Residue if there exists an a such that a2 = x mod p. If there is no such solution, then the integer is a Quadratic Non-Residue.


In other words, x is a quadratic residue when it is possible to take the square root of x modulo an integer p.

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

If a2 = x then (-a)2 = x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.


p = 29
ints = [14, 6, 11]