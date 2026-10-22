"""
Yuki Phone Operations Module (Mock & Mobile Integration Layer)

Note on Android / Mobile Execution:
Direct hardware and OS control (like opening Android apps via Intents, making actual cellular 
calls, sending SMS, or reading device battery) from Python on Android requires 
Android-specific APIs or bridge frameworks such as:
  - Termux API (`termux-telephony-call`, `termux-battery-status`, `termux-open-url`)
  - Pyjnius / Kivy Android API (Java Native Interface wrapper for Android SDK)
  - Android Intents via Android SL4A or ADB commands

This module provides mock/fallback functionality for standard Python environments 
while documenting and attempting Termux/Android integration where available.
"""

import os
import subprocess
import sys
import webbrowser

class PhoneOperations:
    def __init__(self):
        self.is_android = self._detect_android()

    def _detect_android(self):
        """
        Detects if running inside an Android environment like Termux or Kivy.
        """
        return "ANDROID_ARGUMENT" in os.environ or "TERMUX_VERSION" in os.environ or hasattr(sys, 'getandroidapilevel')

    def make_call(self, phone_number: str) -> bool:
        """
        Initiates a phone call or simulates it if on standard OS.
        """
        print(f"Initiating call to: {phone_number}")
        if self.is_android:
            try:
                # Termux API integration attempt
                subprocess.run(["termux-telephony-call", phone_number], check=True)
                return True
            except (FileNotFoundError, subprocess.SubprocessError):
                print("[Phone Mock]: Termux API not available. Simulated calling.")
                return True
        else:
            print(f"[Phone Mock Desktop]: Calling {phone_number} (Simulation mode)")
            return True

    def send_sms(self, phone_number: str, message: str) -> bool:
        """
        Sends an SMS message or simulates it.
        """
        print(f"Sending SMS to {phone_number}: '{message}'")
        if self.is_android:
            try:
                # Termux API integration attempt
                subprocess.run(["termux-sms-send", "-n", phone_number, message], check=True)
                return True
            except (FileNotFoundError, subprocess.SubprocessError):
                print("[Phone Mock]: Termux API not available. Simulated SMS.")
                return True
        else:
            print(f"[Phone Mock Desktop]: SMS sent to {phone_number} (Simulation mode)")
            return True

    def get_battery_status(self) -> dict:
        """
        Retrieves device battery level and charging status.
        """
        if self.is_android:
            try:
                # Termux API integration attempt
                result = subprocess.run(["termux-battery-status"], capture_output=True, text=True, check=True)
                import json
                return json.loads(result.stdout)
            except Exception:
                pass

        # Mock response for standard environments or fallbacks
        return {
            "percentage": 85,
            "plugged": "UNPLUGGED",
            "status": "Mock Battery (85%)"
        }

    def open_app(self, app_name: str) -> bool:
        """
        Opens an application on the device or web fallback.
        Examples: 'whatsapp', 'youtube'
        """
        app_clean = app_name.lower().strip()
        print(f"Opening app: {app_clean}")

        if app_clean == "whatsapp":
            if self.is_android:
                try:
                    # Attempt Android intent or termux-open-url deep link
                    subprocess.run(["termux-open-url", "https://api.whatsapp.com"], check=True)
                    return True
                except Exception:
                    pass
            webbrowser.open("https://web.whatsapp.com")
            return True

        elif app_clean == "youtube":
            if self.is_android:
                try:
                    subprocess.run(["termux-open-url", "https://www.youtube.com"], check=True)
                    return True
                except Exception:
                    pass
            webbrowser.open("https://www.youtube.com")
            return True

        else:
            print(f"[Phone Mock]: App '{app_name}' launch simulated.")
            return True
