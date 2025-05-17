import streamlit as st
from app.chatbot_core import AuraChatbot
import uuid 
import time 


st.set_page_config(page_title="AURA - Apoio Emocional", page_icon="✨", layout="centered")

st.markdown("""
<style>
    .stChatMessage {
        border-radius: 10px;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .stChatMessage[data-testid="chatAvatarIcon-user"] {
        background-color: #e0f7fa; /* Azul claro para usuário */
    }
    .stChatMessage[data-testid="chatAvatarIcon-assistant"] {
        background-color: #fff9c4; /* Amarelo claro para AURA */
    }
    /* Adicionar um pouco de espaço abaixo do título */
    .stApp > header {
        margin-bottom: 20px;
    }
    h1 {
        margin-bottom: 0.5em; /* Adiciona espaço abaixo do H1 */
    }
</style>
""", unsafe_allow_html=True)

def initialize_bot(user_id):
    if "aura_bot" not in st.session_state or st.session_state.user_id != user_id:
        st.session_state.user_id = user_id
        st.session_state.aura_bot = AuraChatbot(user_id=user_id)
        st.session_state.messages = [] 
        loaded_history = st.session_state.aura_bot.chat_session.history
        for turn in loaded_history:
            display_role = "user" if turn.role == "user" else "assistant"
            text_content = "".join(part.text for part in turn.parts if hasattr(part, 'text'))
            if text_content: 
                st.session_state.messages.append({"role": display_role, "content": text_content})
    return st.session_state.aura_bot

# --- Interface Principal ---
st.title("✨ AURA - Seu Amigo Virtual")
st.caption("Um espaço seguro para expressar seus sentimentos e encontrar apoio.")

# 1. Gerenciamento do ID do Usuário e Inicialização do Chat
if "user_id_confirmed" not in st.session_state:
    st.session_state.user_id_confirmed = False

if not st.session_state.user_id_confirmed:
    st.markdown("---")
    st.subheader("Para começar, como AURA pode te chamar?")
    placeholder_name = f"Usuário_{str(uuid.uuid4())[:6]}"
    user_id_input = st.text_input(
        "Digite seu nome ou um apelido:",
        key="user_id_input_field",
        placeholder=f"Ex: {placeholder_name}",
        label_visibility="collapsed" 
    )

    if st.button("Iniciar Conversa com AURA", key="start_chat_button", type="primary"):
        if user_id_input.strip():
            st.session_state.current_user_id = user_id_input.strip()
        else:
            st.session_state.current_user_id = placeholder_name
        
        initialize_bot(st.session_state.current_user_id)
        st.session_state.user_id_confirmed = True
        st.session_state.welcome_message_shown = False 
        st.rerun() 
else:
    aura_bot = initialize_bot(st.session_state.current_user_id) 

    if not st.session_state.get("welcome_message_shown", False):
        st.info(
            f"Olá, **{st.session_state.current_user_id}**! Sou AURA. Estou aqui para te ouvir. 😊\n\n"
            "Lembre-se: não sou um profissional de saúde mental. Se precisar de ajuda urgente ou estiver em crise, "
            "procure um profissional ou ligue para o CVV (188)."
        )
        with st.expander("⚠️ Leia sobre sua Privacidade e como usar o AURA"):
            st.caption(
                "**Privacidade:** Suas conversas são salvas localmente no seu computador para que AURA possa "
                "lembrar de interações passadas e personalizar o diálogo. Não compartilhamos seus dados.\n\n"
                "**Como usar:** Digite sua mensagem na caixa abaixo. Para encerrar e salvar sua conversa, "
                "digite 'sair', 'tchau' ou 'exit'."
            )
        st.session_state.welcome_message_shown = True
        st.markdown("---")


    if "messages" in st.session_state:
        for message in st.session_state.messages:
            avatar_icon = "👤" if message["role"] == "user" else "✨"
            with st.chat_message(message["role"], avatar=avatar_icon):
                st.markdown(message["content"])

    # Input do usuário
    if prompt := st.chat_input("Como você está se sentindo hoje?"):
        # Adiciona mensagem do usuário ao histórico e exibe
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Obtém resposta do AURA
        with st.chat_message("assistant", avatar="✨"):
            with st.spinner("AURA está digitando..."): 
                aura_response_text = aura_bot.interact(prompt)
            
            message_placeholder = st.empty()
            full_response = ""
            for chunk in aura_response_text.split(): 
                full_response += chunk + " "
                time.sleep(0.05) # Pequeno atraso
                message_placeholder.markdown(full_response + "▌") 
            message_placeholder.markdown(full_response.strip()) 

        st.session_state.messages.append({"role": "assistant", "content": aura_response_text})

        if prompt.strip().lower() in ["sair", "exit", "tchau"]:
            st.success("Conversa encerrada e histórico salvo! Para iniciar uma nova conversa, atualize a página ou digite um novo nome se a opção aparecer.")

    # Botão para iniciar nova conversa (opcional)
    st.markdown("---")
    if st.button("Iniciar Nova Conversa / Trocar Usuário"):

        keys_to_reset = ["user_id_confirmed", "current_user_id", "aura_bot", "messages", "welcome_message_shown"]
        for key in keys_to_reset:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()