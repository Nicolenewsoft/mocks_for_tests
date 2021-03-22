import smtplib
from .models import User
from mocks_example.utils import send_email

def send_email_to_recipient(user_id):
    user = User.objects.get(id=user_id)
    try:

        return send_email(
            user.email,
            subject="Aviso importante",
            body="Aqui vai a mensagem")

    except smtplib.SMTPException:
        return "error"