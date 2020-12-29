from Crypto.PublicKey import RSA
from Crypto.Util.asn1 import DerSequence
from binascii import a2b_base64
from base64 import b64decode ,b16encode
with open('/home/kali/Desktop/cryptohack/CERTainly not/2048b-rsa.der', "rb" ) as f:
    kobj = RSA.importKey(f.read())
    print(kobj.e)
    