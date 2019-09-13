from django.test import TestCase
from django.contrib.auth import get_user_model # at some point you may want to change the user model


class ModelTests(TestCase):
    """Tests models"""

    def test_create_user_with_email_successful(self):
        """Tests creating a new user with an email is successful"""
        email = "fakeemail@fake.com"
        password = "fakepassword123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password  # password will be encripted
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests that the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password='testPassword123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new users with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@GMAIL.COM',
            password="test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
