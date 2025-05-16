import json
import os
from typing import List, Dict, Union


MessagePart = Union[str, Dict] 
Turn = Dict[str, Union[str, List[MessagePart]]] 

class HistoryManager:
    def __init__(self, user_id: str, history_dir="data/user_histories"):
        self.user_id = user_id
        # Garante que o caminho para o diretório de histórico seja relativo à raiz do projeto
        base_dir = os.path.join(os.path.dirname(__file__), '..') # Sai de /app para /aura_chatbot
        self.history_file_path = os.path.join(base_dir, history_dir, f"{self.user_id}_history.json")
        self.history_dir_path = os.path.join(base_dir, history_dir)


        os.makedirs(self.history_dir_path, exist_ok=True)

    def load_history(self) -> List[Turn]:

        try:
            with open(self.history_file_path, 'r', encoding='utf-8') as f:
                history_data: List[Turn] = json.load(f)

                if isinstance(history_data, list) and all(
                    isinstance(turn, dict) and
                    "role" in turn and
                    "parts" in turn and
                    isinstance(turn["parts"], list)
                    for turn in history_data
                ):
                    return history_data
                else:
                    print(f"Formato de histórico inválido para {self.user_id} em {self.history_file_path}. Iniciando novo histórico.")
                    return []
        except (FileNotFoundError):

            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o JSON do histórico em {self.history_file_path}. Iniciando novo histórico.")
            return [] 

    def save_history(self, chat_session_history: list):

        serializable_history: List[Turn] = []
        for content_message in chat_session_history:
          
            role = content_message.role 
            
            current_parts: List[MessagePart] = []
            for part in content_message.parts: 

                if hasattr(part, 'text') and isinstance(part.text, str):
                    current_parts.append(part.text)

            if current_parts:
                serializable_history.append({"role": role, "parts": current_parts})
            elif role: 
                serializable_history.append({"role": role, "parts": []})


        try:
            with open(self.history_file_path, 'w', encoding='utf-8') as f:
                json.dump(serializable_history, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Erro de I/O ao salvar o histórico para {self.user_id} em {self.history_file_path}: {e}")
        except TypeError as e:

            print(f"Erro de Tipo (serialização) ao salvar o histórico: {e}")
            print("Isso geralmente significa que um objeto não serializável ainda está presente.")
            print(f"Dados que tentaram ser serializados: {serializable_history}")
        except Exception as e:
            print(f"Um erro inesperado ocorreu ao salvar o histórico para {self.user_id}: {e}")

