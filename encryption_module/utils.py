import rsa

def generate_keys():
    pubkey, privkey = rsa.newkeys(64)
    return pubkey, privkey

def encrypt_message(message, pubkey):
    enc_message = rsa.encrypt(message, pubkey)
    return enc_message

def decrypt_message(enc_message, privkey):
    message = rsa.decrypt(enc_message, privkey)
    return message

def convert_key_to_string(key):
    return key.save_pkcs1().decode('utf8')

def convert_string_to_key(key):
    return rsa.PublicKey.load_pkcs1(key.encode('utf8'))



