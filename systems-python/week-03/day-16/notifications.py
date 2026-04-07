class Notifier:
    def send(self, message):
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        message = f"[{timestamp}] {message}"
        print(f"Sending: {message}")


class EmailNotifier:
    def __init__(self):
        self.notifier = Notifier()

    def send(self, message):
        self.notifier.send(f"EMAIL: {message}")


class SMSNotifier:
    def __init__(self):
        self.notifier = Notifier()

    def send(self, message):
        self.notifier.send(f"SMS: {message}")


email = EmailNotifier()
sms = SMSNotifier()

email.send("Your appointment is confirmed")
sms.send("Your appointment is confirmed")