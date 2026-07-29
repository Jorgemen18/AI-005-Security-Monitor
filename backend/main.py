from fastapi import FastAPI
from backend.routers import security_analysis

# Inicializamos la aplicación
app = FastAPI(
    title="AI-005 Security Monitor API",
    description="API Multimodal que analiza imágenes de seguridad y detecta riesgos usando Azure Vision y Azure OpenAI.",
    version="1.0.0"
)

# Conectamos el router que acabamos de crear
app.include_router(security_analysis.router)

@app.get("/")
def read_root():
    return {"status": "Monitor de Seguridad Inteligente Activo 🟢"}