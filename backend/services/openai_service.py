from openai import AzureOpenAI
import json
from backend.config import settings
from backend.prompts.risk_prompt import SYSTEM_PROMPT

# 1. Inicializamos el cliente de Azure OpenAI
client = AzureOpenAI(
    api_key=settings.OPENAI_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=settings.OPENAI_ENDPOINT
)

def analizar_riesgo(objetos: list[str]) -> dict:
    """
    Toma los objetos detectados, los envía a GPT y devuelve el análisis en JSON.
    """
    # Si no hay objetos, no gastamos tokens de IA
    if not objetos:
        return {
            "objetos_detectados": [],
            "nivel_riesgo": "Bajo",
            "descripcion_escena": "No se detectaron objetos analizables.",
            "recomendacion_seguridad": "Ninguna acción requerida."
        }
        
    lista_texto = ", ".join(objetos)
    mensaje_usuario = f"Objetos detectados en la cámara: {lista_texto}"
    
    try:
        # 2. Llamada al modelo (¡Forzando JSON Object!)
        response = client.chat.completions.create(
            model=settings.OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": mensaje_usuario}
            ],
            response_format={ "type": "json_object" },
            temperature=0.2 # Temperatura baja para que sea estricto
        )
        
        # 3. Convertimos el string de la respuesta a un diccionario de Python
        return json.loads(response.choices[0].message.content)
        
    except Exception as e:
        print(f"Error en OpenAI Service: {e}")
        return {"error": "No se pudo completar el análisis de riesgo."}