from PIL import Image
import hashlib
import random

def process_image(input_path, output_path, key):
    """Encrypt/decrypt image using XOR operations with a key-derived seed"""
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print("Error: Input file not found")
        return

    # Convert to RGB mode to ensure consistent processing
    img = img.convert('RGB')
    pixels = img.load()
    width, height = img.size

    # Generate seed from key using SHA-256 hash
    hash_bytes = hashlib.sha256(key.encode()).digest()
    seed = int.from_bytes(hash_bytes[:4], byteorder='big')
    random.seed(seed)

    # Process each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Generate random values for each color channel
            rand_r = random.randint(0, 255)
            rand_g = random.randint(0, 255)
            rand_b = random.randint(0, 255)
            
            # XOR operation with pixel values
            new_r = r ^ rand_r
            new_g = g ^ rand_g
            new_b = b ^ rand_b
            
            pixels[x, y] = (new_r, new_g, new_b)

    img.save(output_path)
    print(f"Operation completed. Image saved to {output_path}")

if __name__ == "__main__":
    print("Image Encryption/Decryption Tool")
    print("--------------------------------")
    
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = input("Enter encryption/decryption key: ")
    
    process_image(input_path, output_path, key)
