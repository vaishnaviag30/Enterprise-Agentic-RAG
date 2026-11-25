import os
from dotenv import load_dotenv, dotenv_values
from app.config import settings

file_key = dotenv_values(".env").get("GROQ_API_KEY")
loaded_key = settings.GROQ_API_KEY

print("Key exists in .env:", bool(file_key))
print("Key exists in settings:", bool(loaded_key))

print("Key length in .env:", len(file_key) if file_key else 0)
print("Key length in settings:", len(loaded_key) if loaded_key else 0)

print("Settings key matches .env:", loaded_key == file_key)

print("Windows environment key exists:", bool(os.environ.get("GROQ_API_KEY")))