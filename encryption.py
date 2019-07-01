from Crypto.Cipher import AES
import base64

from user_input import *

def making_multiple_16(text):
    len_of_text = len(text)
    while len_of_text % 16 != 0:
        text += " "
        len_of_text = len(text)
    return text

def encryption(text,key,init_vector):
    coder = AES.new(key,AES.MODE_CBC,init_vector)
    code = coder.encrypt(making_multiple_16(text))
    code_64 = str(base64.b64encode(code))
    return code_64
