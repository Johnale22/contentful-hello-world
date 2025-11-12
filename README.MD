# 🚀 Sistema Distribuido: Python + Contentful + Docker

Este proyecto implementa una arquitectura desacoplada donde un microservicio en **Python** gestiona contenido dinámico alojado en **Contentful** (Headless CMS), todo contenerizado mediante **Docker** para garantizar su portabilidad.

## 📋 Descripción Técnica

El sistema consta de dos módulos principales:
1.  **Módulo de Ingesta (`write.py`):** Utiliza la *Content Management API* para inyectar datos automáticamente en la nube.
2.  **Módulo de Consumo (`app.py`):** Utiliza la *Content Delivery API* para recuperar la última versión del contenido en tiempo real.



## 🛠 Tecnologías

* **Lenguaje:** Python 3.9
* **CMS:** Contentful (Headless)
* **Container:** Docker
* **Librerías:** `contentful`, `contentful_management`

## ⚙️ Configuración (Variables de Entorno)

El proyecto requiere un archivo `.env` local o variables de entorno en el contenedor Docker:

```properties
CONTENTFUL_SPACE_ID=tu_space_id
CONTENTFUL_ACCESS_TOKEN=tu_delivery_token  (Para leer)
CONTENTFUL_MANAGEMENT_TOKEN=tu_management_token (Para escribir)