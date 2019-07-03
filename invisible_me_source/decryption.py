# Imports
from Crypto.Cipher import AES
import base64


# Decrypting an AES string
### Note: This assumes that the message is being passed in RADIX 64 format.
#def decryption(coded_64_message: str,key: str,init_vector: str) -> str:
def decryption(coded_64_message, key,init_vector):
    ### The +"===" is to ensure that the coded message is the correct length
    byte_object = base64.b64decode(coded_64_message+"===")
    decoder = AES.new(key,AES.MODE_CBC,init_vector)
    return decoder.decrypt(byte_object).decode('utf-8').strip()
