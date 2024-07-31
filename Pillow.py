from PIL import Image
import random

def swap_pixels(image):
    """Randomly swap pixel values."""
    pixels = list(image.getdata())
    width, height = image.size
    total_pixels = width * height

    # Number of swaps
    num_swaps = total_pixels // 2

    for _ in range(num_swaps):
        i, j = random.sample(range(total_pixels), 2)
        pixels[i], pixels[j] = pixels[j], pixels[i]

    image.putdata(pixels)
    return image

def xor_pixels(image, key):
    """Apply XOR operation to each pixel with a given key."""
    pixels = list(image.getdata())
    new_pixels = [(pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key) for pixel in pixels]
    image.putdata(new_pixels)
    return image

def encrypt_image(image_path, output_path, method, key=None):
    """Encrypt an image using the specified method."""
    image = Image.open(image_path)

    if method == 'swap':
        encrypted_image = swap_pixels(image)
    elif method == 'xor' and key is not None:
        encrypted_image = xor_pixels(image, key)
    else:
        raise ValueError("Invalid method or missing key for XOR method")

    encrypted_image.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
encrypt_image('input_image.jpg', 'encrypted_image.jpg', method='swap')
encrypt_image('input_image.jpg', 'encrypted_image_xor.jpg', method='xor', key=123)

