import base64
import hashlib
from cryptography.fernet import Fernet,InvalidToken

def generate_key(passkey:str) -> bytes:
    sha256_hash=hashlib.sha256(passkey.encode()).digest()
    fernet_key=base64.urlsafe_b64encode(sha256_hash)
    return fernet_key
def encrypt_message(message:str,passkey:str) -> str:
    key=generate_key(passkey)
    f=Fernet(key)
    token=f.encrypt(message.encode())
    return token.decode()

def  decrypt_message(token:str,passkey:str)->str:
    key = generate_key(passkey)
    f=Fernet(key)
    try:
        decrypted=f.decrypt(token.encode())
        return decrypted.decode()
    except InvalidToken:
        return None #Indicate decryption failed due to wrong key