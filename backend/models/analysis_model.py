from pydantic import BaseModel, Field

# Lo que el usuario nos enviará (Input)
class ImageRequest(BaseModel):
    image_url: str = Field(..., description="La URL pública de la imagen de la cámara de seguridad")

# Lo que la IA nos debe responder (Output)
class SecurityAnalysisResult(BaseModel):
    objetos_detectados: list[str] = Field(description="Lista de objetos clave encontrados en la imagen (ej. 'casco', 'montacargas', 'persona')")
    nivel_riesgo: str = Field(description="Clasificar como 'Bajo', 'Medio' o 'Alto'")
    descripcion_escena: str = Field(description="Breve descripción de lo que está ocurriendo")
    recomendacion_seguridad: str = Field(description="Acción sugerida para mitigar el riesgo")