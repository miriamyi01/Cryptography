type private_key.pem
type public_key.pem
type texto.txt
openssl dgst -sha256 -sign private_key.pem -out firma.sha256 texto.txt
type firma.sha256
openssl dgst -sha256 -verify public_key.pem -signature firma.sha256 texto.txt
openssl enc -aes-256-cbc -salt -in texto.txt -out cifrado.txt -k miriam1234 -pbkdf2
type cifrado.txt
openssl enc -d -aes-256-cbc -in cifrado.txt -out descifrado.txt -k miriam1234 -pbkdf2
type descifrado.txt
openssl dgst -sha512 -hex texto.txt
openssl dgst -sha512 -sign private_key.pem -out hash.sha512 texto.txt
type hash.sha512
openssl dgst -sha512 -hex -verify public_key.pem -signature hash.sha512 texto.txt