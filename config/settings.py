import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("A variável de ambiente GOOGLE_API_KEY não foi definida. Crie um arquivo .env ou defina-a no seu ambiente.")

MODEL_NAME = "gemini-1.5-flash-latest" 