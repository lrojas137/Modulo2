from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# 1️ Generar clave secreta (32 bytes = AES-256)
key = os.urandom(32)

# 2️ Generar vector de inicialización
iv = os.urandom(16)

# 3️ Mensaje original
mensaje = b"Hola David, mensaje secreto con AES"

# 4️ Aplicar padding al mensaje
padder = padding.PKCS7(128).padder()
mensaje_padded = padder.update(mensaje) + padder.finalize()

# 5 Crear cifrador AES
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

# 6️ Cifrar mensaje
ciphertext = encryptor.update(mensaje_padded) + encryptor.finalize()

print("Mensaje cifrado:")
print(ciphertext)

# 7 Descifrar mensaje

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()

mensaje_descifrado = decryptor.update(ciphertext) + decryptor.finalize()

# 8 Quitar padding

unpadder = padding.PKCS7(128).unpadder()
mensaje_final = unpadder.update(mensaje_descifrado) + unpadder.finalize()


print("\nMensaje descifrado:")
print(mensaje_final.decode())

'''

# 7 Crear una clave incorrecta
wrong_key = os.urandom(32)

# 8. Intentar descifrar con la clave incorrecta
cipher = Cipher(algorithms.AES(wrong_key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
mensaje_descifrado = decryptor.update(ciphertext) + decryptor.finalize()

# 9. Intentar quitar padding
try:
    unpadder = padding.PKCS7(128).unpadder()
    mensaje_final = unpadder.update(mensaje_descifrado) + unpadder.finalize()

    print("\nMensaje descifrado:")
    print(mensaje_final.decode())
except Exception as e:
    print("\nNo se pudo descifrar correctamente con una clave incorrecta.")
    print("Error:", e)
    
'''
