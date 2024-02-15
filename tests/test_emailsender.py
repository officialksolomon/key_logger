import unittest

from keylogger import KeyLogger


class TestEmailSender(unittest.TestCase):
    def setUp(self) -> None:
        self.keylogger = KeyLogger()

    def test_connect(self):
        pass


if __name__ == "__main__":
    unittest.main()
