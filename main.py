import logging
import time
import asyncio
from telethon import TelegramClient, functions, types

# Configura el logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Reemplaza 'YOUR_API_ID' y 'YOUR_API_HASH' con tu API ID y API Hash de Telegram
API_ID = '27864183'
API_HASH = 'e947ab7db504dc81b1835b1e3c40b30e'

# Reemplaza 'YOUR_PHONE_NUMBER' con tu número de teléfono registrado en Telegram
PHONE_NUMBER = '+573208930349'

# Nombre de usuario de Telegram del usuario (con @)
USERNAME = '@LuxuryyEmpiree'

# Mensaje a enviar
MESSAGE = "HERE YOU TYPE YOUR MESSAGE"

# Tiempo en segundos durante el cual se enviarán los mensajes
DURATION = 60  # 1 minuto

async def main():
    client = TelegramClient('session_name', API_ID, API_HASH)

    async def send_messages():
        await client.start(PHONE_NUMBER)
        logging.info("Sesión iniciada correctamente.")

        # Obtener la entidad del usuario
        user = await client.get_entity(USERNAME)
        logging.info(f"Entidad del usuario resuelta: {user.id} - {user.username}")

        end_time = time.time() + DURATION

        while time.time() < end_time:
            try:
                message = await client.send_message(user, MESSAGE)
                logging.info(f"Mensaje enviado a {USERNAME}. ID del mensaje: {message.id}")
            except Exception as e:
                logging.error(f"Error al enviar mensaje: {e}")

            # Espera 1 segundo antes de enviar el siguiente mensaje
            await asyncio.sleep(1)

    async with client:
        await send_messages()

if __name__ == '__main__':
    asyncio.run(main())
