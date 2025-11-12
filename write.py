import os
import sys
from contentful_management import Client
from dotenv import load_dotenv
import uuid

load_dotenv()

MANAGEMENT_TOKEN = os.getenv('CONTENTFUL_MANAGEMENT_TOKEN')
SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')

if not MANAGEMENT_TOKEN:
    print("❌ Error: No encontré el CONTENTFUL_MANAGEMENT_TOKEN en el archivo .env")
    sys.exit(1)

try:
    print("--- 🚀 INICIANDO PROCESO DE ESCRITURA ---")
    
    client = Client(MANAGEMENT_TOKEN)
    space = client.spaces().find(SPACE_ID)
    environment = space.environments().find('master')

    mensaje_nuevo = f"Hola desde Python xd! ID único: {uuid.uuid4().hex[:8]}"
    print(f"📝 Preparando mensaje: '{mensaje_nuevo}'")

    # --- CORRECCIÓN AQUÍ ---
    # 1. Primero obtenemos el objeto "Content Type" (el molde)
    content_type = environment.content_types().find('saludo')

    # 2. Creamos la entrada USANDO ese molde específico
    # Nota: 'fields' es necesario dentro de attributes
    nueva_entrada = content_type.entries().create(
        attributes={
            'fields': {
                'mensaje1': {
                    'en-US': mensaje_nuevo
                }
            }
        }
    )
    # -----------------------

    print("✅ Entrada creada (Borrador)...")

    nueva_entrada.publish()
    
    print(f"🎉 ¡PUBLICADO EXITOSAMENTE! ID: {nueva_entrada.id}")
    print("--- Ve a Contentful o corre app.py para verlo ---")

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")