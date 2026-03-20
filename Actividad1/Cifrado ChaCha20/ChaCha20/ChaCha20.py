from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

# 1. Generar clave secreta (32 bytes)
key = os.urandom(32)

# 2. Generar nonce
nonce = os.urandom(16)

# 3. Mensaje original
mensaje = b"Hola Ingeniero Luis, mensaje secreto con ChaCha20"

# 4. Crear cifrador ChaCha20
cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
encryptor = cipher.encryptor()

# 5. Cifrar mensaje
ciphertext = encryptor.update(mensaje) + encryptor.finalize()

print("Mensaje cifrado:")
print(ciphertext)

# 6. Descifrar mensaje
cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
decryptor = cipher.decryptor()

mensaje_descifrado = decryptor.update(ciphertext) + decryptor.finalize()

print("\nMensaje descifrado:")
print(mensaje_descifrado.decode())

'''

# 6. Crear una clave diferente
wrong_key = os.urandom(32)

# 7. Intentar descifrar con la clave incorrecta
cipher = Cipher(algorithms.ChaCha20(wrong_key, nonce), mode=None, backend=default_backend())
decryptor = cipher.decryptor()

mensaje_descifrado = decryptor.update(ciphertext) + decryptor.finalize()

# 8. Intentar mostrar el resultado
try:
    print("\nMensaje descifrado:")
    print(mensaje_descifrado.decode())
except Exception as e:
    print("\nNo se pudo recuperar correctamente el mensaje con una clave diferente.")
    print("Resultado en bytes:", mensaje_descifrado)
    print("Error:", e)
'''
