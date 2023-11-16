from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    return private_key, public_key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_private_key_from_file(filename):
    with open(filename, 'rb') as f:
        key_data = f.read()
        return serialization.load_pem_private_key(key_data, password=None, backend=default_backend())

def load_public_key_from_file(filename):
    with open(filename, 'rb') as f:
        key_data = f.read()
        return serialization.load_pem_public_key(key_data, backend=default_backend())

def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_message(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode('utf-8')

# 生成RSA密钥对
private_key, public_key = generate_rsa_key_pair()

# 保存密钥到文件
save_key_to_file(private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
), 'private_key.pem')

save_key_to_file(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
), 'public_key.pem')

# 从文件加载密钥
loaded_private_key = load_private_key_from_file('private_key.pem')
loaded_public_key = load_public_key_from_file('public_key.pem')

# 加密和解密消息
message = "RSA"
ciphertext = encrypt_message(loaded_public_key, message)
decrypted_message = decrypt_message(loaded_private_key, ciphertext)

print("Original Message:", message)
print("Encrypted Message:", ciphertext.hex())
print("Decrypted Message:", decrypted_message)
