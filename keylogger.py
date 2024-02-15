from exceptions import NotRunningError


class KeyLogger:
    """Represent a KeyLogger."""

    def __init__(self):
        self.__keys = []
        self.keys_count = 0
        self.__is_running = False

    def start(self):
        """Starts the key logging process."""
        self.__is_running = True

    def stop(self):
        """Stops the key logging process."""
        self.__is_running = True

    @property
    def is_running(self):
        return self.__is_running

    @property
    def keys(self):
        return self.__keys

    def increase_keys_count(self):
        self.keys_count += 1
        print(self.keys_count)

    def reset_keys_count(self):
        self.keys_count = 0

    def log_keys(self, key):
        """Handles keys logging."""
        if self.__is_running:
            self.__keys.append(key)
        else:
            raise NotRunningError(
                "KeyLogger is not running. Make sure to start() the key logger."
            )
