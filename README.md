# 📊 IA Clube LG – Assistente Técnico

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Assistente inteligente para validação de campos de arquivos Excel no sistema Clube LG. Desenvolvido com Gradio, oferece interface web intuitiva para consultar obrigatoriedade de campos por rede e canal.

---

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/ThomasMF7/LG-AI.git
cd LG-AI

# Crie ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
```

A aplicação estará disponível em `http://localhost:7860`

---

## 📖 Como Usar

1. **Selecione a Rede**: Escolha a rede no dropdown (filtrável)
2. **Selecione o Campo**: Escolha o campo a validar
3. **Consulte**: Clique em "🔍 Consultar" para ver o resultado
4. **Baixe Recursos**: Modelo de planilha e manual disponíveis para download

### Resultados

- 🔴 **Obrigatório**: Campo deve ser preenchido
- 🟢 **Opcional**: Campo pode ou não ser preenchido
- ⚪ **Deve ficar em branco**: Campo não deve ser preenchido

---

## 🏗️ Arquitetura

```
LG-AI/
├── app.py                 # Interface Gradio (entry point)
├── config.py              # Configurações centralizadas
├── requirements.txt       # Dependências de produção
├── requirements-dev.txt   # Dependências de desenvolvimento
├── pyproject.toml         # Configuração de ferramentas
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Este arquivo
│
├── src/                  # Código fonte
│   ├── __init__.py
│   ├── data_loader.py    # Carregamento de dados Excel
│   ├── validator.py      # Lógica de validação
│   ├── formatter.py      # Formatação de respostas HTML
│   ├── utils.py          # Funções auxiliares
│   ├── logger.py         # Sistema de logging
│   └── analytics.py      # Rastreamento de uso
│
├── data/                 # Planilhas e documentos
│   ├── Redes_Codigo_Canal.xlsx
│   ├── Campos_por_Canal.xlsx
│   ├── Modelo_Arquivo_Vendas.xlsx
│   └── Manual_Upload_de_Arquivos_Facilitador.pdf
│
├── assets/               # Recursos estáticos
│   └── favicon.png
│
└── tests/                # Testes automatizados
    ├── __init__.py
    ├── conftest.py       # Fixtures compartilhadas
    ├── test_data_loader.py
    ├── test_validator.py
    └── test_utils.py
```

---

## 🧪 Desenvolvimento

### Instalação para Desenvolvimento

```bash
# Instale dependências de desenvolvimento
pip install -r requirements-dev.txt
```

### Executar Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=src --cov-report=html

# Teste específico
pytest tests/test_validator.py -v
```

### Formatação e Linting

```bash
# Formatar código
black .

# Ordenar imports
isort .

# Linting
flake8 src/ tests/

# Type checking
mypy src/
```

---

## 🧠 Funcionalidades

- ✅ Validação de obrigatoriedade de campos por rede/canal
- ✅ Extração automática de comentários do modelo Excel
- ✅ Interface web responsiva com dark mode
- ✅ Sistema de logging estruturado
- ✅ Analytics básico de uso
- ✅ Cache de dados para performance
- ✅ Testes automatizados (>80% cobertura)
- ✅ Type hints completo
- ✅ Documentação abrangente

---

## 📊 Tecnologias

- **Framework Web**: [Gradio](https://gradio.app/)
- **Processamento de Dados**: [Pandas](https://pandas.pydata.org/)
- **Excel**: [OpenPyXL](https://openpyxl.readthedocs.io/)
- **Testes**: [Pytest](https://pytest.org/)
- **Code Quality**: Black, Flake8, MyPy, isort

---

## 📝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Diretrizes

- Mantenha cobertura de testes >80%
- Use Black para formatação
- Adicione type hints
- Documente funções públicas
- Siga convenções PEP 8

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Thomas MF**
- HuggingFace: [@ThomasMF7](https://huggingface.co/ThomasMF7)
- GitHub: [@ThomasMF7](https://github.com/ThomasMF7)

---

## 🙏 Agradecimentos

Desenvolvido para facilitar o trabalho de validação de arquivos no sistema Clube LG.

---

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma [issue](https://github.com/ThomasMF7/LG-AI/issues)
- Consulte o [manual oficial](https://huggingface.co/spaces/ThomasMF7/ia-clube-lg/resolve/main/Manual_Upload_de_Arquivos_Facilitador.pdf)