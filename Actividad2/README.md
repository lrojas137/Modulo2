# Actividad 5 del Modulo 2

# Taller: Implementación de Encabezados de Seguridad en Apache con XAMPP

## Descripción

Este repositorio contiene el desarrollo del taller de implementación de encabezados de seguridad en una página web local usando **Apache con XAMPP** y **Visual Studio Code**.

El objetivo fue configurar una página HTML básica y aplicar encabezados HTTP de seguridad desde el servidor web, verificando posteriormente su funcionamiento mediante herramientas de análisis como **DevTools** y **OWASP ZAP**.

---

## Objetivo del taller

Implementar y verificar los siguientes encabezados de seguridad en un servidor local Apache:

- `Content-Security-Policy`
- `X-Content-Type-Options`
- `X-XSS-Protection`
- `X-Frame-Options`
- `Strict-Transport-Security`

---

## Herramientas utilizadas

- Visual Studio Code
- XAMPP
- Apache
- Navegador web (Chrome/Edge)
- DevTools del navegador
- OWASP ZAP
- GitHub

---


## Desarrollo del taller

### 1. Creación de la página web base

Se creó un archivo `index.html` con una estructura HTML sencilla para servirlo localmente desde Apache.

### 2. Configuración del servidor Apache

Se utilizó **XAMPP** como servidor local, ubicando el proyecto dentro de la carpeta:

```text
C:\xampp\htdocs\encabezados
```

La página se probó desde:

```text
http://localhost/encabezados/
```

Y para HTTPS desde:

```text
https://localhost/encabezados/
```

### 3. Implementación de los encabezados de seguridad

Los encabezados se configuraron en el archivo `.htaccess` ubicado en la raíz del proyecto.

#### Encabezado 1: Content-Security-Policy

```apache
Header always set Content-Security-Policy "default-src 'self'"
```

**Descripción:**  
Restringe la carga de recursos únicamente al mismo origen del sitio (`self`), ayudando a prevenir inyecciones de contenido no autorizado.

#### Encabezado 2: X-Content-Type-Options

```apache
Header always set X-Content-Type-Options "nosniff"
```

**Descripción:**  
Impide que el navegador intente adivinar el tipo de contenido, reduciendo el riesgo de ejecutar archivos con tipos incorrectos.

#### Encabezado 3: X-XSS-Protection

```apache
Header always set X-XSS-Protection "1; mode=block"
```

**Descripción:**  
Activa el filtro de protección contra ataques XSS reflejados en navegadores que aún soportan este encabezado.

#### Encabezado 4: X-Frame-Options

```apache
Header always set X-Frame-Options "deny"
```

**Descripción:**  
Evita que la página sea cargada dentro de un `iframe`, protegiendo contra ataques de tipo clickjacking.

#### Encabezado 5: Strict-Transport-Security

```apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

**Descripción:**  
Indica al navegador que el sitio debe cargarse únicamente mediante HTTPS durante el tiempo definido.

---

## Archivo `.htaccess` final

```apache
<IfModule mod_headers.c>
    Header always set Content-Security-Policy "default-src 'self'"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-XSS-Protection "1; mode=block"
    Header always set X-Frame-Options "deny"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
</IfModule>
```

---

## Verificación de los encabezados

La verificación se realizó de dos formas:

### 1. DevTools del navegador
Se revisó la pestaña **Network > Headers** para comprobar que los encabezados estuvieran presentes en la respuesta del servidor.

### 2. OWASP ZAP
Se utilizó OWASP ZAP para interceptar y analizar la respuesta HTTP/HTTPS del servidor, comprobando que los encabezados fueran enviados correctamente con los valores esperados.

### Valores verificados

- `Content-Security-Policy: default-src 'self'`
- `X-Content-Type-Options: nosniff`
- `X-XSS-Protection: 1; mode=block`
- `X-Frame-Options: deny`
- `Strict-Transport-Security: max-age=31536000; includeSubDomains`

---

## Evidencias sugeridas

Dentro de la carpeta `evidencias/` se encuandra el documento en PDF para visualizar los pasos con capturas de pantalla en el desarrollo de la actividad`

---

## Ejecución del proyecto

1. Iniciar Apache desde XAMPP.
2. Colocar la carpeta del proyecto dentro de `htdocs`.
3. Abrir en el navegador:

```text
http://localhost/encabezados/
```

4. Para la prueba de HSTS:

```text
https://localhost/encabezados/
```

---

## Comentarios en el código

El código fue comentado para ilustrar la ejecución de cada una de las etapas del taller, tal como lo solicita la actividad.

---


