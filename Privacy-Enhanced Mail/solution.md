from Crypto.PublicKey import RSA
from base64 import b64decode ,b16encode
with open('/home/kali/Desktop/cryptohack/Privacy-Enhanced Mail?/pemail.pem', "rb" ) as f:
    kobj = RSA.importKey(f.read())
    print(kobj.d)