import speech_recognition as sr
import sounddevice as sd

# Set the sample rate and duration of the recording
sample_rate = 44100
duration = 5

# Record audio from the microphone
audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1)

# Wait for the recording to finish
sd.wait()

# Convert the audio data to a format that SpeechRecognition can use
audio_bytes = audio.tobytes()

# Transcribe the audio into text
r = sr.Recognizer()
text = r.recognize_google(audio_bytes)

# Print the transcribed text
print("Transcribed text:", text)