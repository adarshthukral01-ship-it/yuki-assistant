"""
Yuki Assistant Framework - Main Entry Point
Demonstrates voice and text interaction loop for Yuki AI Assistant.
"""

import sys
from yuki.tts import TextToSpeech
from yuki.speech import SpeechRecognizer
from yuki.commands import CommandHandler

def main():
    print("=" * 50)
    print("  Yuki AI Assistant Framework v1.0.0")
    print("=" * 50)
    
    tts = TextToSpeech()
    recognizer = SpeechRecognizer()
    handler = CommandHandler()

    welcome = "Hello! I am Yuki, your mobile and desktop assistant. How can I help you today?"
    print(f"\nYuki: {welcome}")
    tts.speak(welcome)

    # Mode selection
    print("\nSelect Input Mode:")
    print("1. Text Mode (Keyboard input)")
    print("2. Voice Mode (Microphone speech recognition)")
    
    try:
        choice = input("Enter choice (1 or 2, default 1): ").strip()
    except (KeyboardInterrupt, EOFError):
        choice = "1"

    voice_mode = (choice == "2")
    
    if voice_mode:
        print("\n[Voice Mode Activated] Speak into your microphone...")
    else:
        print("\n[Text Mode Activated] Type your commands below (e.g., 'time', 'open whatsapp', 'battery', 'exit')")

    running = True
    while running:
        try:
            if voice_mode:
                user_input = recognizer.listen(timeout=5)
                if user_input:
                    print(f"\nYou: {user_input}")
                else:
                    print(".", end="", flush=True)
                    continue
            else:
                user_input = input("\nYou: ")

            response, should_continue = handler.process(user_input)
            print(f"Yuki: {response}")
            tts.speak(response)

            if not should_continue:
                running = False

        except (KeyboardInterrupt, EOFError):
            print("\nExiting Yuki. Goodbye!")
            tts.speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
