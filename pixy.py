from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Ensure key is within the range of 0-255
    key = key % 256

    # Encrypt the image by XORing each pixel with the key
    encrypted_image_array = image_array ^ key

    # Convert back to image and save
    encrypted_image = Image.fromarray(encrypted_image_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_image_path, output_path, key):
    # Decrypting is the same process as encrypting since XOR is a reversible operation
    encrypt_image(encrypted_image_path, output_path, key)

# Example usage
key = 123  # Example key
encrypt_image('rose_image.jpeg', 'encrypted_image.jpeg', key)
decrypt_image('encrypted_image.jpeg', 'decrypted_image.jpeg', key)