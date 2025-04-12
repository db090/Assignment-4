import hashlib

def hash_passkey(passkey:str) ->str:
    """Returns the SHA-256 hash of the passkey."""
    return hashlib.sha256(passkey.encode()).hexdigest()

def verfiy_passkey(input_passkey:str , stored_hash:str) -> bool:
    """Verifies if the SHA-256 hash of the input matches the stored hash."""
    return hash_passkey(input_passkey) == stored_hash