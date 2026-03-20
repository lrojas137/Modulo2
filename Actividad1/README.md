# Actividad de Cifrados en Python y PHP

Este repositorio contiene cuatro ejemplos básicos de criptografía en Python, desarrollados con la librería `cryptography` y uno en PHP.  
El objetivo es mostrar de forma sencilla cómo funcionan distintos tipos de cifrado y cómo se pueden implementar en programas pequeños.

## Contenido del repositorio

El repositorio está organizado en cuatro carpetas, una para cada programa:

- [AES](https://github.com/lrojas137/Modulo2/tree/main/Actividad1/Cifrado%20Sim%C3%A9trico%20AES)  
  Ejemplo de cifrado **simétrico** usando **AES-256**.

- [RSA](https://github.com/lrojas137/Modulo2/tree/main/Actividad1/Cifrado%20Asim%C3%A9trico%20RSA)  
  Ejemplo de cifrado **asimétrico** usando **RSA**.

- [ChaCha20](https://github.com/lrojas137/Modulo2/tree/main/Actividad1/Cifrado%20ChaCha20)  
  Ejemplo de cifrado **simétrico** usando **ChaCha20**.

- [PHP](https://github.com/lrojas137/Modulo2/tree/main/Actividad1/ProgramaPHP-SHA256)  
  Ejemplo de cifrado  usando **SHA-256** en PHP.

## Objetivo de la actividad

Con estos programas se busca:

- comprender la diferencia entre cifrado simétrico y asimétrico,
- observar cómo se cifra y descifra un mensaje,
- verificar que no es posible recuperar la información sin la clave correcta,
- y documentar el funcionamiento básico de cada algoritmo.

## Requisitos generales

Para ejecutar cualquiera de los programas se necesita:

- Python 3.8 o superior
- la librería `cryptography`
- XAMPP
- Visual Studio Code u otro IDE

### Instalación de la librería en python

```bash
pip install cryptography
