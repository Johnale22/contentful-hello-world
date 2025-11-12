import os
import sys
import contentful
from dotenv import load_dotenv

# Cargar variables
load_dotenv()

SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
ACCESS_TOKEN = os.getenv('CONTENTFUL_ACCESS_TOKEN')

if not SPACE_ID or not ACCESS_TOKEN:
    print("Error: Faltan credenciales en .env")
    sys.exit(1)

try:
    client = contentful.Client(SPACE_ID, ACCESS_TOKEN)
    
    # 1. Obtenemos todas las entradas que sean del tipo 'saludo'
    # (Contentful usa IDs para los modelos, usualmente es el nombre en minúscula: 'saludo')
    entries = client.entries({'content_type': 'saludo',
                              'limit': 1,
                              'order': '-sys.createdAt'})  # Limitar a 5 para no saturar la salida

    print("--- CONECTANDO CON CONTENTFUL ---")

    if not entries:
        print("No encontré ninguna entrada. ¿Creaste el modelo 'Saludo' y publicaste una entrada?")
    
    for entry in entries:
        # Aquí ocurre la magia: Extraemos el campo 'mensaje'
        # fields() devuelve un diccionario con tus datos
        mensaje_recibido = entry.fields().get('mensaje1')
        print(f"\n📥 Mensaje recibido desde la nube:\n'{mensaje_recibido}'")

    print("\n---------------------------------")

except Exception as e:
    print(f"Error: {e}")