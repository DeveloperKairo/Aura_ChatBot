<div align="center">

# ✨ AURA - Seu Amigo Virtual para Apoio Emocional ✨

**Um projeto desenvolvido com carinho para a Imersão IA da Alura em parceria com o Google Gemini!**

[![Evento](https://img.shields.io/badge/Imersão%20IA-Alura%20%26%20Google-%230073E6?style=for-the-badge&logo=google&logoColor=white&labelColor=0B579B)](https://www.alura.com.br/imersao-ia)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini API](https://img.shields.io/badge/Gemini%20API-4A89F3?style=for-the-badge&logo=google-gemini&logoColor=white)](https://ai.google.dev/docs/gemini_api_overview)

</div>

Bem-vindo(a) ao universo de AURA (Amigo Virtual para Resiliência e Autoconhecimento)! 🌟

AURA é mais que um chatbot; é um companheiro virtual projetado para oferecer um espaço seguro, acolhedor e confidencial. Aqui, você pode expressar seus sentimentos, encontrar um ombro amigo digital, receber apoio empático e acessar recursos práticos para promover seu bem-estar emocional.

---

## 💖 Conheça AURA

Em um mundo cada vez mais conectado, mas muitas vezes solitário, AURA surge como uma luz guia. Seu propósito é:

* **Ouvir sem julgamentos:** Sinta-se à vontade para compartilhar o que está em seu coração.
* **Oferecer conforto e empatia:** Respostas pensadas para te acolher e te fazer sentir compreendido(a).
* **Sugerir caminhos para o bem-estar:** Acesso a dicas e recursos simples, como exercícios de respiração e meditação.
* **Lembrar da importância do autocuidado:** Pequenos lembretes para que você priorize sua saúde mental.
* **Incentivar a busca por ajuda profissional:** Quando necessário, AURA gentilmente sugere a procura por especialistas.

AURA utiliza o poder da Inteligência Artificial do Google Gemini para criar interações que buscam ser o mais humanas e compreensivas possível, sempre com foco no seu bem-estar.

---

## 🚀 Funcionalidades Principais

* 🗣️ **Conversas Empáticas:** Diálogos que se adaptam para oferecer suporte emocional.
* 🧘 **Recursos de Bem-Estar:** Sugestões de exercícios de respiração, meditação e técnicas de grounding.
* 🧠 **Memória Afetiva:** Histórico de conversas (salvo localmente e com aviso de privacidade) para personalizar interações futuras e "lembrar" de você.
* ⚠️ **Alerta de Crise:** Identificação de palavras-chave que indicam sofrimento intenso, com sugestão imediata para procurar ajuda profissional (CVV 188).
* 💻 **Interface Simples:** Interação via linha de comando (CLI), focada na conversa.
* 🛡️ **Privacidade em Primeiro Lugar:** Suas conversas são suas. O histórico é salvo localmente no seu computador.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

* **Python:** Linguagem principal do projeto.
* **Google Gemini API:** O cérebro por trás da inteligência e capacidade de conversação empática do AURA.
* **python-dotenv:** Para gerenciar de forma segura as chaves de API.

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini API](https://img.shields.io/badge/Gemini%20API-4A89F3?style=for-the-badge&logo=google-gemini&logoColor=white)](https://ai.google.dev/docs/gemini_api_overview)

</div>

---

## 🎬 AURA em Ação!

![Demonstração do AURA em ação](https://i.imgur.com/KAdy7nj.gif)

---

## ⚙️ Guia de Execução e Instalação

Pronto para conversar com AURA? Siga os passos abaixo:

### 1. Pré-requisitos

* **Python 3.7+** instalado.
* **Git** instalado.

### 2. Configuração do Ambiente

1.  **Clone o repositório:**
    Abra seu terminal e execute o comando:
    ```bash
    git clone [https://www.google.com/search?q=https://github.com/DeveloperKairo/Aura_ChatBot.git](https://www.google.com/search?q=https://github.com/DeveloperKairo/Aura_ChatBot.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd Aura_ChatBot
    ```

3.  **Crie o arquivo de ambiente `.env`:**
    Na raiz do projeto (`Aura_ChatBot/`), crie um arquivo chamado `.env`. Dentro dele, adicione sua chave da API do Google Gemini:
    ```env
    GOOGLE_API_KEY="SUA_CHAVE_API_DO_GEMINI_AQUI"
    ```
    *Substitua `SUA_CHAVE_API_DO_GEMINI_AQUI` pela sua chave real.*

4.  **(Recomendado) Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    ```
    * No Windows:
        ```bash
        venv\Scripts\activate
        ```
    * No Linux/macOS:
        ```bash
        source venv/bin/activate
        ```

5.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Executando o AURA 🚀

Após a configuração, execute o comando:
```bash
python main.py
AURA irá te cumprimentar e pedir um nome ou apelido para personalizar a conversa e salvar o histórico.

### 4. Como Interagir 💬
   
Simplesmente digite suas mensagens e pressione Enter.
Para encerrar a conversa, digite sair, exit ou tchau.
AURA tentará entender suas emoções e oferecer o melhor suporte possível!
🔒 Aviso de Privacidade
Levamos sua privacidade a sério.

Suas conversas com AURA podem ser salvas localmente no seu computador, na pasta data/user_histories/, para ajudar a personalizar futuras interações e permitir que AURA "se lembre" de você.
Estes dados não são compartilhados com terceiros.
Você tem controle sobre esses arquivos e pode excluí-los se desejar (funcionalidade de exclusão via app pode ser implementada no futuro).

👨‍💻 Desenvolvido Por
Este projeto foi idealizado e desenvolvido por:

Kairo Kaléo

🙏 Agradecimentos Especiais
À Alura e ao Google pela incrível iniciativa da Imersão IA, que proporcionou o conhecimento e a inspiração para este projeto.
Se tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma Issue no repositório! Cuide-se! ❤️