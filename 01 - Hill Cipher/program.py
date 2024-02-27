#Reyes Mendoza Miriam Guadalupe
#Criptografía - Grupo 2
#Semestre 2024-2
#Facultad de Ingeniería
#Universidad Nacional Autónoma de México

#01 - Hill Cipher 

import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

    import numpy as np

    def hill_cipher_encryption(plaintext, key):
        # Convert plaintext and key to uppercase
        plaintext = plaintext.upper()
        key = key.upper()

        # Remove any non-alphabetic characters from plaintext
        plaintext = ''.join(filter(str.isalpha, plaintext))

        # Pad the plaintext if its length is not a multiple of the key size
        if len(plaintext) % len(key) != 0:
            plaintext += 'X' * (len(key) - len(plaintext) % len(key))

        # Create the key matrix
        key_matrix = np.array([ord(c) - ord('A') for c in key])
        key_matrix = key_matrix.reshape(int(len(key_matrix) ** 0.5), -1)

        # Encrypt the plaintext using the key matrix
        ciphertext = ''
        for i in range(0, len(plaintext), len(key)):
            block = np.array([ord(c) - ord('A') for c in plaintext[i:i+len(key)]])
            block = block.reshape(-1, 1)
            encrypted_block = np.dot(key_matrix, block) % 26
            ciphertext += ''.join(chr(c + ord('A')) for c in encrypted_block.flatten())

        return ciphertext

    def hill_cipher_decryption(ciphertext, key):
        # Convert ciphertext and key to uppercase
        ciphertext = ciphertext.upper()
        key = key.upper()

        # Remove any non-alphabetic characters from ciphertext
        ciphertext = ''.join(filter(str.isalpha, ciphertext))

        # Create the key matrix
        key_matrix = np.array([ord(c) - ord('A') for c in key])
        key_matrix = key_matrix.reshape(int(len(key_matrix) ** 0.5), -1)

        # Calculate the inverse of the key matrix
        det = np.linalg.det(key_matrix)
        det_inv = pow(int(round(det)) % 26, -1, 26)
        key_matrix_inv = (det_inv * np.round(det * np.linalg.inv(key_matrix)) % 26).astype(int)

        # Decrypt the ciphertext using the inverse key matrix
        plaintext = ''
        for i in range(0, len(ciphertext), len(key)):
            block = np.array([ord(c) - ord('A') for c in ciphertext[i:i+len(key)]])
            block = block.reshape(-1, 1)
            decrypted_block = np.dot(key_matrix_inv, block) % 26
            plaintext += ''.join(chr(c + ord('A')) for c in decrypted_block.flatten())

        return plaintext

    # Read the input from the file
    input_lines = lines[:-1]
    mode = input_lines[0].strip()
    text = input_lines[1].strip()
    key = input_lines[2].strip()

    # Perform encryption or decryption based on the mode
    if mode == 'c':
        result = hill_cipher_encryption(text, key)
    else:
        result = hill_cipher_decryption(text, key)

    # Print the result
    print(result)