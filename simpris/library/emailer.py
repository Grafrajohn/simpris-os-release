__author__ = 'Graham'

from django.core.mail import send_mail
from simpris.models.models import Users
from django.db.models import Q

def send_smtp_email(type, action, from_addr, user_id, mail_subject, mail_message):

     to_addr_string = get_email_address(user_id)
     to_addr = ('support@simpris.com', to_addr_string)

     send_mail(mail_subject, mail_message, from_addr, to_addr, fail_silently=False)

def get_email_address(user_id):

     users_queryset = Users.objects.get(id=user_id)
     return users_queryset.email
