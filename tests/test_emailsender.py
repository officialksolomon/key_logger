import unittest
from unittest.mock import patch

from emailsender import EmailSender
from exceptions import NoOrIncompleteConfigException
from keylogger import KeyLogger


@patch("emailsender.config")
@patch("emailsender.smtplib.SMTP_SSL")
class TestEmailSender(unittest.TestCase):
    def setUp(self) -> None:
        self.keylogger = KeyLogger()
        self.email_sender = EmailSender()

    def test_connection_success(self, mock_smtp_ssl, mock_config):
        # Arrange
        mock_config.EMAIL_HOST = "smtp.example.com"
        mock_config.EMAIL_PORT = 465
        mock_config.EMAIL_USER = "user@example.com"
        mock_config.EMAIL_PASSWORD = "password"
        # Act
        self.email_sender.connect()
        # Assert
        mock_smtp_ssl.assert_called_once_with(
            mock_config.EMAIL_HOST, mock_config.EMAIL_PORT
        )

    def test_connect_missing_config(self, mock_smtp_ssl, mock_config):
        # Arange
        mock_config.EMAIL_PORT = None
        mock_config.EMAIL_USER = None
        mock_config.EMAIL_PASSWORD = None
        # Act
        # Act & Assertions
        with self.assertRaises(NoOrIncompleteConfigException):
            self.email_sender.connect()

    def test_compose_message(self, mock_smtp_ssl, mock_config):
        msg_body = "Test Body"
        wrong_msg = "wrong message"
        message = self.email_sender.compose_message(
            "sender@email.com", "receiver@email.com", "Test Subject", msg_body
        )
        self.assertIn(msg_body, message)
        self.assertNotIn(wrong_msg, message)

    def test_send_mail(self, mock_smtp_ssl, mock_config):
        # Arrange
        mock_config.FROM_EMAIL = "sender@gmail.com"
        # mock_smtp_ssl.return_value.sendmail.return_value = {}
        self.email_sender.server = mock_smtp_ssl

        # Act
        message = self.email_sender.compose_message(
            "sender@email.com", "receiver@email.com", "Test Subject", "Test Body"
        )
        self.email_sender.send_mail(
            "receiver@email.com", "Test Subject", "Test Body", "sender@email.com"
        )
        # Assert
        mock_smtp_ssl.sendmail.assert_called_once_with(
            "sender@email.com",
            "receiver@email.com",
            message,
        )


if __name__ == "__main__":
    unittest.main()
