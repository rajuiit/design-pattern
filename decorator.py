class Notifier:
    def send(self, message):
        print(f"Sending basic notification: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        self.notifier.send(message)

class EmailNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Sending email notification: {message}")

class SMSNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Sending SMS notification: {message}")
 
if __name__ == "__main__":
    # Basic notifier
    notifier = Notifier()

    # Add email functionality
    email_notifier = EmailNotifier(notifier)

    # Add SMS functionality on top of email
    sms_notifier = SMSNotifier(email_notifier)

    # Send notification using the full decorator chain
    sms_notifier.send("Hello, World!")
