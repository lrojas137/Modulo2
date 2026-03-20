from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1️ Generar claves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# 2️ Mensaje a cifrar
mensaje = b"Hola Ingeniero Luis, este es un mensaje secreto"

# 3️ Cifrar usando la clave pública
ciphertext = public_key.encrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensaje cifrado:")
print(ciphertext)

# 4. Generar otra clave privada diferente
other_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 5. Intentar descifrar con la clave privada incorrecta
try:
    plaintext = other_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("\nMensaje descifrado:")
    print(plaintext.decode())

except Exception as e:
    print("\nNo se pudo descifrar con una clave privada diferente.")
    print("Error:", e)
