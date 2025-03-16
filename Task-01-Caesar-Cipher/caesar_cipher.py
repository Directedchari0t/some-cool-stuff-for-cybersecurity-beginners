def caesar_cipher(text, shift):
    result = []
    # Normalize shift to handle values over 26 and negative shifts
    shift = shift % 26
    for char in text:
        if char.isupper():
            # Handle uppercase letters
            shifted = ord(char) + shift
            if shifted > ord('Z'):
                shifted -= 26
            elif shifted < ord('A'):
                shifted += 26
            result.append(chr(shifted))
        elif char.islower():
            # Handle lowercase letters
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= 26
            elif shifted < ord('a'):
                shifted += 26
            result.append(chr(shifted))
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return ''.join(result)

# Get user input
operation = input("Enter operation (encrypt/decrypt): ").lower()
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Adjust shift for decryption
if operation == "decrypt":
    shift = -shift

# Process the message
processed_text = caesar_cipher(message, shift)
print(f"Result: {processed_text}")
