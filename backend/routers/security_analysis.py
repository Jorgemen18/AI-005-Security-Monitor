from fastapi import APIRouter, HTTPException
from backend.models.analysis_model import ImageRequest, SecurityAnalysisResult
from backend.services.vision_service import detectar_objetos_en_imagen
from backend.services.openai_service import analizar_riesgo

# Creamos el router para nuestros endpoints
router = APIRouter(prefix="/api/v1/security", tags=["Análisis de Seguridad"])

@router.post("/analyze", response_model=SecurityAnalysisResult)
async def analyze_security_camera_image(request: ImageRequest):
    # 1. Los "Ojos": Enviamos la URL a Azure Vision
    objetos = detectar_objetos_en_imagen(request.image_url)
    
    if "Error al analizar la imagen" in objetos:
        raise HTTPException(status_code=400, detail="No se pudo procesar la imagen. Verifica que la URL sea pública y válida.")
        
    # 2. El "Cerebro": Pasamos los objetos a Azure OpenAI para el análisis de riesgo
    analisis = analizar_riesgo(objetos)
    
    if "error" in analisis:
        raise HTTPException(status_code=500, detail="Error en el motor de razonamiento lógico.")
        
    # 3. Retornamos la respuesta ya formateada según el modelo de Pydantic
    return analisis