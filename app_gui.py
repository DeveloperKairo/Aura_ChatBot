import streamlit as st
from app.chatbot_core import AuraChatbot  # Ajuste conforme sua estrutura de pastas
import uuid

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
    .stApp > header {
        margin-bottom: 20px;
    }
    h1 {
        margin-bottom: 0.5em;
    }
</style>
""", unsafe_allow_html=True)

def initialize_bot(user_id):
    try:
        if "aura_bot" not in st.session_state or st.session_state.user_id != user_id:
            st.session_state.user_id = user_id
            st.session_state.aura_bot = AuraChatbot(user_id=user_id)
            st.session_state.messages = []

            try:
                loaded_history = st.session_state.aura_bot.chat_session.history
                for turn in loaded_history:
                    display_role = "user" if turn.role == "user" else "assistant"
                    text_content = "".join(part.text for part in turn.parts if hasattr(part, 'text'))
                    if text_content:
                        st.session_state.messages.append({
                            "role": display_role,
                            "content": text_content
                        })
            except Exception as e:
                st.error(f"Erro ao carregar histórico: {str(e)}")
    except Exception as e:
        st.error(f"Falha na inicialização do bot: {str(e)}")
    return st.session_state.get("aura_bot")

def save_current_conversation():
    aura_bot = st.session_state.get("aura_bot")
    if aura_bot:
        try:
            aura_bot.end_session()  # Método que salva o histórico da conversa
            st.success("Conversa anterior salva com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar a conversa: {e}")
    else:
        st.warning("Nenhuma conversa ativa para salvar.")

# Inicializa nome aleatório uma única vez
if "current_user_id" not in st.session_state:
    st.session_state.current_user_id = f"Usuário_{str(uuid.uuid4())[:6]}"

if "user_id_confirmed" not in st.session_state:
    st.session_state.user_id_confirmed = False

# --- Interface Principal ---
st.title("✨ AURA - Seu Amigo Virtual")
st.caption("Um espaço seguro para expressar seus sentimentos e encontrar apoio.")

if not st.session_state.user_id_confirmed:
    st.markdown("---")
    st.subheader("Para começar, como AURA pode te chamar?")

    with st.form("user_name_form", clear_on_submit=False):
        user_name = st.text_input(
            "Digite seu nome ou um apelido:",
            placeholder=st.session_state.current_user_id,
            key="user_id_input_field",
            label_visibility="collapsed"
        )
        submitted = st.form_submit_button("Iniciar Conversa com AURA")

        if submitted:
            if user_name.strip():
                st.session_state.current_user_id = user_name.strip()
            st.session_state.user_id_confirmed = True
            st.session_state.welcome_message_shown = False
            st.rerun()  # Substitui st.experimental_rerun()

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

    if prompt := st.chat_input("Como você está se sentindo hoje?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="✨"):
            with st.spinner("AURA está digitando..."):
                try:
                    aura_response_text = aura_bot.interact(prompt)
                    st.markdown(aura_response_text)
                    st.session_state.messages.append({"role": "assistant", "content": aura_response_text})
                except Exception as e:
                    st.error(f"Erro na geração da resposta: {str(e)}")

        if prompt.strip().lower() in ["sair", "exit", "tchau"]:
            st.success("Conversa encerrada e histórico salvo! Para iniciar uma nova conversa, atualize a página ou clique no botão abaixo.")

    st.markdown("---")
    if st.button("Iniciar Nova Conversa / Trocar Usuário"):
        save_current_conversation()
        st.session_state.clear()
        st.rerun()
