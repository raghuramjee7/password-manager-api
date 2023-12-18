from simplecrypt import encrypt, decrypt

def encrypt_password(password, text):
    return encrypt(password, text).decode("utf-8")

def decrypt_password(password, text):
    return decrypt(password, text.encode("utf-8")).decode("utf-8")

