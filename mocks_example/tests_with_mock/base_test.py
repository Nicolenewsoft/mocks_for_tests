import django
django.setup()

from ..models import User
from unittest import TestCase


class BaseAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='barrosnicole094@gmail.com',
        )