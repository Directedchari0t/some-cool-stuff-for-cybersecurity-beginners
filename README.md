# Will you like it? tell me by like it

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 📚 Tasks Overview

1. **Caesar Cipher**  
   Encryption/decryption tool using the classic substitution cipher
   
2. **Image Encryption**  
   Pixel manipulation-based image encryption/decryption system

3. **Password Strength Checker**  
   Comprehensive password analysis tool with feedback system

4. **Keylogger (Educational)**  
   Basic keyboard input monitoring demonstration

5. **Packet Sniffer**  
   Network traffic analysis tool (requires admin privileges)

## ⚙️ Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/some-cool-stuff.git
cd Prodigy-Infotech-Internship-Tasks
```

2. Install requirements:
```bash
pip install -r requirements.txt
```



# Task 1 - Caesar Cipher

## 🎯 Objective
Implement a classic Caesar Cipher for encrypting and decrypting text.

## 📝 Description
The Caesar Cipher is one of the simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet.

## 🛠️ Features
- Encrypt and decrypt text
- Handle uppercase and lowercase letters
- Preserve non-alphabetic characters
- Customizable shift value

## 🚀 Usage
    python3 caesar_cipher.py

# Encrypt
    Enter operation (encrypt/decrypt): encrypt
    Enter message: Hello World!
    Enter shift value: 3
    Result: Khoor Zruog!

# Decrypt
    Enter operation (encrypt/decrypt): decrypt
    Enter message: Khoor Zruog!
    Enter shift value: 3
    Result: Hello World!




---



# Task 2 - Image Encryption Tool

## 🎯 Objective
Develop an image encryption tool using pixel manipulation.

## 📝 Description
This tool encrypts and decrypts images using XOR operations on pixel values. It provides a simple yet effective way to secure image files.

## 🛠️ Features
- Encrypt and decrypt images
- Preserve image format
- SHA-256 key hashing
- Pixel value manipulation

## 🚀 Usage
    python3 image_encryptor.py

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


---



# Task 3 - Password Strength Checker

## 🎯 Objective
Create a tool to assess password strength based on multiple criteria.

## 📝 Description
This tool evaluates passwords based on length, character diversity, and common patterns. It provides feedback to help users create stronger passwords.

## 🛠️ Features
- Length check (minimum 8 characters)
- Uppercase, lowercase, digit, and special character checks
- Common password detection
- Sequential pattern detection

## 🚀 Usage

    python3 password_checker.py
## Example 
    Enter password: P@ssw0rd123

    Strength: Very Strong (8/8)
    All requirements met!


---



# Task 4 - Educational Keylogger

## 🎯 Objective
Develop a basic keylogger for educational purposes.

## 📝 Description
This keylogger demonstrates how keyboard input can be captured and logged. It is designed for educational use only and includes safeguards to prevent misuse.

## 🛠️ Features
- Logs keystrokes with timestamps
- Stops logging on ESC key press
- No persistence or stealth features
- Logs saved to `keylog.txt`

## 🚀 Usage 
    sudo python3 keylogger.py
## Example    
# Run keylogger
    sudo python3 keylogger.py
    # Type in any application
    # Press ESC to stop

    # Check logs
    cat keylog.txt
    #check the encrypted codes by running decrypted.py
    python3 decrypted.py
   
---



# Task 5 - Network Packet Sniffer

## � Objective
Create a tool to capture and analyze network packets.

## 📝 Description
This packet sniffer captures network traffic and displays relevant information such as source/destination IPs, protocols, and payload data.

## 🛠️ Features
- Captures IP/TCP/UDP/ICMP traffic
- Displays truncated payload (first 64 bytes)
- Real-time packet analysis
- Requires admin privileges

## 🚀 Usage

    sudo python3 packet_sniffer.py
    # Run sniffer
    sudo python3 packet_sniffer.py

    # Observe output
    [2024-05-20 14:35:22]
    Protocol: TCP
    Source: 192.168.1.15:54321
    Dest: 104.18.25.123:443
    Payload Preview:
    0000  17 03 03 01 5A  [...]

## ⚠️ Ethical Notice
All tools are provided **for educational purposes only**. Particularly note:
- Keylogger requires explicit user consent
- Packet sniffer should only be used on networks you own
- Never use these tools on unauthorized systems

## 📝 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details

---

*Submitted as part of Prodigy Infotech internship program requirements*
