def encrypt(text, s):
    cipher_t = ""
    
    for char in text:
        if char.lower() == 'n' or char == ' ':
            continue  # Skip 'n', 'N', and spaces

        if char.isupper():
            cipher_t += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            cipher_t += chr((ord(char) + s - 97) % 26 + 97)
        else:
            cipher_t += char  # Keep non-alphabet characters unchanged
    
    return cipher_t

def decrypt(cipher_t, s):
    plain_t = ""
    cipher_index = 0
    
    for char in original_text:
        if char == ' ':
            plain_t += ' '  # Add space back to the plaintext
        elif char.lower() == 'n':
            plain_t += 'n'  # Add 'n' or 'N' back to the plaintext
        else:
            if char.isupper():
                plain_t += chr((ord(cipher_t[cipher_index]) - s - 65) % 26 + 65)
            elif char.islower():
                plain_t += chr((ord(cipher_t[cipher_index]) - s - 97) % 26 + 97)
            else:
                plain_t += cipher_t[cipher_index]  # Keep non-alphabet characters unchanged
            cipher_index += 1
    
    return plain_t

original_text = input("Enter the text to encrypt: ")
s = 3

encrypted_text = encrypt(original_text, s)

print("Text: " + original_text)
print("Cipher: " + encrypted_text)
print("Plain: " + decrypt(encrypted_text, s))
