# AI-005-Security-Monitor 👁️🧠

API REST Multimodal construida con FastAPI que utiliza Inteligencia Artificial para analizar imágenes de cámaras de seguridad y detectar riesgos industriales o de seguridad física.

## 📸 Demostración del Análisis

*A continuación se muestra un ejemplo de la API evaluando una imagen y devolviendo el análisis de riesgo estructurado en formato JSON:*

![Demostración del resultado final](demo.png)

*(Nota: Asegúrate de guardar tu captura de pantalla con el nombre `demo.png` en la misma carpeta que este archivo README, o actualiza la ruta de arriba si usas otro nombre).*

## 🚀 Arquitectura
Este proyecto implementa dos servicios cognitivos en cadena:
1. **Azure AI Vision (Ojos):** Extrae características visuales, etiquetas y objetos de una imagen a partir de su URL pública.
2. **Azure OpenAI (Cerebro):** Evalúa los objetos detectados aplicando reglas de negocio estrictas para determinar el nivel de riesgo de la escena y emitir recomendaciones de seguridad.

## 🛠️ Tecnologías Utilizadas
* Python 3.10+
* FastAPI & Uvicorn (Framework API y Servidor web)
* Pydantic (Validación estricta de modelos de datos JSON)
* Azure AI Vision SDK
* Azure OpenAI SDK

## ⚙️ Configuración y Despliegue Local

### 1. Preparar el entorno virtual
Es recomendable usar un entorno virtual para aislar las dependencias:
```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
Crea un archivo llamado `.env` en la raíz del proyecto (nunca lo subas al repositorio) y agrega tus credenciales de Azure:
```env
AZURE_OPENAI_ENDPOINT="tu_endpoint_aqui"
AZURE_OPENAI_API_KEY="tu_llave_aqui"
AZURE_OPENAI_DEPLOYMENT_NAME="tu_modelo_gpt"
AZURE_VISION_ENDPOINT="tu_endpoint_vision"
AZURE_VISION_KEY="tu_llave_vision"
```

### 4. Ejecutar el servidor
Levanta la API en tu máquina local usando Uvicorn:
```bash
uvicorn backend.main:app --reload
```

### 5. Uso de la API
Una vez encendido el servidor, abre tu navegador y entra a la interfaz interactiva de Swagger:
**`http://127.0.0.1:8000/docs`**

Desde ahí, expande el endpoint `POST /api/v1/security/analyze`, haz clic en "Try it out" y envía un cuerpo JSON válido como este:

```json
{
  "image_url": "[https://revistaelobservador.com/images/stories/Galerias/obra_bulto_sando/sando_bulto.jpg](https://revistaelobservador.com/images/stories/Galerias/obra_bulto_sando/sando_bulto.jpg)"
}
```
La API te devolverá la clasificación del riesgo, la descripción de la escena y las acciones sugeridas.