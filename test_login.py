import unittest

# Assume we have a simple dictionary with valid usernames and passwords for the test
valid_users = {
    'user1': 'password123',
    'user2': 'securepass456',
    'admin': 'adminpass789'
}

def login(username, password):
    # Check if the username exists and the password matches
    if username in valid_users and valid_users[username] == password:
        return True
    else:
        return False

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        """Test valid username and password"""
        self.assertTrue(login('user1', 'password123'))
        print("Test for valid login passed")

    def test_invalid_username(self):
        """Test invalid username"""
        self.assertFalse(login('invalid_user', 'password123'))
        print("Test for invalid username passed")

    def test_invalid_password(self):
        """Test invalid password"""
        self.assertFalse(login('user1', 'wrongpassword'))
        print("Test for invalid password passed")

    def test_empty_username(self):
        """Test empty username"""
        self.assertFalse(login('', 'password123'))
        print("Test for empty username passed")

    def test_empty_password(self):
        """Test empty password"""
        self.assertFalse(login('user1', ''))
        print("Test for empty password passed")

    def test_case_sensitive_login(self):
        """Test case sensitivity for username and password"""
        self.assertFalse(login('User1', 'password123'))  # Username case doesn't match
        self.assertFalse(login('user1', 'Password123'))  # Password case doesn't match
        print("Test for case sensitivity passed")

    def test_empty_username_and_password(self):
        """Test empty username and password"""
        self.assertFalse(login('', ''))
        print("Test for empty username and password passed")

