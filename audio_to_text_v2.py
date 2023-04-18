import requests
import speech_recognition as sr

# Define the WhisperAPI endpoint and API key
whisper_api_endpoint = "https://api.silero.ai/transcription/api/v1/whisper"
# api_key = , enter your API key here

# Initialize the speech recognition engine
r = sr.Recognizer()

# Set up the microphone as the audio source
with sr.Microphone() as source:
    print("Speak now...")
    audio_data = r.record(source, duration=5)

# Send the audio data to the WhisperAPI
response = requests.post(
    whisper_api_endpoint,
    headers={"Authorization": f"Bearer {api_key}"},
    data=audio_data.get_wav_data(),
)

# Print the transcribed text
if response.status_code == 200:
    text = response.json()["text"]
    print(f"Transcribed text: {text}")
else:
    print(f"Unable to transcribe audio. Error code: {response.status_code}")
