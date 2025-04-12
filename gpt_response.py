
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

# client = AzureOpenAI(
#   azure_endpoint = "https://s2249-m9dydovh-eastus2.openai.azure.com/", 
#   azure_ad_token_provider="2SKMnXkuBUTxY5QtrFi25DmC1MjNG8mFL3DD5hgY1BtIWmx4AXt2JQQJ99BDACHYHv6XJ3w3AAAAACOGXzDr",
#   api_version="2024-12-01-preview"
# )

client = ChatCompletionsClient(
    endpoint='https://s2249-m9dydovh-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4o',
    credential=AzureKeyCredential("2SKMnXkuBUTxY5QtrFi25DmC1MjNG8mFL3DD5hgY1BtIWmx4AXt2JQQJ99BDACHYHv6XJ3w3AAAAACOGXzDr")
)

# Set up Azure OpenAI API credentials
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., "https://your-resource-name.openai.azure.com"
# openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")   # The API key from Azure OpenAI resource
# openai.api_version = "2023-05-15"  # Use the version you are working with (check Azure documentation)

#openai.api_base = "https://s2249-m9dydovh-eastus2.openai.azure.com/"
#openai.api_key = "2SKMnXkuBUTxY5QtrFi25DmC1MjNG8mFL3DD5hgY1BtIWmx4AXt2JQQJ99BDACHYHv6XJ3w3AAAAACOGXzDr"
#openai.api_version = "2024-12-01-preview"
#openai.api_base = "https://s2249-m9dydovh-eastus2.cognitiveservices.azure.com/"
#openai.api_key = "93474448-28c1-497a-94f0-d626ae495fe1"#"2SKMnXkuBUTxY5QtrFi25DmC1MjNG8mFL3DD5hgY1BtIWmx4AXt2JQQJ99BDACHYHv6XJ3w3AAAAACOGXzDr"

# client = AzureOpenAI(
#     api_version="2024-12-01-preview",
#     azure_endpoint="https://s2249-m9dydovh-eastus2.cognitiveservices.azure.com/",
#     api_key="93474448-28c1-497a-94f0-d626ae495fe1",
# )

# Check if the endpoint is accessible
# try:
#     response = requests.get("https://s2249-m9dydovh-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2025-01-01-preview")
#     response.raise_for_status()  # If the request failed, this will raise an error
#     print("Successfully connected to Azure OpenAI Endpoint")
# except requests.exceptions.RequestException as e:
#     print(f"Failed to connect to Azure OpenAI: {e}")


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






