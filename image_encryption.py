from PIL import Image

def swap_rb(pixel):
    """Swap Red and Blue channels: (R, G, B) -> (B, G, R)"""
    r, g, b = pixel
    return (b, g, r)

def add_key(pixel, key):
    """Add key to each channel (mod 256)"""
    r, g, b = pixel
    return ((r + key) % 256, (g + key) % 256, (b + key) % 256)

def subtract_key(pixel, key):
    """Subtract key from each channel (mod 256)"""
    r, g, b = pixel
    return ((r - key) % 256, (g - key) % 256, (b - key) % 256)

def xor_key(pixel, key):
    """XOR each channel with key"""
    r, g, b = pixel
    return (r ^ key, g ^ key, b ^ key)

def process_image(input_path, output_path, mode, operation, key=None):
    # Open image and convert to RGB
    img = Image.open(input_path).convert("RGB")
    pixels = list(img.getdata())

    new_pixels = []

    for p in pixels:
        if operation == "swap":
            new_p = swap_rb(p)
        elif operation == "add":
            if mode == "encrypt":
                new_p = add_key(p, key)
            else:  # decrypt
                new_p = subtract_key(p, key)
        elif operation == "xor":
            # XOR is same for encrypt & decrypt
            new_p = xor_key(p, key)
        else:
            raise ValueError("Unknown operation.")
        new_pixels.append(new_p)

    # Create new image with processed pixels
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)

    print(f"{mode.capitalize()}ed image saved as: {output_path}")


def main():
    print("=== Simple Image Encryption Tool (Pixel Manipulation) ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
        return

    print("\nOperations:")
    print("1. Swap R and B channels (swap)")
    print("2. Add/Subtract key (add)")
    print("3. XOR with key (xor)")
    op_choice = input("Choose operation (swap/add/xor): ").strip().lower()

    if op_choice not in ["swap", "add", "xor"]:
        print("Invalid operation.")
        return

    input_path = input("Enter input image path (e.g., input.png): ").strip()
    output_path = input("Enter output image path (e.g., output.png): ").strip()

    key = None
    if op_choice in ["add", "xor"]:
        try:
            key = int(input("Enter key (0–255): ").strip())
            if not (0 <= key <= 255):
                print("Key must be between 0 and 255.")
                return
        except ValueError:
            print("Key must be an integer.")
            return

    process_image(input_path, output_path, mode, op_choice, key)

if __name__ == "__main__":
    main()
