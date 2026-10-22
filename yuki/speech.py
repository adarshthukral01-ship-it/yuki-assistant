"""
Yuki Speech Recognition Module
Handles listening to microphone input and converting speech to text.
"""

import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, language="en-US"):
        self.recognizer = sr.Recognizer()
        self.language = language

    def listen(self, timeout=5, phrase_time_limit=10):
        """
        Listens to microphone input and returns the recognized text.
        """
        try:
            with sr.Microphone() as source:
                print("Yuki is listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            print("Processing speech...")
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return ""
        except Exception as e:
            print(f"Microphone error (Note: mobile environment may require specific permissions/APIs): {e}")
            return ""
