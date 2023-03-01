# AES algorithm

from Crypto.Cipher import AES
import base64

def encrypt_AES(key, plain_text):
    key = key.encode('utf-8')
    plain_text = plain_text.encode('utf-8')
    iv = b'0000000000000000'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plain_text = _pad(plain_text, AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_plain_text)
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_base64

def decrypt_AES(key, encrypted_text):
    key = key.encode('utf-8')
    encrypted_text = base64.b64decode(encrypted_text)
    iv = b'0000000000000000'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(encrypted_text)
    decrypted_text = decrypted_bytes.decode('utf-8').rstrip('\0')
    return decrypted_text

def _pad(s, block_size):
    return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

def main():
    key = 'secretkey123456'
    plain_text = 'This is a secret message.'
    encrypted_text = encrypt_AES(key, plain_text)
    print('Encrypted text:', encrypted_text)
    decrypted_text = decrypt_AES(key, encrypted_text)
    print('Decrypted text:', decrypted_text)

if __name__ == '__main__':
    main()
