import azure.cognitiveservices.speech as speechsdk
from config import DefaultConfig

config = DefaultConfig()

def speech_to_text():
    if not config.SPEECH_KEY or not config.SPEECH_REGION:
        print("Missing Speech API configuration.")
        return ""

    speech_config = speechsdk.SpeechConfig(subscription=config.SPEECH_KEY, region=config.SPEECH_REGION)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("🎙️ Speak into your microphone...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("✅ Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("⚠️ Speech could not be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print("❌ Canceled: {}".format(cancellation.reason))
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation.error_details))
    return ""
