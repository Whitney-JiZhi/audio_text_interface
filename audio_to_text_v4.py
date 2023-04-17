import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    # Set a threshold for voice activity detection
    r.adjust_for_ambient_noise(source)
    # Prompt the user to speak
    print("Please say something...")
    # Record audio from the user
    audio = r.listen(source)

# Transcribe the audio into text
try:
    text = r.recognize_google(audio)
    print(f"Transcribed text: {text}")
except sr.UnknownValueError:
    print("Unable to transcribe audio")