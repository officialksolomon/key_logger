import types
import unittest

from utils import check_variables_exist


class TestUtils(unittest.TestCase):
    def test_check_variable_exist_is_true(self):
        # Arrange
        module = types.SimpleNamespace(
            EMAIL_HOST="smtp.privateemail.com",
            EMAIL_PORT=465,     
            EMAIL_USER="user@example.com",
            EMAIL_PASSWORD="password",
        )
        # Act
        variable_list = ["EMAIL_HOST", "EMAIL_PORT", "EMAIL_USER", "EMAIL_PASSWORD"]
        result = check_variables_exist(module, variable_list)
        # Assert
        self.assertIs(result, True)

    def test_check_variable_exist_is_false(self):
        # Arrange
        module = types.SimpleNamespace(
            EMAIL_HOST="smtp.example.com",
            EMAIL_PORT=465,
            EMAIL_USER="user@example.com",
        )
        # Act
        variable_list = ["EMAIL_HOST", "EMAIL_PORT", "EMAIL_USER", "EMAIL_PASSWORD"]
        result = check_variables_exist(module, variable_list)
        # Assert
        self.assertIs(result, False)


if __name__ == "__main__":
    unittest.main()
