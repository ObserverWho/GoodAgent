import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LLM_API_BASE = os.getenv("LLM_API_BASE")
    LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")
    SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    print(LLM_API_BASE)


settings = Settings()
