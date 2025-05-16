import re

class EmotionalAnalyzer:
    def __init__(self):
        self.keywords_map = {
            "triste": [
                "triste", "chateado", "baixo", "deprimido", "abatido", "melancólico",
                "desanimado", "infeliz", "desmotivado", "na bad", "bad", "mal", 
                "emo", "pra baixo", "deprê"
            ],
            "ansioso": [
                "ansioso", "preocupado", "nervoso", "medo", "tenso", "aflito",
                "inseguro", "apreensivo", "agitado", "temeroso", "pilhado", 
                "acelerado", "no pique", "com pressa", "paranoico"
            ],
            "estressado": [
                "estresse", "sobrecarregado", "pressão", "cansado", "exausto",
                "irritado", "nervoso", "acelerado", "esgotado", "preocupação",
                "sem paciência", "de saco cheio", "estress", "estressadão", 
                "na correria"
            ],
            "solitário": [
                "sozinho", "solitário", "isolado", "abandonado", "ignorado",
                "excluído", "distante", "carente", "desconectado", "afastado",
                "sem ninguém", "sem companhia", "forever alone", "largado", 
                "esquecido"
            ],
            "feliz": [
                "feliz", "contente", "alegre", "ótimo", "animado", "empolgado",
                "radiante", "grato", "satisfeito", "realizado", "de boa", 
                "suave", "tranquilo", "daora", "top", "show"
            ],
            "respiração": [
                "respirar", "respiração", "acalmar", "inspiração", "expiração",
                "fôlego", "respirando", "oxigenar", "trazer o ar", "puxar o ar",
                "dar um respiro", "dar um tempo", "parar um pouco", "pausar", 
                "sossegar"
            ],
            "meditação": [
                "meditar", "meditação", "mindfulness", "contemplar", "refletir",
                "centrar", "equilibrar", "atenção plena", "foco interior", "relaxamento",
                "zen", "ficar de boa", "focar na mente", "limpar a cabeça", 
                "acalma mente"
            ]
        }

    def detect_keywords(self, text: str) -> list:

        detected = []
        text_lower = text.lower()
        for sentiment, keys in self.keywords_map.items():
            for key in keys:
                if re.search(r'\b' + re.escape(key) + r'\b', text_lower):
                    detected.append(sentiment)
                    break 
        return list(set(detected)) 

    def get_sentiment_nuance(self, text: str) -> str:

        keywords = self.detect_keywords(text)
        if keywords:
            return f"Detectei menções a: {', '.join(keywords)}. Como posso ajudar com isso?"
        return ""