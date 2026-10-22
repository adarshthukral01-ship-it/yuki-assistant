# Yuki Assistant Framework 🤖

A modular Python AI assistant framework built for voice and text input, app navigation shortcuts, mock/Termux phone operations, and text-to-speech feedback.

## Features

- **Speech Recognition**: Voice input via `speech_recognition` (Google Speech API).
- **Text-to-Speech (TTS)**: Voice responses using `pyttsx3`.
- **Custom Command Handling**: Time, date, weather, app launching (WhatsApp, YouTube), battery queries, calling, and messaging.
- **Mobile Integration Layer**: Detects Android environments (Termux / Kivy) and uses `termux-api` utilities where supported, with clear mock fallbacks for standard desktop environments.

## Mobile Control Notice 📱

> **Note on Direct Mobile Control from Python on Android:**
> Executing OS and hardware-level operations (calling cellular networks, hardware battery level, system intents) directly from standard Python scripts on Android is constrained by OS sandboxing.
> Full mobile control requires specialized Android bridge APIs or native wrappers:
> - **Termux + Termux API**: Shell utilities (`termux-telephony-call`, `termux-battery-status`, `termux-open-url`).
> - **Pyjnius / Kivy Android**: Android Java API wrappers for Android SDK (`android.content.Intent`, `android.net.Uri`).
> - **SL4A (Scripting Layer for Android) / ADB commands**.

## File Structure

