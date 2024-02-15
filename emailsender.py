import smtplib
from asyncio.windows_events import NULL

import config
from exceptions import NoOrIncompleteConfigException
from Utils import check_variables_exist


class EmailSender:
    def __init__(self) -> None:
        self.server: smtplib.SMTP_SSL = NULL

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.server is not None:
            self.server.quit()

    def connect(self):
        if check_variables_exist(
            config, ["EMAIL_HOST", "EMAIL_PORT", "EMAIL_USER", "EMAIL_PASSWORD"]
        ):
            server = smtplib.SMTP_SSL(config.EMAIL_HOST, config.EMAIL_PORT)
            server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
            self.server = server
        else:
            raise NoOrIncompleteConfigException(
                "Required configs for EmailSender connection missing missing."
            )

    def compose_message(self, sender_email, receiver_email, subject, message):
        sender_email = sender_email
        recipient_email = receiver_email
        subject = subject
        body = message
        message = f"From: {sender_email or config.FROM_EMAIL}\nTo: {recipient_email}\nSubject: {subject}\n\n{body}"
        return message

    def send_mail(
        self, receiver_email: str, subject, message, sender_email: str = None
    ):
        message = self.compose_message(sender_email, receiver_email, subject, message)
        self.server.sendmail(sender_email or config.FROM_EMAIL, receiver_email, message)
