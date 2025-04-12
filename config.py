import os

class DefaultConfig:
    APP_ID = "2f5e21a3-eb85-4652-8e06-d7a72b34eb63"#os.getenv("MicrosoftAppId", "")
    APP_PASSWORD ="fbbb2d88-f504-458b-81e2-c2c0c7be1822" #os.getenv("MicrosoftAppPassword", "")
    COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT", "")
    COSMOS_KEY = os.getenv("COSMOS_KEY", "")
    SPEECH_KEY = os.getenv("SPEECH_KEY", "")
    SPEECH_REGION = os.getenv("SPEECH_REGION", "")

