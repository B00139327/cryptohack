from Crypto.Cipher import AES
import requests
url = 'http://http://aes.cryptohack.org'
encrypt = '/block_cipher_starter/encrypt_flag/'
decrypt = '/block_cipher_starter/decrypt/<ciphertext>/'

#get encrypted flag from website
r= requests.get(url + encrypt)
#send a request to the url and save the result in r

data = r.json()
ciphertext = data['ciphertext']



#get decrypted flag from website
r= requests.get(url + encrypt+ciphertext)

data = r.json()
plaintext = data['plaintext']

print(bytes.fromhex(plaintext))


