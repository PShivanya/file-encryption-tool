from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted = f.encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    with open(filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)

# Example usage:
# write_key()
# key = load_key()
# encrypt_file("secret.txt", key)
# decrypt_file("secret.txt.enc", key)
