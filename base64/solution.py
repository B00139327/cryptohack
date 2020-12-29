import base64

byte = b''
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte = byte.fromhex(hex_string)

a = base64.b64encode(byte)

print(a)