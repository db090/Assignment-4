# test_encryptor.py

import pytest
from crypto.encryptor import encrypt_message, decrypt_message

def test_encryption_decryption_success():
    message = "SecretData"
    passkey = "MySecureKey123"

    encrypted = encrypt_message(message, passkey)
    decrypted = decrypt_message(encrypted, passkey)

    assert decrypted == message, "Decrypted message should match the original"

def test_decryption_fails_with_wrong_passkey():
    message = "TopSecret"
    passkey = "CorrectKey"
    wrong_passkey = "WrongKey"

    encrypted = encrypt_message(message, passkey)
    decrypted = decrypt_message(encrypted, wrong_passkey)

    assert decrypted is None, "Decryption with wrong passkey should return None"

def test_output_is_string():
    message = "Text123"
    passkey = "Key123"

    encrypted = encrypt_message(message, passkey)
    assert isinstance(encrypted, int), "Encrypted output should be a string"
