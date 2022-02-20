import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_message(message, password):
    password_provided = password
    password = password_provided.encode()
    salt = b"salty"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()


def decrypt_message(message, password):
    password_provided = password
    password = password_provided.encode()
    salt = b"salty"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    f = Fernet(key)
    try:
        plain_text = f.decrypt(message.encode()).decode()
    except:
        plain_text = "Nice Try Bitch !!!!"
    return plain_text
