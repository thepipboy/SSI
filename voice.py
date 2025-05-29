import whisper
import pyttsx3

model = whisper.load_model("base")
audio_text = model.transcribe("audio.wav")["text"]

engine = pyttsx3.init()
engine.say(audio_text)
engine.runAndWait()