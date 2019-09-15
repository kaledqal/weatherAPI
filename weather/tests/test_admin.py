"""
    Module for testing admin features
"""


from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class AdminSiteTests(TestCase):
    """
    Test several admin features
    """

    def setUp(self):
        """A function that is run before every test in this class is run"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@GMAIL.COM",
            password="password123"
        )
        # helps login the user without us manually logging in the user
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@fake.com",
            password="password123",
            first_name="John",
            last_name="Doe"
        )

    def test_users_listed(self):
        """Tests that users are listed on our page"""
        url = reverse('admin:weather_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.first_name)
        self.assertContains(resp, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:weather_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """Tests that the create user page works"""
        url = reverse('admin:weather_user_add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
