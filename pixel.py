#task2-pixel manipulation (encrypt and decrypt image )

import cv2

# Load an image
image = cv2.imread('rose_image.jpeg')

# Loop through each pixel in the image
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        # Get the pixel value at (x, y)
        pixel = image[y, x]

        # Example: Invert pixel color (for grayscale images)
        inverted_pixel = 255 - pixel

        # Set the pixel value to the inverted color
        image[y, x] = inverted_pixel

# Save the manipulated image
cv2.imwrite('encrypted_image.jpeg', image)

# Load the manipulated image
image = cv2.imread('encrypted_image.jpeg')

# Loop through each pixel in the image
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        # Get the pixel value at (x, y)
        pixel = image[y, x]

        # Revert pixel color (undo inversion)
        original_pixel = 255 - pixel

        # Set the pixel value to the original color
        image[y, x] = original_pixel

# Save the decrypted image
cv2.imwrite('decrypted_image.jpeg', image)