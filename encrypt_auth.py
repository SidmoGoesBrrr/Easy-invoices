from zocrypt import encrypter,key
import os
key = key.generate()
to_encrypt=input("Enter your auth token to encrypt: ")
print(f"Your encrypted auth token is: {encrypter.encrypt_text(to_encrypt,key)}")
