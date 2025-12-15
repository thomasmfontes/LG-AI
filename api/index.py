from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import gradio as gr
import os
from app import demo

# Workaround para erro de Jinja2 no Vercel/Serverless
# Criamos uma nova instância FastAPI e montamos o Gradio nela
app = FastAPI()

# 1. Configurar rotas de arquivos estáticos (PWA)
# Precisamos definir isso AQUI também, pois o 'demo.app' do app.py é ignorado ao usar mount_gradio_app
current_dir = os.path.dirname(os.path.realpath(__file__))
# O arquivo api/index.py está em /api, então subimos um nível para a raiz
root_dir = os.path.dirname(current_dir)
pwa_directory = os.path.join(root_dir, "src", "pwa")
assets_directory = os.path.join(root_dir, "assets")

# Montar pasta assets
# IMPORTANTE: Usamos '/public' e não '/assets' para evitar conflito com 
# os arquivos internos do frontend do Gradio que também usam '/assets'
app.mount("/public", StaticFiles(directory=assets_directory), name="public")

# Rotas do PWA
@app.get("/app-manifest.json")
async def manifest():
    return FileResponse(os.path.join(pwa_directory, "manifest.json"))

@app.get("/sw.js")
async def service_worker():
    return FileResponse(os.path.join(pwa_directory, "sw.js"))

@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join(assets_directory, "fav-lg.ico"))

# 2. Montar Gradio
app = gr.mount_gradio_app(app, demo, path="/")
