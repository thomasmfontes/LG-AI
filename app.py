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
with gr.Blocks(title="IA Clube LG - Assistente Técnico") as demo:
    gr.HTML("""
        <head>
            <link rel="manifest" href="/app-manifest.json">
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
            <script>
                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.register('/sw.js')
                        .then(reg => console.log('Service Worker registered'))
                        .catch(err => console.log('Service Worker registration failed', err));
                }
            </script>
        </head>
        <div class="header-container">
            <img src="file/assets/favicon.ico" class="header-icon">
            <h2>Assistente Técnico - Clube LG</h2>
        </div>
    """, visible=True)
    
    with gr.Accordion("❓ Como funciona", open=False):
        gr.Markdown(
            "🧭 Escolha a rede e o campo de seu arquivo Excel. "
            "A IA informará se o campo é obrigatório, opcional ou deve ser deixado em branco. "
            "Você também pode baixar o modelo oficial da planilha e o manual."
        )
    
    # Estatísticas
    stats = analytics.get_stats()
    with gr.Accordion("📊 Estatísticas de Uso", open=False):
        gr.Markdown(f"""
        - **Total de Redes Disponíveis:** {len(lista_redes)}
        - **Total de Campos:** {len(lista_campos)}
        - **Consultas Realizadas:** {stats['total_queries']}
        """)
    
    # Inputs
    with gr.Row():
        rede_dropdown = gr.Dropdown(
            choices=lista_redes,
            label="🏢 Selecione sua rede",
            filterable=True,
            info="Digite para filtrar as opções"
        )
        campo_dropdown = gr.Dropdown(
            choices=lista_campos,
            label="📝 Selecione o campo que deseja verificar",
            filterable=True,
            info="Digite o nome do campo para buscar"
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

# CSS
gr.HTML("""
<style>
/* Reset & Base */
body, .gradio-container {
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
}

/* Header */
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    background: #f8f9fa;
    border-bottom: 1px solid #e9ecef;
    margin-bottom: 1rem;
}
.header-icon {
    height: 32px;
    margin-right: 12px;
}
h2 {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 600;
}

/* Mobile optimizations */
@media (max-width: 768px) {
    .gradio-container {
        padding: 0px !important;
    }
    .main {
        padding: 10px !important;
    }
    textarea, input, select, .gr-input {
        font-size: 16px !important; /* Prevents iOS zoom */
        padding: 12px !important;
        height: auto !important;
    }
    button {
        padding: 16px !important;
        font-size: 18px !important;
    }
}

/* Results */
.resposta-ia {
  padding: 15px;
  border-radius: 10px;
  font-size: 16px;
  margin-top: 15px;
  border: 1px solid #ccc;
  background-color: #ffffff;
  color: #222;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.resposta-bloco {
  margin-top: 10px;
  padding: 15px;
  border-left: 5px solid #4EA1FF;
  border-radius: 6px;
  background-color: #f8f9fa;
  color: #222;
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
  .resposta-ia {
    background-color: #1e1e1e;
    color: #eee;
    border-color: #444;
  }
  .header-container {
      background: #1e1e1e;
      border-color: #333;
  }
  h2 { color: #eee; }
  .resposta-bloco {
    background-color: #2b2b2b;
    color: #eee;
    border-color: #4EA1FF;
  }
}
</style>
""")

# Mount static files (PWA)
from fastapi import Response
from fastapi.responses import FileResponse
import os

pwa_directory = "src/pwa"

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