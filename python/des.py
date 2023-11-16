from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

#加密函数 拆成个部分加密
def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

#解密函数 
def decrypt_des(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text

# 随机生成数字密钥
key = get_random_bytes(8)
# 明文 8字节的整数倍
plaintext = b'TestTest'

# 加密
encrypted_text = encrypt_des(key, plaintext)
print("Encrypted Text:", encrypted_text.hex())

# 解密
decrypted_text = decrypt_des(key, encrypted_text)
print("Decrypted Text:", decrypted_text.decode())
