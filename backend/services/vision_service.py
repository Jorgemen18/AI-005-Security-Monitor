from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from backend.config import settings

# 1. Inicializamos el cliente de Azure con tus credenciales
client = ImageAnalysisClient(
    endpoint=settings.VISION_ENDPOINT,
    credential=AzureKeyCredential(settings.VISION_KEY)
)

def detectar_objetos_en_imagen(image_url: str) -> list[str]:
    """
    Envía la URL de la imagen a Azure AI Vision y devuelve una lista 
    de los objetos y etiquetas detectadas con alta confianza.
    """
    try:
        # 2. Le pedimos a Azure que extraiga las "Etiquetas" (Tags) y "Objetos"
        result = client.analyze_from_url(
            image_url=image_url,
            visual_features=[VisualFeatures.TAGS, VisualFeatures.OBJECTS]
        )
        
        elementos_detectados = []
        
        # 3. Guardamos los objetos detectados (ej. "persona", "coche")
        if result.objects is not None:
            for obj in result.objects.list:
                elementos_detectados.append(obj.tags[0].name)
                
        # 4. Guardamos las etiquetas generales que tengan más del 70% de certeza
        if result.tags is not None:
            for tag in result.tags.list:
                if tag.confidence > 0.70:
                    elementos_detectados.append(tag.name)
                    
        # 5. Limpiamos duplicados y devolvemos la lista final
        return list(set(elementos_detectados))
        
    except Exception as e:
        print(f"Error en Vision Service: {e}")
        return ["Error al analizar la imagen"]