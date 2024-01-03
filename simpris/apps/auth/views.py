from django.shortcuts import render
from simpris.library.user_context import UserContextFull
from django import forms
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect
import logging
import time
from django.conf import settings
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
# from settings import DEFAULT_FROM_EMAIL
from django.views.generic import *
# from utils.forms.reset_password_form import PasswordResetRequestForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q

from ...models.models import Useractivity
from ...library import slog

logger = logging.getLogger(__name__)


class LoginForm(forms.Form):
    username = forms.CharField(label='username',max_length=30)
    password = forms.CharField(label='password',max_length=40)


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label="Email Or Username", max_length=40)


class ResetPasswordRequestView(FormView):
    template_name = "account/test_template.html"    #code for template is given below the view's code
    success_url = '/account/login'
    form_class = PasswordResetRequestForm


# Create your views here.
@login_required
def logoff(request):
    user_context = UserContextFull(request)
    logger.info(str.format('auth logoff : {0}' .format(user_context.id)))
        
    if hasattr(request, 'user'):
        logger.info('logoff - request has user')
        if request.user.is_authenticated:
            logger.info('auth logoff OK')
            slog.log_activity(request.user.id, "logoff", "logoff", "auth", "logoff", user_context.clientID)
            logout(request)
            request.session.flush()
        else:
            logger.warning('auth logoff FAIL')
    return redirect(settings.BASE_URL_DJ + "/auth/logon")


def logon(request):
    if request and request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password'] 
            user = authenticate(username=username,password=password)
            if user is not None: 
                if user.is_active:
                    login(request,user)
                    slog.log_activity(request.user.id or 0,"login","login OK","auth","logon",0)
                    return redirect(settings.BASE_URL_DJ + "/project/home")
                else:
                    errors = form._errors.setdefault("user",ErrorList())
                    errors.append(u'User is not active')
                    return render(request, 'simpris/auth/logon.html')
            else:
                errors = form._errors.setdefault("password",ErrorList())
                errors.append(u'Login credentials incorrect')
                return render(request, 'simpris/auth/logon.html', { 'form': form })
        else:

            return render(request, 'simpris/auth/logon.html', { 'form': form })
    elif request:
        form = {}
        return render(request, 'simpris/auth/logon.html', { 'form': form})
    else:
        return render()


def forgot_password(request):
    user_context = UserContextFull(request)
    logger.info(str.format('auth logoff : {0}'.format(user_context.id)))

    if hasattr(request, 'user'):
        logger.info('logoff - request has user')
        if request.user.is_authenticated():
            logger.info('auth logoff OK')
            logout(request)
            request.session.flush()
        else:
            logger.warning('auth logoff FAIL')
    return redirect(settings.BASE_URL_DJ + "/auth/logon")


@staticmethod
def validate_email_address(email):
    '''
    This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
    '''


    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def post(self, request, *args, **kwargs):
    '''
    A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).
    '''


    form = self.form_class(request.POST)
    if form.is_valid():
        data = form.cleaned_data["email_or_username"]
    if self.validate_email_address(data) is True:  # uses the method written above
        '''
        If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
        '''
        associated_users = User.objects.filter(Q(email=data) | Q(username=data))
        if associated_users.exists():
            for user in associated_users:
                c = {
                    'email': user.email,
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'your site',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                subject_template_name = 'registration/password_reset_subject.txt'
                # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                email_template_name = 'registration/password_reset_email.html'
                # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                subject = loader.render_to_string(subject_template_name, c)
                # Email subject *must not* contain newlines
                subject = ''.join(subject.splitlines())
                email = loader.render_to_string(email_template_name, c)
                send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
            result = self.form_valid(form)
            messages.success(request,
                             'An email has been sent to ' + data + ". Please check its inbox to continue reseting password.")
            return result
        result = self.form_invalid(form)
        messages.error(request, 'No user is associated with this email address')
        return result
    else:
        '''
        If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
        '''
        associated_users = User.objects.filter(username=data)
        if associated_users.exists():
            for user in associated_users:
                c = {
                    'email': user.email,
                    'domain': 'example.com',  # or your domain
                    'site_name': 'example',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                subject_template_name = 'registration/password_reset_subject.txt'
                email_template_name = 'registration/password_reset_email.html'
                subject = loader.render_to_string(subject_template_name, c)
                # Email subject *must not* contain newlines
                subject = ''.join(subject.splitlines())
                email = loader.render_to_string(email_template_name, c)
                send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
            result = self.form_valid(form)
            messages.success(request,
                             'Email has been sent to ' + data + "'s email address. Please check its inbox to continue reseting password.")
            return result
        result = self.form_invalid(form)
        messages.error(request, 'This username does not exist in the system.')
        return result
    messages.error(request, 'Invalid Input')
    return self.form_invalid(form)
