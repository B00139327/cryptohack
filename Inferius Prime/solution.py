 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
e =3
p =  752708788837165590355094155871
q = 986369682585281993933185289261
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

print(d)