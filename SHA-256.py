#  Secure Hash Algorithm 256 (SHA-256) 

import hashlib

def sha256_hash(msg):
    # Convert message to bytes if it is not already
    if isinstance(msg, str):
        msg = msg.encode()
    
    # Compute SHA-256 hash
    hash_object = hashlib.sha256(msg)
    hash_value = hash_object.hexdigest()
    
    return hash_value
