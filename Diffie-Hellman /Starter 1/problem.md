The set of integers modulo n, together with the operations of both addition and multiplication is a ring. This means that adding or multiplying any two elements in the set returns another element in the set.

When the modulus is prime: n = p, we are guaranteed an inverse of every element in the set, and so the ring is promoted to a field. We refer to this field as a finite field Fp.

The Diffie-Hellman protocol works with elements of some finite field Fp, where the prime modulus is typically a large prime.

Given the prime p = 991, and the element g = 209, find the inverse element d such that g * d mod 991 = 1.