from botbuilder.core import ActivityHandler, TurnContext
from sentiment_analysis import analyze_text
from gpt_response import generate_response
#from db import save_user_preference, save_feedback, get_user_preference
import datetime
from get_recommendation import get_recommendation

class StressReliefBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Get user input and user id from the activity
        user_input = turn_context.activity.text
        user_id = turn_context.activity.from_property.id

        # ✅ Validate input
        if not user_input or not user_input.strip():
            await turn_context.send_activity("⚠️ I didn't catch that. Could you please try saying that again?")
            return

        # ✅ Analyze text with error handling
        try:
            analysis = analyze_text(user_input)
            sentiment = analysis["sentiment"]
            key_phrases = analysis["key_phrases"]
        except Exception as e:
            await turn_context.send_activity(f"⚠️ Sorry, I couldn't analyze your message. ({str(e)})")
            return

        # Generate response based on sentiment and key phrases
        gpt_reply = generate_response(user_input, sentiment, key_phrases)

        # Auto-detect preference based on sentiment (mood)
        if sentiment == "negative":
            preference = "meditation"  # Suggest meditation if the mood is negative
        elif sentiment == "positive":
            preference = "yoga"  # Suggest yoga if the mood is positive
        else:
            preference = "breathing"  # Default to breathing if the mood is neutral

        # Save the detected preference in Cosmos DB
        #save_user_preference(user_id, preference)

        # Get the user's current preference from Cosmos DB (to maintain consistency)
        #preference = get_user_preference(user_id)
        
        # Personalize the recommendation based on preference and time of day
        recommendation = self.get_personalized_recommendation(preference)
        #recommendation = get_recommendation(preference)

        # Save user feedback (assuming thumbs_up is used as a sample feedback)
        #save_feedback(user_id, user_input, "thumbs_up")

        # Send GPT reply and recommendation to the user
        full_reply = f"{gpt_reply}\n\n{recommendation}"
        await turn_context.send_activity(full_reply)

    async def on_members_added_activity(self, members_added, turn_context: TurnContext):
        # Send a greeting message when a new user starts interacting with the bot
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hi there! How are you feeling today?")

    def get_personalized_recommendation(self, preference):
        """Personalize the recommendation based on preference and time of day"""
        # Get current time
        current_time = datetime.datetime.now().hour

        # Recommend based on time of day (morning, afternoon, or evening)
        if 6 <= current_time < 12:
            recommendation = f"How about some {preference} exercises to start your day?"
        elif 12 <= current_time < 18:
            recommendation = f"It's afternoon, how about a {preference} session to relax?"
        else:
            recommendation = f"As it's evening, a {preference} session could help you unwind."

        return recommendation
