import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav
sound = AudioSegment.from_mp3("song2.mp3")
sound.export("song2.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "song2.wav"

# song 2 is working as the audio is clearer than song 1.

# use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    r.recognize_google(audio, language="en-US")  # Specify the appropriate language code
    # read the entire audio file

    print("Transcription: " + r.recognize_google(audio))
