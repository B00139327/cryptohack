So far we've been using the product of small primes for the modulus, but small primes aren't much good for RSA as they can be factorised using modern methods.

What is a "small prime"? There was an RSA Factoring Challenge with cash prizes given to teams who could factorise RSA moduli. This gave insight to the public into how long various key sizes would remain safe. Computers get faster, algorithms get better, so in cryptography it's always prudent to err on the side of caution.

These days, using primes that are at least 1024 bits long is recommended—multiplying two such 1024 primes gives you a modulus that is 2048 bits large. RSA with a 2048-bit modulus is called RSA-2048.

Some say that to really remain future-proof you should use RSA-4096 or even RSA-8192. However, there is a tradeoff here; it takes longer to generate large prime numbers, plus modular exponentiations are predictably slower with a large modulus.

Factorise the 150-bit number 510143758735509025530880200653196460532653147 into its two constituent primes. Give the smaller one as your answer.

