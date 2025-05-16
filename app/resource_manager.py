import json
import os
import random

class ResourceManager:
    def __init__(self, resources_file="data/resources.json"):
        self.resources_path = os.path.join(os.path.dirname(__file__), '..', resources_file) 
        self._load_resources()

    def _load_resources(self):
        try:
            with open(self.resources_path, 'r', encoding='utf-8') as f:
                self.resources = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo de recursos não encontrado em {self.resources_path}. Criando com estrutura padrão.")
            self.resources = {} 
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o JSON em {self.resources_path}. Verifique o formato do arquivo.")
            self.resources = {}


    def get_resource_suggestion(self, text: str) -> str | None:

        text_lower = text.lower()

        professional_help_resource = self.resources.get("professional_help_info")
        if professional_help_resource:
            for keyword in professional_help_resource.get("keywords", []):
                if keyword in text_lower:
                    return f"{professional_help_resource['text']} {professional_help_resource.get('link', '')}".strip()

        possible_suggestions = []
        for key, resource_data in self.resources.items():
            if key == "professional_help_info": 
                continue
            for keyword in resource_data.get("keywords", []):
                if keyword in text_lower:
                    suggestion = resource_data['text']
                    if resource_data.get('link'):
                        suggestion += f" Você pode encontrar mais aqui: {resource_data['link']}"
                    possible_suggestions.append(suggestion)
                    break 

        if possible_suggestions:
            return random.choice(possible_suggestions) 
        return None