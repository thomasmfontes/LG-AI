from app import demo

# Vercel requer que a variável se chame 'app'
# O Gradio (demo) expõe o app FastAPI em demo.app
app = demo.app
