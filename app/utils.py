def format_as_aura_name(text: str) -> str:
    return f"AURA: {text}"

def format_as_user_name(text: str, user_name="Você") -> str:
    return f"{user_name}: {text}"

def display_welcome_message():
    print("=" * 50)
    print(" Bem-vindo(a) ao AURA - Seu Amigo Virtual para Apoio Emocional ")
    print("=" * 50)
    print("Olá! Sou AURA, aqui para te ouvir e oferecer um espaço seguro.")
    print("Lembre-se: não sou um profissional de saúde mental, mas posso te oferecer apoio e recursos.")
    print("Se estiver em crise, por favor, procure ajuda profissional imediatamente (ex: CVV 188).")
    print("Digite 'sair' a qualquer momento para encerrar nossa conversa.")
    print("-" * 50)

def display_privacy_notice():
    print("\n--- Aviso de Privacidade ---")
    print("Suas conversas podem ser salvas localmente para personalizar futuras interações.")
    print("Não compartilhamos seus dados com terceiros sem seu consentimento.")
    print("Você pode solicitar a exclusão do seu histórico a qualquer momento (funcionalidade futura).")
    print("--------------------------\n")