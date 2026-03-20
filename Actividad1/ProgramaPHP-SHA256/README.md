## Práctica: Almacenamiento de contraseñas con SHA-256 (PHP + MySQL)

### Propósito
Evitar el almacenamiento de contraseñas en texto plano implementando el guardado de contraseñas mediante **hash SHA-256**, cumpliendo el requerimiento de la actividad.

## Materiales / Requisitos
- XAMPP (Apache + MySQL + PHP)
- phpMyAdmin
- Proyecto PHP en `C:\xampp\htdocs\sqli_demo`
- Editor (Visual Studio Code recomendado)

---

### 1) Cambio en la base de datos
Se modificó la columna de contraseñas para guardar el hash:

```sql
ALTER TABLE usuarios
  CHANGE password password_hash CHAR(64) NOT NULL;
```

<img width="929" height="274" alt="image" src="https://github.com/user-attachments/assets/55bce054-1ccf-4a28-b710-8cd2096ab340" />

---

### 2) Implementación del registro con SHA-256 (PHP)
Se creó el archivo registro.php para insertar usuarios guardando el hash SHA-256 en la base de datos.

1. En la carpeta del proyecto crear el archivo:
   - `C:\xampp\htdocs\sqli_demo\registro.php`

2. En el código, antes de guardar, aplicar SHA-256:

```php
$hash = hash("sha256", $password);
```

Idea principal:

- Recibir la contraseña del formulario
- Calcular el hash con SHA-256
- Guardar el hash en password_hash (no la contraseña original)

```php
registro.php
$hash = hash("sha256", $password);

$stmt = $conn->prepare("INSERT INTO usuarios (usuario, password_hash, nombre) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $usuario, $hash, $nombre);
$stmt->execute();
```
Al usar el formulario se crea la contraseña con SHA-256.

<img width="866" height="489" alt="image" src="https://github.com/user-attachments/assets/11b9b938-0cd6-4b25-a163-a0399c1c2453" />

<img width="929" height="161" alt="image" src="https://github.com/user-attachments/assets/f8108163-bcce-4b1a-93f6-0139c5998b9c" />



---

### 3) Actualización de usuarios ya existentes 

Se convierten las contraseñas antiguas (texto plano) a SHA-256.

1. En phpMyAdmin → lab_sqli → pestaña SQL

2. Ejecutar las actualizaciones (según contraseñas conocidas en el laboratorio):

```sql
UPDATE usuarios SET password_hash = SHA2('1234', 256) WHERE usuario='lcrojas';
UPDATE usuarios SET password_hash = SHA2('abcd', 256) WHERE usuario='ana';
UPDATE usuarios SET password_hash = SHA2('admin', 256) WHERE usuario='admin';
```
El resultado queda con las demas contraseñas con SHA-256.

<img width="929" height="161" alt="image" src="https://github.com/user-attachments/assets/e4c9bcbc-9f6a-4f3b-81aa-8b45ce5ae921" />

---

### 4) Criterio de verificación

- password_hash debe tener 64 caracteres y ser hexadecimal (0-9, a-f).

- No debe verse la contraseña original (por ejemplo 1234, abcd, etc.).

