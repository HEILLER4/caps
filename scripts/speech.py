import vosk
import pyttsx3
import json
import pyaudio

class SpeechHandler:
    def __init__(self, model_path):
        self.model = vosk.Model(model_path)
        self.engine = pyttsx3.init()

    def recognize_speech(self):
        recognizer = vosk.KaldiRecognizer(self.model, 16000)
        mic = pyaudio.PyAudio()
        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
        stream.start_stream()

        while True:
            data = stream.read(4000)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                return result["text"]

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
