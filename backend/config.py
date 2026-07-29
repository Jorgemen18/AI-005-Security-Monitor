import os
from dotenv import load_dotenv

# Carga las variables del archivo .env al entorno de Python
load_dotenv()

class Settings:
    # Credenciales de Azure OpenAI
    OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    
    # Credenciales de Azure AI Vision
    VISION_ENDPOINT = os.getenv("AZURE_VISION_ENDPOINT")
    VISION_KEY = os.getenv("AZURE_VISION_KEY")

# Instanciamos la configuración para importarla fácilmente en otros archivos
settings = Settings()