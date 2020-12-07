from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test creating a user with email is successful."""
        email = "test@testprovider.com"
        password = "testpass"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self,):
        """Test if email for a user is normalized.
        """
        email = 'test@TESTPROVIDEr.com'
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user without email
        raises error.
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='testpass')

    def test_create_new_superuser(self):
        """Test creating a new superuser.
        """
        user = get_user_model().objects.create_super_user(email='testadmin@test.com',
                                                    password='testpass123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
