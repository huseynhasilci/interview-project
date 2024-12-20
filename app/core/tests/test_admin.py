"""
Testing admin features for django.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Test for admin."""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@exmaple.com',
            password='testpass123',
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@exmaple.com',
            password='testpass123',
            name='Test user'
        )

    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_users_modify(self):
        """Test editing users informations."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_superuser_create_casual_user(self):
        """Test creating new user."""
        url = reverse('admin:core_user_add')

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
