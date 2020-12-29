In Quadratic Residues we learnt what it means to take the square root modulo an integer. We also saw that taking a root isn't always possible.

In the previous case when p = 29, even the simplest method of calculating the square root was fast enough, but as p gets larger, this method becomes wildly unreasonable.

Lucky for us, we have a way to check whether an integer is a quadratic residue with a single calculation thanks to Legendre. In the following, we will assume we are working modulo a prime p.

Before looking at Legendre's symbol, let's take a brief detour to see an interesting property of quadratic (non-)residues.

Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue

Want an easy way to remember this? Replace "Quadratic Residue" with +1 and "Quadratic Non-residue" with -1, all three results are the same!


So what's the trick? The Legendre Symbol gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime p.

Legendre's Symbol: (a / p) ≡ a(p-1)/2 mod p obeys:

(a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
(a / p) = -1 if a is a quadratic non-residue mod p
(a / p) = 0 if a ≡ 0 mod p

Which means given any integer a, calculating pow(a,(p-1)/2,p) is enough to determine if a is a quadratic residue.

Now for the flag. Given the following 1024 bit prime and 10 integers, find the quadratic residue and then calculate its square root; the square root is your flag. Of the two possible roots, submit the larger one as your answer.

So Legendre's symbol tells us which integer is a quadratic residue, but how do we find the square root?! The prime supplied obeys p = 3 mod 4, which allows us easily compute the square root. The answer is online, but you can figure it our yourself if you think about Fermat's little theorem.