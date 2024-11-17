"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Model testing class with test cases."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with email."""
        email = "test@example.com"
        password = "pass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
            Test user email normalized. 
            (Normalizing before hashing ensures that the generated UID2 value will always be the same, so that the data can be matched.)
        """

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Creating a superuser."""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test123',
        )

        self.assertTrue(user.is_superuser) # is_superuser this coming from the permissionsmixin
        self.assertTrue(user.is_staff)
