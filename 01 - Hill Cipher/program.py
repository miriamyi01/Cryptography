#Reyes Mendoza Miriam Guadalupe
#Criptografía - Grupo 2
#Semestre 2024-2
#Facultad de Ingeniería
#Universidad Nacional Autónoma de México

'''import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)'''

with open('C:\\Users\\miria\\Desktop\\prueba.txt', 'r') as file:
    lines = file.readlines()

def hill_cipher_encryption(plaintext, key):
    # Convertir el texto plano y la clave a mayúsculas
    plaintext = plaintext.upper()
    key = key.upper()

    # Eliminar cualquier carácter no alfabético del texto plano
    plaintext = ''.join(filter(str.isalpha, plaintext))

    # Convertir la clave en una matriz clave numérica de 2x2
    key_matrix = [[ord(key[0]) - 65, ord(key[1]) - 65],
                  [ord(key[2]) - 65, ord(key[3]) - 65]]
    
    # Imprimir la matriz clave
    # print("Matriz clave:")
    # for row in key_matrix:
    #    print(row)
    
    # Dividir el texto plano en bloques de dos letras
    plaintext_blocks = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    # Rellenar el último bloque si su longitud es menor que 2
    if len(plaintext_blocks[-1]) < 2:
        plaintext_blocks[-1] += 'X'

    # Convertir los bloques de texto plano a vectores numéricos
    plaintext_vectors = []
    for block in plaintext_blocks:
        vector = [ord(letter) - 65 for letter in block]
        plaintext_vectors.append(vector)

    # Imprimir los vectores numéricos del texto plano
    # print("Vectores numéricos del texto plano: ", plaintext_vectors)

    # Realizar la multiplicación de matrices para obtener los vectores de texto cifrado
    ciphertext_vectors = []
    for vector in plaintext_vectors:
        result_vector = [0, 0]
        for i in range(2):
            for j in range(2):
                result_vector[i] += key_matrix[j][i] * vector[j]
            result_vector[i] %= 26
        ciphertext_vectors.append(result_vector)

    # Imprimir los vectores resultantes de la multiplicación de matrices
    # print("Vectores de la multiplicación de matrices: ", ciphertext_vectors)

    # Convertir los vectores de texto cifrado a texto
    ciphertext = ""
    for vector in ciphertext_vectors:
        for i in vector:
            ciphertext += chr(i + 65)  # Convertir de número a letra

    # Eliminar las 'X' al final del texto cifrado
    # ciphertext = ciphertext.rstrip('X')

    # Devolver el texto cifrado
    return ciphertext


def hill_cipher_decryption(ciphertext, key):
    # Convertir el texto cifrado y la clave a mayúsculas
    ciphertext = ciphertext.upper()
    key = key.upper()

    # Eliminar cualquier carácter no alfabético del texto cifrado
    ciphertext = ''.join(filter(str.isalpha, ciphertext))


    return plaintext


# Leer la entrada del archivo
input_lines = lines[:3]
mode = input_lines[0].strip()
text = input_lines[1].strip()
key = input_lines[2].strip()

# Realizar cifrado o descifrado según el modo
if mode == 'C':
    result = hill_cipher_encryption(text, key)
elif mode == 'D':
    result = hill_cipher_decryption(text, key)

# Imprimir el resultado
print(result)