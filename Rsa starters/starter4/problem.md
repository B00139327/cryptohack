The private key d is used to decrypt ciphertexts created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).

The private key is the secret piece of information or "trapdoor" which allows us to quickly invert the encryption function. If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to first factorise the modulus.

In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N.

Given the two primes:

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

and the exponent:

e = 65537

What is the private key d?