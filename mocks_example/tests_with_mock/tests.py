from .base_test import BaseAPITestCase
from mocks_example.views import send_email_to_recipient
import smtplib
from unittest.mock import patch


class TestMocks(BaseAPITestCase):

    @patch('mocks_example.utils.send_email')
    def test_send_email(self, mock_send_email):
        # Aqui testamos a send_email_to_recipient, mockando o send_email
        mock_send_email.return_value = 1
        self.assertTrue(send_email_to_recipient(self.user), 1)
        # assert send_email_to_recipient(self.user) == 1

    @patch('mocks_example.utils.send_email')
    def test_send_email_on_failure(self, mock_send_email):
        mock_send_email.sideeffect = smtplib.SMTPException
        self.assertEqual(send_email_to_recipient (self.user), "error")