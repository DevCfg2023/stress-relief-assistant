from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")
key = os.getenv("TEXT_ANALYTICS_KEY")

def authenticate_client():
    return TextAnalyticsClient(endpoint='https://stress-bot-text.cognitiveservices.azure.com/', credential=AzureKeyCredential('b5debe5af4aa48e59dcb73917a649c8a')) #AzureKeyCredential(key)



def analyze_text(user_input):
    client = authenticate_client()
    # if not user_input or user_input.strip() == "":
    #     return {"sentiment": "neutral", "key_phrases": []}  # Default for empty input

    try:
        response = client.analyze_sentiment([user_input])
        sentiment = response[0].sentiment
        key_phrases_response = client.extract_key_phrases([user_input])
        key_phrases = key_phrases_response[0].key_phrases
        
        return {"sentiment": sentiment, "key_phrases": key_phrases}
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return {"sentiment": "neutral", "key_phrases": []}  # Default in case of error

# def analyze_text(text):
#     client = authenticate_client()
#     documents = [text]

#     response = client.analyze_sentiment(documents=documents)[0]
#     key_phrases = client.extract_key_phrases(documents=documents)[0]

#     print("Sentiment:", response.sentiment)
#     print("Key Phrases:", key_phrases.key_phrases)

#     return {
#         "sentiment": response.sentiment,
#         "key_phrases": key_phrases.key_phrases
#     }

# def analyze_text(text):
#     endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")
#     key = os.getenv("TEXT_ANALYTICS_KEY")
    
#     client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
#     response = client.analyze_sentiment([text])[0]
#     sentiment = response.sentiment
#     key_phrases = response.key_phrases
    
#     return {"sentiment": sentiment, "key_phrases": key_phrases}

