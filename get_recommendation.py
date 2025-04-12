def get_recommendation(preference: str) -> str:
    preference = preference.lower().strip()

    if preference == "breathing":
        return "🧘‍♀️ Here's a calming breathing exercise to help you relax. Would you like to begin now?"
    elif preference == "yoga":
        return "🧎‍♂️ Let's do some gentle yoga stretches together. Ready to start?"
    elif preference == "meditation":
        return "🧘 Would you like to try a short guided meditation session to clear your mind?"
    elif preference == "music":
        return "🎵 I can play some relaxing background music. Want to listen?"
    elif preference == "journal":
        return "📓 Want to reflect a bit? I can guide you through a short journaling prompt."
    elif preference == "walk":
        return "🚶 A short mindful walk might help. Would you like a quick outdoor mindfulness tip?"
    elif preference == "hydration":
        return "💧 Let's take a hydration break. Drinking water can help reset your focus."
    else:
        return "✨ I can suggest a quick mindfulness activity. Would you like to give it a try?"
