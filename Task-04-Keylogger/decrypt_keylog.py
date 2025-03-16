from cryptography.fernet import Fernet

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Decrypt the content of keylog.txt
with open("keylog.txt", "rb") as f:
    encrypted_data = f.readlines()

    # Decrypt each line and print it
    for encrypted_line in encrypted_data:
        decrypted_line = cipher.decrypt(encrypted_line.strip())  # Remove any trailing newline characters
        print(decrypted_line.decode())
