openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -in private_key.pem -pubout -out public_key.pem
openssl req -new -x509 -key private_key.pem -out self_signed_certificate.pem -days 365
openssl pkcs12 -export -inkey private_key.pem -in self_signed_certificate.pem -out keystore.pfx
openssl pkcs12 -info -in keystore.pfx
openssl req -new -key private_key.pem -out miriamyi01.github.io.csr
openssl pkcs12 -export -inkey private_key.pem -in MIRIAM-2024-05-11-03328.pem -out keystore1.pfx
openssl pkcs12 -info -in keystore1.pfx