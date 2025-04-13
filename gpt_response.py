
import openai
import os
import requests
#from openai import AzureOpenAI
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential


import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)


client = ChatCompletionsClient(
    endpoint='https://s2249-m9dydovh-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4o',
    credential=AzureKeyCredential("")
)


# Define a function to generate a response using OpenAI client.chat.
#os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # The model deployed in your Azure OpenAI resource (e.g., 'gpt-4')
def generate_response(message, sentiment, key_phrases):
 try:
    prompt = f"The user is feeling {sentiment} and mentioned {', '.join(key_phrases)}. Generate a calming and empathetic response to help the user."

    payload = {
    "messages": [
        {
        "role": "user",
        "content": f"The user is feeling {sentiment} and mentioned {', '.join(key_phrases)}. Generate a calming and empathetic response to help the user."

        }
    ],
    "max_tokens": 4096,
    "temperature": 1,
    "top_p": 1,
    "stop": []
    }
    response = client.complete(payload)
    # response = client.complete(            
    #         messages=prompt,
    #         max_tokens=150,
    #         temperature=0.7,
    #         top_p=0.95,
    #         frequency_penalty=0,
    #         presence_penalty=0.6,
    #         stop=None
    #     )
   
    return response.choices[0].message.content
 except Exception as e:
    return f"⚠️ Failed to generate response: {str(e)}"






