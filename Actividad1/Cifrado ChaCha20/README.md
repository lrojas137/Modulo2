# Programa de cifrado simétrico con ChaCha20

Este programa muestra cómo cifrar y descifrar un mensaje usando **ChaCha20** con Python.

## ¿Qué hace este programa?

El programa:

1. Genera una **clave secreta** de 32 bytes.
2. Genera un **nonce** de 16 bytes.
3. Define un mensaje en formato bytes.
4. Crea el cifrador ChaCha20.
5. Cifra el mensaje.
6. Muestra el mensaje cifrado.
7. Descifra el mensaje usando la misma clave y el mismo nonce.
8. Muestra el mensaje original recuperado.

## Requisitos

- Python 3.8 o superior
- Librería `cryptography`

## Instalación

Abre una terminal en esta carpeta y ejecuta:

```bash
pip install cryptography
```

<img width="929" height="319" alt="image" src="https://github.com/user-attachments/assets/8f5b4484-ae97-4933-8b1d-64498fbb7bf4" />


## Cómo ejecutar el programa

El archivo se llama `chacha20.py`, ejecutar:

```bash
python chacha20.py
```

## Resultado esperado

Al ejecutar el programa, se mostrará:

- un **mensaje cifrado** en forma de bytes no legibles,
- y luego el **mensaje descifrado**, igual al original.

Ejemplo:

```text
Mensaje cifrado:
b'...'

Mensaje descifrado:
Hola Ingeniero Luis, mensaje secreto con ChaCha20
```

<img width="940" height="86" alt="image" src="https://github.com/user-attachments/assets/3b77143d-b085-4492-b109-bc3ccd467c69" />


## Explicación general

- ChaCha20 es un algoritmo de **cifrado simétrico**.
- Usa la **misma clave** para cifrar y descifrar.
- También necesita un **nonce**, que es un valor adicional requerido por el algoritmo.
- A diferencia de AES-CBC, **no necesita padding**, porque funciona como un **cifrador de flujo**.

## Pruebas recomendadas

### 1. Ejecución normal
Comprueba que el mensaje se cifra y luego se recupera correctamente.

<img width="929" height="133" alt="image" src="https://github.com/user-attachments/assets/50fb0ec5-9b4a-4016-a60f-cf18d69473b9" />


### 2. Prueba con clave diferente
Cambia la clave en la parte de descifrado por otra distinta. El resultado será incorrecto o dará error al convertirlo a texto.

<img width="929" height="169" alt="image" src="https://github.com/user-attachments/assets/0d33ce1d-356b-4727-a1e6-8ed3bc3f9a71" />


### 3. Prueba sin clave
Intenta descifrar sin proporcionar una clave válida. El programa debe generar un error.

<img width="1101" height="227" alt="image" src="https://github.com/user-attachments/assets/1a873704-98e7-4c74-a5e7-ee4b7e5e7d40" />


## Conclusión

Este programa demuestra el funcionamiento básico de **ChaCha20**, donde la misma clave y el mismo nonce permiten cifrar y recuperar correctamente la información.

