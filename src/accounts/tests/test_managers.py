from django.test import TestCase
from django.contrib.auth import get_user_model


class ManagersTest(TestCase):

    def test_create_user_Without_phone(self):
        with self.assertRaises(TypeError):
            user = get_user_model().objects.create_user()

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            phone=9123456788
        )
        self.assertFalse(user.is_staff, user.is_superuser)
        self.assertFalse(user.is_active_email)
        self.assertIsInstance(user, get_user_model())
        self.assertEqual(user.user_level, "normal")

    def test_create_super_user(self):
        super_user = get_user_model().objects.create_superuser(
            phone=9123456789
        )
        self.assertTrue(super_user.is_staff, super_user.is_superuser)
        self.assertTrue(super_user.is_active_email)
        self.assertEqual(super_user.user_level, "super_user")
        self.assertIsInstance(super_user, get_user_model())

    def test_create_super_user_with_change_attribute(self):
        with self.assertRaises(ValueError):
            super_user = get_user_model().objects.create_superuser(
                phone=9123456787,
                is_staff=False
            )

        with self.assertRaises(ValueError):
            super_user = get_user_model().objects.create_superuser(
                phone=9123456787,
                is_superuser=False
            )

