# AURA - Seu Amigo Virtual para Apoio Emocional

AURA (Amigo Virtual para Resiliência e Autoconhecimento) é um chatbot de apoio emocional personalizado, desenvolvido com Python e a API Google Gemini. Este projeto foi criado como parte de um hackathon, com foco em utilidade, criatividade, eficiência e apresentação.

## Visão Geral

AURA visa oferecer um primeiro ponto de contato para pessoas que precisam de apoio emocional. Utilizando o poder da IA Generativa do Google, AURA busca:

* **Utilidade:** Oferecer respostas empáticas, utilizando o `system_instruction` do Gemini para guiar a IA a entender nuances de sentimento e oferecer recursos relevantes.
* **Criatividade:** Personalizar a conversa com base no histórico do usuário (salvo localmente) e sugerir recursos como exercícios de respiração ou links para meditação.
* **Eficácia:** Ajudar o usuário a se sentir ouvido e oferecer estratégias de enfrentamento simples e eficazes, sempre com o lembrete de procurar ajuda profissional quando necessário.
* **Apresentação:** Interface de linha de comando (CLI) limpa, acolhedora, com avisos claros de privacidade e segurança de dados (foco na transparência).

**Importante:** AURA não substitui aconselhamento médico ou terapêutico profissional. Em caso de crise ou sofrimento intenso, procure ajuda especializada.

## Estrutura do Projeto
/aura_chatbot
    |-- /app                  # Contém a lógica principal da aplicação
    |-- /config               # Arquivos de configuração (ex: API Key)
    |-- /data                 # Dados utilizados/gerados (históricos, recursos)
    |-- main.py               # Ponto de entrada da CLI
    |-- requirements.txt      # Dependências
    |-- README.md             # Este arquivo
    |-- .env.example          # Exemplo para o arquivo .env
    |-- .gitignore            # Arquivos a serem ignorados pelo Git

## Como Rodar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd aura_chatbot
    ```

2.  **Crie um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a API Key do Google Gemini:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua chave da API do Google Gemini ao arquivo `.env`:
        ```
        GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
        ```
    * Você pode obter uma chave de API no [Google AI Studio](https://aistudio.google.com/).

5.  **Execute a Aplicação:**
    ```bash
    python main.py
    ```

6.  Siga as instruções no terminal para interagir com AURA. Digite "sair" para encerrar.

## Funcionalidades Futuras (Ideias para Evolução)

* Integração com APIs de meditação guiada ou sons relaxantes.
* Interface gráfica mais amigável (Web com Flask/Streamlit ou aplicativo Desktop).
* Sistema de feedback do usuário para melhorar as respostas.
* Opção para o usuário solicitar a exclusão do seu histórico.
* Mecanismos mais avançados para detecção de crises e encaminhamento (com consentimento).
