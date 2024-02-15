import unittest
from unittest.mock import Mock

from keylogger import KeyLogger
from keystroke_handler import KeyStrokeHandler


class TestKeyStrokeHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.key = "a"
        self.keylogger_mock = Mock(spec=KeyLogger)
        self.keystroke_handler = KeyStrokeHandler(self.keylogger_mock)

    def test_on_press(self):
        # Arrange
        self.keylogger_mock.log_keys.return_value = None
        # Act
        result = self.keystroke_handler.on_press(self.key)
        # Assertions
        assert result is None
        self.keylogger_mock.log_keys.called_once_with(self.key)

    def test_on_press_exception(self):
        # Arrange
        self.keylogger_mock.log_keys.side_effect = AttributeError
        # Act
        with self.assertRaises(AttributeError):
            self.keystroke_handler.on_press(self.key)
        # Assertion
        self.assertEqual(self.keylogger_mock.log_keys.call_count, 2)

    def test_on_release(self):
        # Act
        result = self.keystroke_handler.on_release(self.key)
        # Assertion
        assert result is False


if __name__ == "__main__":
    unittest.main()
