# Simple File Encryption/Decryption in Python

In this tutorial, we will learn how to build a simple file encryption and decryption script using basic encryption methods like the Caesar Cipher and XOR encryption. These methods are easy to implement and help you understand the fundamental concepts of encryption. We will also briefly introduce an advanced challenge where you can try implementing the **Vigenère Cipher** to enhance security.

---

## What You Will Learn:
- File handling in Python.
- Basic encryption algorithms: Caesar Cipher and XOR encryption.
- String manipulation techniques for encryption and decryption.
- Challenge: Implementing the Vigenère Cipher.

---

## Part 1: Caesar Cipher for File Encryption/Decryption

### What is a Caesar Cipher?

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It works by shifting the letters of the plaintext by a fixed number of positions down the alphabet. For example, shifting the letter 'A' by 3 would give us 'D'.

### Implementing Caesar Cipher

Here’s a basic implementation of a Caesar Cipher that encrypts and decrypts text files.

```python
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        data = file.read()

    encrypted_data = caesar_cipher(data, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_data)

    print(f"File '{input_file}' has been encrypted and saved as '{output_file}'.")

def decrypt_file(input_file, output_file, shift):
    # To decrypt, we simply use the negative shift
    encrypt_file(input_file, output_file, -shift)
    print(f"File '{input_file}' has been decrypted and saved as '{output_file}'.")

# Example usage
shift_value = 3
encrypt_file('plaintext.txt', 'encrypted.txt', shift_value)
decrypt_file('encrypted.txt', 'decrypted.txt', shift_value)
```

### Explanation:
- **caesar_cipher**: This function shifts each character by the `shift` value. Non-alphabetical characters remain unchanged.
- **encrypt_file**: Reads the contents of a file, encrypts the text, and writes the encrypted text to a new file.
- **decrypt_file**: It reverses the encryption by using the negative of the shift value.

### How to Use:
1. Create a text file named `plaintext.txt`.
2. Run the script with a chosen shift value.
3. The script will generate `encrypted.txt` and `decrypted.txt` for comparison.

---

## Part 2: XOR Encryption for File Encryption/Decryption

### What is XOR Encryption?

XOR encryption is another simple encryption technique that uses the **exclusive or (XOR)** bitwise operation. This method can be more secure than the Caesar Cipher since the key can be more complex (not just a simple shift).

### Implementing XOR Encryption

```python
def xor_cipher(text, key):
    encrypted_text = ''.join(chr(ord(c) ^ key) for c in text)
    return encrypted_text

def encrypt_file_xor(input_file, output_file, key):
    with open(input_file, 'r') as file:
        data = file.read()

    encrypted_data = xor_cipher(data, key)

    with open(output_file, 'w') as file:
        file.write(encrypted_data)

    print(f"File '{input_file}' has been XOR encrypted and saved as '{output_file}'.")

def decrypt_file_xor(input_file, output_file, key):
    encrypt_file_xor(input_file, output_file, key)
    print(f"File '{input_file}' has been XOR decrypted and saved as '{output_file}'.")

# Example usage
key_value = 123
encrypt_file_xor('plaintext.txt', 'xor_encrypted.txt', key_value)
decrypt_file_xor('xor_encrypted.txt', 'xor_decrypted.txt', key_value)
```

### Explanation:
- **xor_cipher**: This function encrypts or decrypts text using a key with XOR operation.
- **encrypt_file_xor**: Encrypts a file using XOR encryption.
- **decrypt_file_xor**: Decrypts a file by performing the XOR operation again with the same key.

---

## Part 3: Saving and Loading Files in a User-Friendly Way

We’ve seen how to encrypt and decrypt files. Now let’s improve the script by adding user input for filenames and encryption keys.

```python
def main():
    print("Welcome to the Simple File Encryption/Decryption Tool")
    print("Choose an option:")
    print("1. Encrypt a file with Caesar Cipher")
    print("2. Decrypt a file with Caesar Cipher")
    print("3. Encrypt a file with XOR Encryption")
    print("4. Decrypt a file with XOR Encryption")

    choice = input("Enter your choice (1-4): ")
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    if choice in ['1', '2']:
        shift = int(input("Enter the shift value (Caesar Cipher): "))
        if choice == '1':
            encrypt_file(input_file, output_file, shift)
        else:
            decrypt_file(input_file, output_file, shift)
    elif choice in ['3', '4']:
        key = int(input("Enter the XOR key (an integer): "))
        if choice == '3':
            encrypt_file_xor(input_file, output_file, key)
        else:
            decrypt_file_xor(input_file, output_file, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
```

---

## Challenge: Implementing the Vigenère Cipher

For more advanced encryption, try implementing the **Vigenère Cipher**. It’s a polyalphabetic substitution cipher that uses a keyword to encrypt the message. Instead of using a single shift (like in Caesar Cipher), it shifts each letter by a different amount based on the keyword.

Here’s the general idea:

1. Repeat the keyword to match the length of the plaintext.
2. Use the position of the keyword letters to determine the shift for each letter of the plaintext.

---

## Part 4: Advanced Tools (Coming Soon)

In future tutorials, we will provide more advanced encryption tools with extra features like:
- **AES (Advanced Encryption Standard)** encryption.
- **RSA** for public and private key encryption.
- **Hybrid encryption** techniques that combine symmetric and asymmetric algorithms.

Stay tuned for more!

---

## Conclusion

In this tutorial, we learned the basics of file encryption and decryption using the Caesar Cipher and XOR encryption. These techniques are simple yet effective ways to get started with encryption in Python. You can take it a step further by implementing the Vigenère Cipher or other more advanced encryption methods.

Feel free to expand this project by adding password-protection, file format support, or even a graphical user interface (GUI) for easier use!
