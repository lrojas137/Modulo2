# Programa de cifrado asimétrico con RSA

Este programa muestra cómo cifrar y descifrar un mensaje usando **RSA** con Python.

## ¿Qué hace este programa?

El programa:

1. Genera una **clave privada RSA**.
2. Obtiene la **clave pública** asociada.
3. Define un mensaje en formato bytes.
4. Cifra el mensaje con la **clave pública**.
5. Muestra el mensaje cifrado.
6. Descifra el mensaje con la **clave privada**.
7. Muestra el mensaje original recuperado.

## Requisitos

- Python 3.8 o superior
- Librería `cryptography`

## Instalación

Abre una terminal en esta carpeta y ejecuta:

```bash
pip install cryptography
```
<img width="929" height="319" alt="image" src="https://github.com/user-attachments/assets/2b6d3405-0b3b-4cea-9314-e41201b12765" />

## Cómo ejecutar el programa

El archivo se llama `asimetrico.py`, ejecuta:

```bash
python asimetrico.py
```

## Resultado esperado

Al ejecutar el programa, se mostrará:

- un **mensaje cifrado** en forma de bytes,
- y luego el **mensaje descifrado**, igual al original.

Ejemplo:

```text
Mensaje cifrado:
b'...'

Mensaje descifrado:
Hola Ingeniero Luis, este es un mensaje secreto
```
<img width="929" height="154" alt="image" src="https://github.com/user-attachments/assets/b7b4c7bd-d094-442d-bbc6-4a4a89ac6358" />


## Explicación general

- RSA es un algoritmo de **cifrado asimétrico**.
- Se usan **dos claves diferentes**:
  - **clave pública** para cifrar,
  - **clave privada** para descifrar.
- El programa usa un tamaño de clave de **2048 bits**, que es un valor común y seguro.
- También usa **OAEP con SHA-256**, que mejora la seguridad del cifrado.

## Pruebas recomendadas

### 1. Ejecución normal
Compruebar que el mensaje se cifra con la clave pública y se recupera con la clave privada.

<img width="929" height="154" alt="image" src="https://github.com/user-attachments/assets/b1129d88-a0c5-4862-9214-c6108a56aa80" />


### 2. Prueba con clave privada diferente
Generar otra clave privada distinta e intentar descifrar con ella. El proceso debe fallar.

<img width="929" height="178" alt="image" src="https://github.com/user-attachments/assets/ee17fe93-c6dd-488d-ba94-ca84c327e46a" />


### 3. Prueba sin clave privada
Intentar descifrar sin proporcionar una clave privada válida. El programa debe generar un error.

<img width="1057" height="91" alt="image" src="https://github.com/user-attachments/assets/7fb36ef2-6643-49ae-9f91-6c943c0158df" />


## Conclusión

Este programa demuestra el funcionamiento del **cifrado asimétrico con RSA**, donde la clave pública se usa para proteger el mensaje y solo la clave privada correspondiente permite recuperarlo.

