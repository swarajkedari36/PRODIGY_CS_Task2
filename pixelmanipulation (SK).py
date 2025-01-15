from PIL import Image
import numpy as np

print("------------- Image Encryption Tool --------------")

def encrypt_image(image_path, key):
    # Opening the image
    original_image = Image.open(image_path)

    # Converting the image to a NumPy array
    image_array = np.array(original_image)

    # Encrypting the image
    encrypted_image_array = (image_array + key) % 256

    # Converting the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_image_array.astype('uint8'))

    # Saving the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

def encrypt_choice():
    key = int(input("Enter encryption key: "))
    image_location = "D:\\OneDrive\\Pictures\\back pic 2\\task 2 imgh.jpg"

    try:
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")
        return False
    return True

def decrypt_image(image_path, key):
    # Opening the image
    encrypted_image = Image.open(image_path)

    # Converting the image to a NumPy array
    image_array = np.array(encrypted_image)

    # Decrypting the image
    decrypted_image_array = (image_array - key) % 256

    # Converting the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_image_array.astype('uint8'))

    # Saving the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

def decrypt_choice():
    key = int(input("Enter decryption key: "))
    image_location = "D:\\OneDrive\\Pictures\\back pic 2\\task 2 imgh.jpg"

    try:
        decrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    if choice == 'e':
        encrypt_choice()
    elif choice == 'd':
        decrypt_choice()
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        main()

if __name__ == "__main__":
    main()