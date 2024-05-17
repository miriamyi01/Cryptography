openssl dgst -sha256 -sign private_key.pem -out firma.sha256 Texto.txt
openssl dgst -sha256 -verify public_key.pem -signature firma.sha256 Texto.txt
openssl enc -aes-256-cbc -salt -in Texto.txt -out cifrado.txt -k miriam1234
openssl enc -d -aes-256-cbc -in cifrado.txt -out descifrado.txt -k miriam1234
openssl dgst -sha512 -hex Texto.txt
openssl dgst -sha512 -sign private_key.pem -out hash.sha512 Texto.txt
openssl dgst -sha512 -hex -verify public_key.pem -signature hash.sha512 Texto.txt