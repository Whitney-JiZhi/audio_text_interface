import sounddevice as sd
import soundfile as sf
import requests
import json

# Set up the API endpoint and access token
url = "https://api.whisper.ai/v1/transcriptions"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "audio/wav"
}

# Set the audio parameters
duration = 5  # seconds
sample_rate = 44100  # Hz
channels = 1

# Use sounddevice to capture audio data from the default microphone
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

# Wait for the audio data to be recorded
sd.wait()

# Save the audio data to a WAV file
filename = "audio.wav"
sf.write(filename, audio_data, sample_rate)

# Read the audio data from the WAV file
with open(filename, "rb") as f:
    audio_data = f.read()

# Send the audio data to the Whisper API for transcription
response = requests.post(url, headers=headers, data=audio_data)

# Parse the response JSON and print the transcribed text
if response.ok:
    json_data = json.loads(response.text)
    text = json_data["transcription"]["text"]
    print(f"Transcribed text: {text}")
else:
    print("Error: Unable to transcribe audio")