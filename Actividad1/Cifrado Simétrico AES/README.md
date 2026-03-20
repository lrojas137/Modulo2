# Cifrado Simétrico AES
# Programa de cifrado simétrico con AES

Este programa muestra cómo cifrar y descifrar un mensaje usando **AES-256 en modo CBC** con Python.

## ¿Qué hace este programa?

El programa:

1. Genera una **clave secreta** aleatoria de 32 bytes.
2. Genera un **vector de inicialización (IV)** de 16 bytes.
3. Define un mensaje en formato bytes.
4. Aplica **padding PKCS7** al mensaje.
5. Cifra el mensaje con **AES-256-CBC**.
6. Muestra el mensaje cifrado.
7. Descifra el mensaje usando la misma clave y el mismo IV.
8. Quita el padding y muestra el mensaje original.

## Requisitos

- Python 3.8 o superior
- Librería `cryptography`

## Instalación

Abre una terminal en esta carpeta y ejecuta:

```bash
pip install cryptography
```
<img width="929" height="319" alt="image" src="https://github.com/user-attachments/assets/bf0e91dd-7800-4c48-9c68-c018a9ca22b1" />


## Cómo ejecutar el programa

El archivo se llama `asimetrico.py`, ejecutar en la terminal de Visual Studio Code:

```bash
python asimetrico.py
```

## Resultado esperado

Al ejecutar el programa, se mostrará:

- un **mensaje cifrado** en forma de bytes no legibles,
- y luego el **mensaje descifrado**, que debe coincidir con el texto original.

Ejemplo:

```text
Mensaje cifrado:
b'...'

Mensaje descifrado:
Hola David, mensaje secreto con AES
```
<img width="929" height="78" alt="image" src="https://github.com/user-attachments/assets/b7631e46-4570-4db4-aac6-800a8040bf85" />

## Explicación general

- La clave de **32 bytes** equivale a **256 bits**, por eso se usa **AES-256**.
- El IV de **16 bytes** es necesario porque AES trabaja con bloques de **128 bits**.
- Se usa **padding** porque AES-CBC necesita que el mensaje tenga un tamaño múltiplo de 16 bytes.
- Para descifrar correctamente, se necesita la **misma clave** y el **mismo IV**.

## Pruebas recomendadas

### 1. Ejecución normal
Compruebar que el mensaje se cifra y luego se recupera correctamente.

<img width="929" height="102" alt="image" src="https://github.com/user-attachments/assets/93b21113-8983-4088-a1b0-440a3cd98f4c" />


### 2. Prueba con clave diferente
Cambiar la clave en la parte de descifrado por otra distinta. El mensaje no podrá recuperarse correctamente.

<img width="929" height="83" alt="image" src="https://github.com/user-attachments/assets/d883b5af-5f47-4056-9875-f4402e59b020" />


### 3. Prueba sin clave
Intentar descifrar sin proporcionar una clave válida. El programa debe generar un error.

<img width="1220" height="260" alt="image" src="https://github.com/user-attachments/assets/41f18946-e529-4b2e-a9e8-bd0763d5746b" />


## Conclusión

Este programa demuestra el funcionamiento básico del **cifrado simétrico con AES**
