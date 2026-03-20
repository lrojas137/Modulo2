<?php
require_once "db.php";

$msg = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $usuario  = $_POST["usuario"] ?? "";
    $nombre   = $_POST["nombre"] ?? "";
    $password = $_POST["password"] ?? "";

    // ✅ Aquí se aplica SHA-256
    $hash = hash("sha256", $password);

    // ✅ Guardar el hash en la BD
    $stmt = $conn->prepare("INSERT INTO usuarios (usuario, password_hash, nombre) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $usuario, $hash, $nombre);

    if ($stmt->execute()) {
        $msg = "✅ Usuario creado y contraseña guardada con SHA-256.";
    } else {
        $msg = "❌ Error: " . $stmt->error;
    }
}
?>
<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><title>Registro</title></head>
<body>
<h2>Registro (SHA-256)</h2>

<form method="post">
  <label>Usuario:</label><br>
  <input name="usuario" required><br><br>

  <label>Nombre:</label><br>
  <input name="nombre" required><br><br>

  <label>Contraseña:</label><br>
  <input name="password" type="password" required><br><br>

  <button type="submit">Crear usuario</button>
</form>

<p><?= htmlspecialchars($msg) ?></p>
</body>
</html>