def rail_fence_cipher(plain_text, rails):
    # Initialize variables
    len_text = len(plain_text)
    rail = [['' for _ in range(len_text)] for _ in range(rails)]
    down = False
    row, col = 0, 0
    
    # Fill the rail matrix
    for i in range(len_text):
        if row == 0 or row == rails - 1:
            down = not down
        rail[row][col] = plain_text[i]
        col += 1
        if down:
            row += 1
        else:
            row -= 1
    
    # Construct the cipher text
    cipher_text = []
    for i in range(rails):
        for j in range(len_text):
            if rail[i][j] != '':
                cipher_text.append(rail[i][j])
    
    return ''.join(cipher_text)

if __name__ == "__main__":
    print("****** RAILFENCE CIPHER ******")
    plain_text = input("Enter the plaintext: ")
    rails = int(input("Enter the number of Rails: "))
    cipher_text = rail_fence_cipher(plain_text, rails)
    print("The Cipher text is:\n" + cipher_text)
    print("Cipher text length: " + str(len(cipher_text)))