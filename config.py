import os

class DefaultConfig:
    APP_ID = ""#os.getenv("MicrosoftAppId", "")
    APP_PASSWORD ="" #os.getenv("MicrosoftAppPassword", "")
    COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT", "")
    COSMOS_KEY = os.getenv("COSMOS_KEY", "")
    SPEECH_KEY = os.getenv("SPEECH_KEY", "")
    SPEECH_REGION = os.getenv("SPEECH_REGION", "")

