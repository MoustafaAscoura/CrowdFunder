from django.utils import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
    
account_activation_token = TokenGenerator()

def send_verification_email(request,user):
    
    mail_subject = 'Activate your CrowdFunder account.'
    message = render_to_string('registration/acc_active_email.html', {
        'user': user,
        'domain':request.META['HTTP_HOST'],
        'uid':force_str(urlsafe_base64_encode(force_bytes(user.pk))),
        'token':account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.send()