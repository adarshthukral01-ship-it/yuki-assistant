"""
Yuki Text-To-Speech (TTS) Module
Handles speaking out text responses using pyttsx3.
"""

import pyttsx3

class TextToSpeech:
    def __init__(self, rate=170, volume=1.0):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('volume', volume)
        except Exception as e:
            print(f"TTS initialization error: {e}")
            self.engine = None

    def speak(self, text):
        """
        Speaks the given text aloud.
        """
        if not self.engine:
            print(f"[TTS Mock]: {text}")
            return
        
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error during speech output: {e}")
            print(f"[TTS Fallback]: {text}")

    def set_property(self, name, value):
        if self.engine:
            self.engine.setProperty(name, value)
