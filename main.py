from app.chatbot_core import AuraChatbot
from app.utils import display_welcome_message, format_as_aura_name, format_as_user_name, display_privacy_notice
import uuid 

def run_aura_cli():
    user_id = input("Para começarmos, por favor, me diga seu nome ou um apelido (isso ajudará a lembrar de nossas conversas): ").strip()
    if not user_id:
        user_id = f"user_{str(uuid.uuid4())[:8]}" 
        print(f"Ok, vamos usar um identificador anônimo por enquanto: {user_id}")

    aura_bot = AuraChatbot(user_id=user_id)

    display_welcome_message()
    display_privacy_notice() 

    try:
        while True:
            user_input = input(format_as_user_name("", user_name=user_id) + " ")
            if user_input.strip().lower() in ["sair", "exit", "tchau"]:
                response = aura_bot.interact(user_input) 
                print(format_as_aura_name(response))
                break

            if not user_input.strip(): 
                continue

            aura_response = aura_bot.interact(user_input)
            print(format_as_aura_name(aura_response))

    except KeyboardInterrupt:
        print(format_as_aura_name("\nEntendido. Encerrando nossa conversa. Cuide-se!"))
    finally:
        aura_bot.end_session() 

if __name__ == "__main__":
    run_aura_cli()