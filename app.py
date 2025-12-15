import gradio as gr
import traceback
from pathlib import Path

from config import Config
from src import DataLoader, Validator, ResponseFormatter, setup_logger
from src.analytics import Analytics
from src.utils import ValidationError

# Setup
logger = setup_logger("lg_ai_app")
analytics = Analytics()

# Carrega dados
logger.info("Iniciando aplicação LG-AI...")
data_loader = DataLoader()
data_loader.load_all()

validator = Validator(data_loader)
formatter = ResponseFormatter()

# Listas para interface
lista_redes = data_loader.get_lista_redes()
lista_campos = data_loader.get_lista_campos()

logger.info(f"Aplicação iniciada: {len(lista_redes)} redes, {len(lista_campos)} campos")


def responder_interface(rede: str, campo: str) -> str:
    """
    Handler principal da interface Gradio.
    
    Args:
        rede: Rede selecionada
        campo: Campo selecionado
    
    Returns:
        HTML formatado com resultado
    """
    try:
        # Validação
        resultado = validator.validar_campo(rede, campo)
        
        # Analytics
        analytics.log_query(rede, campo, resultado['status'])
        
        # Formatação
        return formatter.format_response(resultado)
        
    except ValidationError as e:
        logger.warning(f"Erro de validação: {e}")
        return formatter.format_error(str(e))
    
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        logger.error(traceback.format_exc())
        return formatter.format_error(f"Erro interno: {e}")


# Interface Gradio
from src.theme import LGTheme

with gr.Blocks(title="IA Clube LG", theme=LGTheme()) as demo:
    gr.HTML("""
        <head>
            <link rel="icon" href="/favicon.ico" sizes="any">
            <link rel="apple-touch-icon" href="/public/fav-ai-lg.png">
            <link rel="manifest" href="/app-manifest.json">
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
            <link rel="apple-touch-startup-image" href="/public/fav-ai-lg.png">
            <script>
                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.register('/sw.js')
                        .then(reg => console.log('Service Worker registered'))
                        .catch(err => console.log('Service Worker registration failed', err));
                }
            </script>
        </head>
        <div class="header-container">
            <h2>Assistente Técnico - Clube LG</h2>
        </div>
    """, visible=True)
    
    with gr.Accordion("❓ Como funciona", open=False):
        gr.Markdown(
            "🧭 Escolha a rede e o campo de seu arquivo Excel. "
            "A IA informará se o campo é obrigatório, opcional ou deve ser deixado em branco. "
            "Você também pode baixar o modelo oficial da planilha e o manual."
        )
    
    # Inputs
    with gr.Row():
        rede_dropdown = gr.Dropdown(
            choices=lista_redes,
            label="🏢 Selecione sua rede",
            filterable=False,
            interactive=True
        )
        campo_dropdown = gr.Dropdown(
            choices=lista_campos,
            label="📝 Selecione o campo que deseja verificar",
            filterable=False,
            interactive=True
        )
    
    # Botão e resultado
    submit_btn = gr.Button("🔍 Consultar", variant="primary")
    resultado_output = gr.HTML()
    
    submit_btn.click(
        fn=responder_interface,
        inputs=[rede_dropdown, campo_dropdown],
        outputs=resultado_output
    )
    

    
    # Downloads
    with gr.Row():
        gr.File(
            value=str(Config.MODELO_FILE),
            label="📥 Baixar modelo de planilha (.xlsx)"
        )
        gr.File(
            value=str(Config.MANUAL_FILE),
            label="📘 Baixar manual oficial (.pdf)"
        )
    
    # Version Footer
    gr.Markdown(
        f"<div style='text-align: center; color: #999; margin-top: 20px; font-size: 0.8rem;'>v2.3 Mobile-First - {Config.MANUAL_FILE.name}</div>", 
        elem_classes=["footer-links"]
    )

# CSS Styling - Overrides for Mobile-First Design
gr.HTML("""
<style>
/* Force Font Family */
.gradio-container {
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
}

/* Header Container Styling */
.header-container {
    text-align: center;
    padding: 2rem 1rem;
    margin-bottom: 2rem;
    background: white;
    border-radius: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.header-container h2 {
    color: #A50034 !important; /* LG Red */
    font-size: 1.8rem !important;
    font-weight: 700 !important;
    margin: 0;
}

/* Main Content Area */
.main-content {
    max-width: 600px;
    margin: 0 auto;
}

/* Inputs Styling */
.gr-form {
    background: transparent !important;
    border: none !important;
}

/* Custom Dropdown Styling */
label.svelte-1f354aw-container {
    background: white !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
    padding: 8px !important;
    border: 1px solid #e5e7eb !important;
}

/* Primary Button Styling - PILL SHAPE */
button.primary {
    background-color: #A50034 !important;
    color: white !important;
    border-radius: 9999px !important; /* Pill shape */
    padding: 16px 32px !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    box-shadow: 0 4px 14px rgba(165, 0, 52, 0.4) !important;
    transition: transform 0.2s ease !important;
    border: none !important;
    width: 100%;
}
button.primary:hover {
    transform: scale(1.02);
    background-color: #850029 !important;
}

/* Response Box */
.resposta-ia {
    background: white;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #A50034;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-top: 2rem;
}

/* Footer Section */
.footer-links {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #eee;
}

/* Mobile Specific Adjustments */
@media (max-width: 640px) {
    .gradio-container {
        padding: 16px !important;
    }
    .header-container {
        margin-bottom: 1.5rem;
        padding: 1.5rem 1rem;
    }
    .header-container h2 {
        font-size: 1.4rem !important;
    }
    button.primary {
        padding: 18px !important;
        font-size: 1.15rem !important;
    }
}
</style>
""")

# Mount static files (PWA)
from fastapi import Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

pwa_directory = "src/pwa"

# Mount assets architecture for PWA
demo.app.mount("/public", StaticFiles(directory="assets"), name="public")

@demo.app.get("/app-manifest.json")
async def manifest():
    return FileResponse(os.path.join(pwa_directory, "manifest.json"))

@demo.app.get("/sw.js")
async def service_worker():
    return FileResponse(os.path.join(pwa_directory, "sw.js"))

# Mount other static files if needed, but avoid root mount to prevent conflicts
# demo.app.mount("/", StaticFiles(directory="src/pwa", html=True), name="pwa")

if __name__ == "__main__":
    demo.launch()