import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes

from speech_to_text import speech_to_text
from sentiment_analysis import analyze_text
from gpt_response import generate_response
from get_recommendation import get_recommendation

# Load credentials
APP_ID = os.getenv("MicrosoftAppId", "")
APP_PASSWORD = os.getenv("MicrosoftAppPassword", "")
adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

# Webhook to handle incoming messages
async def message_handler(request: web.Request) -> web.Response:
    body = await request.json()
    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")

    async def logic(turn_context: TurnContext):
        user_input = turn_context.activity.text

        # If no text in message, attempt speech recognition (mock logic)
        # if not user_input:
        #     user_input = speech_to_text()

        # 1. Analyze emotion and key phrases
        analysis = analyze_text(user_input)

        # 2. Get GPT response
        gpt_reply = generate_response(user_input, analysis["sentiment"], analysis["key_phrases"])

        # 3. Retrieve recommendation (mocked)
        preference = "breathing"  # Placeholder; could come from Cosmos DB
        recommendation = get_recommendation(preference)

        # 4. Combine and send response
        full_reply = f"{gpt_reply}" #\n\n{recommendation}
        await turn_context.send_activity(Activity(type=ActivityTypes.message, text=full_reply))

    await adapter.process_activity(activity, auth_header, logic)
    return web.Response(status=200)

# Set up web server
app = web.Application()
app.router.add_post("/api/messages", message_handler)

if __name__ == "__main__":
    web.run_app(app, port=3978)
