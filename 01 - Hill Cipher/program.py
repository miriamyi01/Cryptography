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
        # Convertir el texto plano y la clave a mayúsculas
        plaintext = plaintext.upper()
        key = key.upper()

        # Eliminar cualquier carácter no alfabético del texto plano
        plaintext = ''.join(filter(str.isalpha, plaintext))

        # Rellenar el texto plano si su longitud no es un múltiplo del tamaño de la clave
        if len(plaintext) % len(key) != 0:
            plaintext += 'X' * (len(key) - len(plaintext) % len(key))

        # Crear la matriz clave
        key_matrix = np.array([ord(c) - ord('A') for c in key])
        key_matrix = key_matrix.reshape(int(len(key_matrix) ** 0.5), -1)

        # Cifrar el texto plano usando la matriz clave
        ciphertext = ''
        for i in range(0, len(plaintext), len(key)):
            block = np.array([ord(c) - ord('A') for c in plaintext[i:i+len(key)]])
            block = block.reshape(-1, 1)
            encrypted_block = np.dot(key_matrix, block) % 26
            ciphertext += ''.join(chr(c + ord('A')) for c in encrypted_block.flatten())

        return ciphertext

    def hill_cipher_decryption(ciphertext, key):
        # Convertir el texto cifrado y la clave a mayúsculas
        ciphertext = ciphertext.upper()
        key = key.upper()

        # Eliminar cualquier carácter no alfabético del texto cifrado
        ciphertext = ''.join(filter(str.isalpha, ciphertext))

        # Crear la matriz clave
        key_matrix = np.array([ord(c) - ord('A') for c in key])
        key_matrix = key_matrix.reshape(int(len(key_matrix) ** 0.5), -1)

        # Calcular la inversa de la matriz clave
        det = np.linalg.det(key_matrix)
        det_inv = pow(int(round(det)) % 26, -1, 26)
        key_matrix_inv = (det_inv * np.round(det * np.linalg.inv(key_matrix)) % 26).astype(int)

        # Descifrar el texto cifrado usando la matriz clave inversa
        plaintext = ''
        for i in range(0, len(ciphertext), len(key)):
            block = np.array([ord(c) - ord('A') for c in ciphertext[i:i+len(key)]])
            block = block.reshape(-1, 1)
            decrypted_block = np.dot(key_matrix_inv, block) % 26
            plaintext += ''.join(chr(c + ord('A')) for c in decrypted_block.flatten())

        return plaintext

   # Leer la entrada del archiv
    input_lines = lines[:-1]
    mode = input_lines[0].strip()
    text = input_lines[1].strip()
    key = input_lines[2].strip()

    # Realizar cifrado o descifrado según el modo
    if mode == 'c':
        result = hill_cipher_encryption(text, key)
    else:
        result = hill_cipher_decryption(text, key)

    # Imprimir el resultado
    print(result)