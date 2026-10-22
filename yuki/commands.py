"""
Yuki Command Handler Module
Processes spoken or typed commands and routes them to appropriate actions.
"""

import datetime
from yuki.phone import PhoneOperations

class CommandHandler:
    def __init__(self):
        self.phone = PhoneOperations()

    def process(self, text: str) -> tuple[str, bool]:
        """
        Processes string input and executes appropriate logic.
        Returns a tuple: (response_text, should_continue)
        """
        if not text or not text.strip():
            return "I didn't hear anything.", True

        cmd = text.lower().strip()

        # Exit / Stop commands
        if any(w in cmd for w in ["exit", "quit", "stop", "bye", "goodbye"]):
            return "Goodbye! Have a great day.", False

        # Time command
        elif "time" in cmd:
            now = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {now}.", True

        # Date command
        elif "date" in cmd or "day" in cmd:
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {today}.", True

        # Open WhatsApp
        elif "whatsapp" in cmd:
            self.phone.open_app("whatsapp")
            return "Opening WhatsApp for you.", True

        # Open YouTube
        elif "youtube" in cmd:
            self.phone.open_app("youtube")
            return "Opening YouTube for you.", True

        # Battery Status
        elif "battery" in cmd:
            info = self.phone.get_battery_status()
            pct = info.get("percentage", "unknown")
            plugged = info.get("plugged", "UNPLUGGED")
            status_str = f"Battery is at {pct}% ({plugged})."
            return status_str, True

        # Phone Call
        elif "call" in cmd:
            # Simple extraction for phone numbers or fallback
            words = cmd.split()
            phone_num = words[-1] if words[-1].isdigit() else "1234567890"
            self.phone.make_call(phone_num)
            return f"Initiating call to {phone_num}.", True

        # Send SMS
        elif "sms" in cmd or "message" in cmd:
            self.phone.send_sms("1234567890", "Hello from Yuki Assistant!")
            return "Sent simulated SMS message.", True

        # Weather query
        elif "weather" in cmd:
            # Mock or simple weather response
            return "The current weather is clear and pleasant at 25 degrees Celsius.", True

        # Help command
        elif "help" in cmd or "what can you do" in cmd:
            help_msg = (
                "I can tell you the time and date, check battery status, "
                "open WhatsApp or YouTube, simulate calls and SMS, or check weather."
            )
            return help_msg, True

        # Default fallback
        else:
            return f"I heard '{text}', but I don't have a command configured for that yet. Type 'help' to see what I can do.", True
