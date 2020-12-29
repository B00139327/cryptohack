We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.

The integers modulo p define a field, denoted Fp.

If the modulus is not prime, the set of integers modulo n define a ring.


A finite field Fp is the set of integers {0,1,...,p-1}, and under both addition and multiplication there is an inverse element b for every element a in the set, such that a + b = 0 and a * b = 1.

 A field is a general name for a commutative ring in which every non-zero element has a multiplicative inverse.


 Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: a + 0 = a and a * 1 = a.


Lets say we pick p = 17. Calculate 317 mod 17. Now do the same but with 517 mod 17.

What would you expect to get for 716 mod 17? Try calculating that.

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.

Now take the prime p = 65537. Calculate 27324678765465536 mod 65537.

Did you need a calculator?