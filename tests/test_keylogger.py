import unittest

from exceptions import NotRunningError
from keylogger import KeyLogger


class TestKeyLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.keylogger = KeyLogger()

    def test_start(self):
        # Arrange
        keylogger = KeyLogger()
        # Act
        keylogger.stop()
        # Assert
        assert keylogger.is_running is True

    def test_stop(self):
        # Arrange
        keylogger = KeyLogger()
        # Act
        keylogger.stop()
        # Assert
        assert self.keylogger.is_running is False

    def test_log_keys(self):
        # Arrange
        keylogger = KeyLogger()
        # Act

        keylogger.start()
        keylogger.log_keys("a")
        # Assert
        assert len(keylogger.keys) > 0

    def test_log_keys_exception(self):
        # Arrange
        keylogger = KeyLogger()
        # Act & Assert
        with self.assertRaises(NotRunningError):
            keylogger.log_keys("a")

    def test_increase_keys_count(self):
        # Arrange
        keylogger = KeyLogger()
        keylogger.start()
        keylogger.increase_keys_count()
        # Act & Assert
        self.assertEqual(keylogger.keys_count, 1)

    def test_reset_keys_count(self):
        # Arrange
        keylogger = KeyLogger()
        keylogger.start()
        keylogger.reset_keys_count()
        # Act & Assert
        self.assertEqual(keylogger.keys_count, 0)


if __name__ == "__main__":
    unittest.main()
