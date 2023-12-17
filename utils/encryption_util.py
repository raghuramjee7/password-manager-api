import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class Encryption:
    def __init__(self, key):
        self.key = Fernet(self.string_to_fernet_key(key))

    def encrypt(self, message):
        return self.key.encrypt(message.encode())

    def decrypt(self, token):
        return self.key.decrypt(token).decode()

    def string_to_fernet_key(self, input_string):
    # Convert the input string to bytes
        password = input_string.encode()

        # Derive a key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            salt=b'some_salt',  # Add a salt for additional security
            iterations=100000,  # Adjust the number of iterations as needed
            length=32  # For a 256-bit key (Fernet key)
        )

        key = kdf.derive(password)

        # Create a Fernet key
        fernet_key = base64.urlsafe_b64encode(key)

        return fernet_key
