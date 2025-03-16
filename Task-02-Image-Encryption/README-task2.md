# Task 2 - Image Encryption Tool

## 🔒 Description
A Python program that encrypts/decrypts images using XOR operations with pixel manipulation

## 📦 Dependencies
- Python 3.8+
- Pillow (`pip install pillow`)

## 🚀 Usage
```bash
python image_encryptor.py
```
Follow the prompts to:
1. Choose encryption/decryption mode
2. Enter input/output file paths
3. Provide encryption key

## ✨ Features
- Symmetric encryption (same key for encrypt/decrypt)
- SHA-256 key hashing
- Preserves image format
- Pixel value manipulation

## ⚠️ Ethical Note
- Only use on images you own
- Keep encryption keys secure
- Not suitable for sensitive data

## Example
```bash
# Encrypt
Mode: encrypt
Input: original.jpg
Output: encrypted.png
Key: mysecret123

# Decrypt
Mode: decrypt
Input: encrypted.png
Output: decrypted.jpg
Key: mysecret123
```
