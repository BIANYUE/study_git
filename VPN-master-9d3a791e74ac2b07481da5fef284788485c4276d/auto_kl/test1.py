from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import binascii

def des_decrypt(ciphertext, key, mode):
    key_bytes = key.encode('utf-8')

    cipher = DES.new(key_bytes, mode)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted


ciphertext = binascii.unhexlify('d898d74eadf5bbdbaac07d0437c9a3081c7232e976275481387f850c517ead6cdee1a792d5f4248fd2c338064506a20bc422b831ffb04d80baa260432b4f57c619bfb7ae3da174ba1eb6af45f53d76f5472bfdddcdf4711be64ffcc5c461d06b53aed1b765a7707d19bfb7ae3da174ba5a5069d6b4a566c5f79b9ef1a1c13b44b8820d565d3dd85b21403309737707e9c842e378876e6451068f5f9c0e49d68edcfdb0381fa74f253cb910270a4ee7b021403309737707e9d1fb6a42e59c8f9095afa2d8459d926227771b7f4c03e6375c4ac83b2e6b052e9fd96213fbfb8e775e9fc487df922374af1d349e4fe6d9fa90f9e53fa82e755b983fcf655ea0502412a3ea2c96e76894ddd9def9dc09f42be38aefc588d41fdd')
key_str = 'google.c'
key_hex = '676f6f67'
mode = DES.MODE_ECB

decrypted_str = des_decrypt(ciphertext, key_str, mode)
decrypted_hex = des_decrypt(ciphertext, key_hex, mode)


print('Decrypted (str key):', decrypted_str)
decoded_data = decrypted_str.decode('utf-8')
print(decoded_data)
print('Decrypted (hex key):', decrypted_hex)