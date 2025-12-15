from fastapi import FastAPI
import gradio as gr
from app import demo

# Workaround para erro de Jinja2 no Vercel/Serverless
# Criamos uma nova instância FastAPI e montamos o Gradio nela
app = FastAPI()
app = gr.mount_gradio_app(app, demo, path="/")
