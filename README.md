# medcare

# Instalando dependências do backend

Para instalar todas as dependências de um projeto Flask (ou qualquer outro projeto Python) em outra máquina, a pessoa precisará seguir dois passos:

# Passo 1: Ativar o ambiente virtual (opcional)
    Primeiro, crie e ative um ambiente virtual para isolar as dependências do projeto. Isso é opcional, mas recomendado para evitar conflitos de pacotes com outras aplicações Python.

**Criar o ambiente virtual:**
    python -m venv venv
    Ativar o ambiente virtual:
        No Windows:
            venv\Scripts\activate
        No macOS/Linux:
            source venv/bin/activate

# Passo 2: Instalar as dependências

Uma vez no ambiente virtual (ou mesmo fora dele), o comando para instalar todas as dependências listadas no arquivo requirements.txt é:

    pip install -r requirements.txt

Esse comando vai instalar todas as dependências necessárias para rodar o projeto de acordo com o arquivo requirements.txt que você já deve ter gerado com:
    
    pip freeze > requirements.txt