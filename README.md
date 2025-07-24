
# 💣 Script de Mensajes Bomba para Telegram

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Telethon](https://img.shields.io/badge/Telethon-latest-informational?style=for-the-badge)

Un script de Python diseñado para enviar mensajes repetidamente a un usuario específico de Telegram durante un período de tiempo determinado. Ideal para situaciones en las que se necesita asegurar la atención del destinatario. **Úsalo de manera responsable y ética.**

## ✨ Características

-   **Envío Automatizado**: Envía un mensaje predefinido de forma continua.
-   **Control de Duración**: Establece un límite de tiempo para el envío de mensajes.
-   **Registro Detallado**: Muestra en consola el progreso y los errores.
-   **Fácil de Configurar**: Personaliza rápidamente el mensaje, el destinatario y la duración.

## 📋 Requisitos Previos

Antes de ejecutar este script, asegúrate de tener lo siguiente:

-   **Python 3.x**: Recomendamos usar Python 3.8 o superior.
    -   Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
-   **Cuenta de Telegram**: Necesitarás una cuenta activa de Telegram.
-   **API ID y API Hash de Telegram**: Estos son credenciales esenciales para que el script interactúe con la API de Telegram. Puedes obtenerlos en [my.telegram.org](https://my.telegram.org/).

## 🚀 Instalación

Sigue estos pasos para poner en marcha el script:

1.  **Clona o descarga el repositorio**: Si el script está en un repositorio, clónalo. De lo contrario, descarga el archivo `main.py`.

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio # O la carpeta donde guardaste main.py
    ```

2.  **Crea un entorno virtual (recomendado)**:

    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias**: El script utiliza la biblioteca `telethon`.

    ```bash
    pip install telethon
    ```

## ⚙️ Configuración

Edita el archivo `main.py` y actualiza las siguientes variables con tu información:

-   `API_ID`: Tu API ID de Telegram (número).
-   `API_HASH`: Tu API Hash de Telegram (cadena de texto).
-   `PHONE_NUMBER`: Tu número de teléfono de Telegram, incluyendo el código de país (ej. `+573201234567`).
-   `USERNAME`: El nombre de usuario de Telegram del destinatario (ej. `@LuxuryyEmpiree`).
-   `MESSAGE`: El mensaje que deseas enviar repetidamente.
-   `DURATION`: La duración en segundos durante la cual se enviarán los mensajes (ej. `60` para 1 minuto).

```python
# ... existing code ...
API_ID = 'TU_API_ID' # Reemplaza con tu API ID
API_HASH = 'TU_API_HASH' # Reemplaza con tu API Hash

# ... existing code ...
PHONE_NUMBER = 'TU_NUMERO_DE_TELEFONO' # Reemplaza con tu número

# ... existing code ...
USERNAME = '@NOMBRE_DE_USUARIO_DESTINATARIO' # Reemplaza con el nombre de usuario

# ... existing code ...
MESSAGE = "TU MENSAJE AQUÍ" # Reemplaza con tu mensaje

# ... existing code ...
DURATION = 15 # O la duración que desees en segundos
# ... existing code ...
```

## ▶️ Uso

Una vez configurado, ejecuta el script desde tu terminal:

```bash
python main.py
```

La primera vez que ejecutes el script, Telethon te pedirá que introduzcas un código de verificación que recibirás en tu aplicación de Telegram. Una vez autenticado, el script comenzará a enviar los mensajes al usuario especificado durante la duración establecida.

## ⚠️ Advertencias y Consideraciones

-   **Uso Ético**: Este script debe usarse de manera responsable. El envío masivo e indeseado de mensajes puede considerarse spam y violar los términos de servicio de Telegram, lo que podría resultar en la suspensión de tu cuenta.
-   **Frecuencia de Envío**: El script envía mensajes cada 1 segundo. Si bien es efectivo para llamar la atención, ten en cuenta el impacto en el destinatario.
-   **Manejo de Errores**: El script incluye un manejo básico de excepciones para errores de envío, pero no cubre todos los posibles escenarios de la API de Telegram.
-   **Sesión**: La sesión de Telegram se guarda en un archivo llamado `session_name.session` en la misma carpeta que el script. No lo elimines a menos que quieras volver a iniciar sesión.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` (si existe) para más detalles.
