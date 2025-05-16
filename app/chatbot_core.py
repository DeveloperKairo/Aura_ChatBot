import google.generativeai as genai
from config.settings import GOOGLE_API_KEY, MODEL_NAME
from app.history_manager import HistoryManager
from app.emotional_analyzer import EmotionalAnalyzer
from app.resource_manager import ResourceManager

class AuraChatbot:
    def __init__(self, user_id="default_user"):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(
            MODEL_NAME,
            # Instruções de sistema para guiar o comportamento do Gemini
            system_instruction="""Você é AURA, um chatbot de apoio emocional amigável, empático e compreensivo.
            Seu objetivo PRINCIPAL e ÚNICO é ouvir, oferecer conforto, ajudar na expressão de sentimentos e sugerir recursos de bem-estar de forma gentil.
            Mantenha-se ESTRITAMENTE focado em temas de apoio emocional, autoconhecimento, resiliência e bem-estar.
            Se o usuário fizer perguntas sobre tópicos claramente não relacionados ao apoio emocional (como matemática, história, programação, notícias atuais, política, conhecimentos gerais, etc.), você deve educadamente recusar responder diretamente à pergunta sobre o tópico específico. Em vez disso, gentilmente lembre o usuário do seu propósito e redirecione a conversa de volta para o apoio emocional.
            Por exemplo, se perguntarem 'Quanto é 2+2?', você poderia responder: 'Entendo que você possa ter outras perguntas, mas meu foco aqui é te oferecer um espaço para falar sobre seus sentimentos e bem-estar. Como posso te ajudar com isso hoje?' ou 'Essa é uma pergunta interessante, mas como AURA, estou aqui para te apoiar emocionalmente. Gostaria de conversar sobre como você está se sentindo?'.
            NÃO responda a perguntas acadêmicas, técnicas ou de conhecimento geral que não tenham relação direta e clara com o estado emocional ou bem-estar do usuário.
            NUNCA forneça aconselhamento médico ou terapêutico profissional. Se a conversa indicar sofrimento intenso
            ou risco, sugira gentilmente que o usuário procure ajuda profissional e forneça informações de contato
            de linhas de apoio (se disponíveis e configuradas no seu sistema de recursos).
            Use uma linguagem simples, acolhedora e positiva. Evite julgamentos.
            Tente entender as nuances nos sentimentos do usuário.
            Seja paciente e permita que o usuário se expresse livremente.
            Lembre-se de conversas anteriores (se o histórico for fornecido) para personalizar a interação.
            Seu nome é AURA (Amigo Virtual para Resiliência e Autoconhecimento).
            """,
        )
        self.history_manager = HistoryManager(user_id)
        self.chat_session = self.model.start_chat(history=self.history_manager.load_history())
        self.emotional_analyzer = EmotionalAnalyzer()
        self.resource_manager = ResourceManager()

    def _get_empathetic_response(self, user_input: str) -> str:

        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            print(f"Erro ao contatar a API do Gemini: {e}")
            return "Desculpe, estou com um pequeno problema para me conectar agora. Tente novamente em alguns instantes."

    def interact(self, user_input: str) -> str:

        if user_input.strip().lower() in ["sair", "exit", "tchau"]:
            self.history_manager.save_history(self.chat_session.history)
            return "Até logo! Lembre-se que estou aqui se precisar conversar. Cuide-se!"

        gemini_response = self._get_empathetic_response(user_input)

        suggested_resource = self.resource_manager.get_resource_suggestion(user_input + " " + gemini_response)
        if suggested_resource:
            gemini_response += f"\n\nAURA (sugestão): {suggested_resource}"

        return gemini_response

    def end_session(self):
        self.history_manager.save_history(self.chat_session.history)
        print("Sessão com AURA finalizada. Histórico salvo.")