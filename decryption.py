from Crypto.Cipher import AES
import base64

def decryption(coded_64_message,key,init_vector):
    byte_object = base64.b64decode(coded_64_message+"===")
    decoder = AES.new(key,AES.MODE_CBC,init_vector)
    return decoder.decrypt(byte_object).decode('utf-8').strip()
