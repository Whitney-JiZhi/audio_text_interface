import speech_recognition as sr
import sounddevice as sd
import wavio
import wave

# Set the sampling rate and the duration of the recording
sample_rate = 16000
duration = 5  # in seconds

# Create an instance of the Recognizer class
r = sr.Recognizer()

# Use the microphone as the audio source
print("Speak now...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()

# Save the recorded audio to a WAV file
file_path = "recording.wav"
wavio.write(file_path, audio, sample_rate, sampwidth=2)

# Transcribe the audio into text using Google Web Speech API
with wave.open(file_path, "rb") as wave_file:
    audio_data = wave_file.readframes(-1)

try:
    text = r.recognize_google(audio_data, language="en-US")
    print(f"Transcribed text: {text}")
except sr.UnknownValueError:
    print("Unable to transcribe audio")