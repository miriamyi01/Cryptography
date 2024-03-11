# Reyes Mendoza Miriam Guadalupe
# Criptografía - Grupo 2
# Semestre 2024-2
# Facultad de Ingeniería
# Universidad Nacional Autónoma de México

# PRACTICAL SESSION 2 – RC4

# Leer líneas de una entrada estándar y almacenarlas en una lista
import fileinput

# Leer archivo de pruebas en línea
lines = []
for line in fileinput.input():
    lines.append(line)

#Leer archivo de pruebas local
'''with open('C:\\Users\\miria\\Desktop\\prueba.txt', 'r') as file:
    lines = file.readlines()'''

#Implementación de RC4
def rc4(plaintext, key):
    """
    Realiza el cifrado RC4 utilizando una clave dada.

    Parámetros:
    - plaintext: El texto plano a cifrar.
    - key: La clave para el cifrado.

    Regresa:
    - El texto cifrado resultante.
    """

    # Key Scheduling Algorithm - KSA
    S = list(range(256))
    j = 0
    keylength = len(key)
    for i in range(255):
        j = (j + S[i] + ord(key[i % keylength])) % 256
        S[i], S[j] = S[j], S[i]


    # Pseudo-random generation algorithm - PRGA
    i = 0
    j = 0
    keystream = []
    for _ in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystream.append(k)

    # XOR del keystream con el texto plano
    ciphertext = ''.join(chr(ord(c) ^ keystream[i]) for i, c in enumerate(plaintext))


    # Convertir el keystream a hexadecimal
    keystream = ''.join(format(x, '02x') for x in keystream).upper()
    
    # Convertir el texto cifrado a hexadecimal
    ciphertext = ''.join(format(ord(x), '02x') for x in ciphertext).upper()

    # Imprimir la clave, el keystream, el texto plano y el texto cifrado
    '''print("\nKEY:", key)
    print("KEYSTREAM:", keystream)
    print("\nPLAINTEXT:", plaintext)
    print("CIPHERTEXT:", ciphertext, "\n")'''

    return ciphertext


# Leer la entrada del archivo
input_lines = lines[:2]
text = input_lines[0].strip()
key = input_lines[1].strip()

# Realizar cifrado
result = rc4(key, text)

# Imprimir el resultado
print(result)