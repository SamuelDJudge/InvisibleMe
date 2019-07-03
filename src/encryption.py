# Imports
from Crypto.Cipher import AES
import base64

### AES assumes that the message is a multiple of 16.
### This function adds empty space to the end to make up the rest of those characters, if needed
def making_multiple_16(text: str) -> str:
    len_of_text = len(text)
    while len_of_text % 16 != 0:
        text += " "
        len_of_text = len(text)
    return text

### This code uses AES to encrypt the message and then turns it into a Base 64 encoding to confirm that
### it displays and reads correctly.
def encryption(text: str,key: str,init_vector: str) -> str:
    coder = AES.new(key,AES.MODE_CBC,init_vector)
    code = coder.encrypt(making_multiple_16(text))
    code_64 = str(base64.b64encode(code))
    return code_64
