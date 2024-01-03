import logging, datetime, time, uuid, math, urllib, json, pytz

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django import forms
from django.db import IntegrityError
from django.forms.utils import ErrorList
from django.contrib import messages
from django.utils import timezone

from ...models.models import Account, Client, Organisation, Users
from ...library import emailer
from ...library.user_context import UserContextFull

logger = logging.getLogger(__name__)


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30, initial="")
    last_name = forms.CharField(label='Last name', max_length=30, initial="")
    company = forms.CharField(label='Company name', max_length=100, initial="")
    email = forms.EmailField(label='Email', max_length=75, initial="")
    phone = forms.CharField(label='Phone', max_length=20, required=False, initial="")
    username = forms.CharField(label='Username', min_length=8, max_length=30, initial="")
    password = forms.CharField(label='Password', min_length=8, max_length=128, initial="")
    password_confirm = forms.CharField(label='Password confirm', min_length=8, max_length=128, initial="")
    tcs = forms.BooleanField(label='Terms and conditions',
                             error_messages={'required': 'You must accept the terms and conditions'})


def new(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        # recaptcha v3 code

        # get the token submitted in the form
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(payload).encode()
        req = urllib.request.Request(url, data=data)

        # verify the token submitted with the form is valid
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        # result will be a dict containing 'success' and 'action'.
        # it is important to verify both

        if (not result['success']):  # make sure action matches the one from your template
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return render(request, 'simpris/register/new.html', {'form': form})

        # end of recaptcha v3

        if form.is_valid(): # and (settings.BASE_URL_DJ == 'http://127.0.0.1:8000'):
            user_name = form.cleaned_data['username']
            company = form.cleaned_data['company']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password != password_confirm:
                errors = form._errors.setdefault("password", ErrorList())
                errors.append(u'Passwords do not match')
                return render(request, 'simpris/register/new.html', {'form': form})
            created_date = time.strftime('%Y-%m-%d %H:%M:%S')
            account_uuid = uuid.uuid1()
            current_time = timezone.now()
            created_on = current_time.timestamp()
            created_modulus = math.floor(created_on)
            last_login = created_date

            # create auth user
            try:
                auth_user_new = User.objects.create_user(user_name, email, password)
                auth_user_new.first_name = first_name
                auth_user_new.last_name = last_name
                auth_user_new.is_superuser = 0
                auth_user_new.is_staff = 0
                auth_user_new.is_active = 1
                auth_user_new.date_joined = created_date
                auth_user_new.last_login = created_date
                auth_user_new.save()
            except IntegrityError as e:
                return render(request, 'simpris/register/new.html', {'form': form, 'error': e.__cause__})

            # create account
            account_new = Account(accountname=company, authenticationid=account_uuid, authenticationid2=email,
                                  authenticationid3='Free Account',
                                  membershiptypeid='2', email=email, firstname=first_name, lastname=last_name,
                                  phone=phone, membershiprenewaldate=created_date, createddate=created_date,
                                  createdby=auth_user_new.id)
            account_new.save()
            account_object = Account.objects.filter(createdby=auth_user_new.id).latest('accountid')
            account_id = account_object.accountid

            # create client
            client_new = Client(accountid=account_object, userid=auth_user_new.id, clientname=company,
                                address1='address1', address2='address2',
                                address3='address3', city='city', region='region', country='country',
                                postcode='postcode',
                                createddate=created_date, createdby=auth_user_new.id)
            client_new.save()
            client_object = Client.objects.get(accountid=account_id)
            client_id = client_object.clientid

            # create organisation
            organisation_new = Organisation(clientid=client_object, organisationname=company,
                                            createddate=created_date, createdby=auth_user_new.id)
            organisation_new.save()
            organisation_object = Organisation.objects.get(clientid=client_id, createdby=auth_user_new.id)
            organisation_id = organisation_object.organisationid

            # create user
            user_new = Users(id=auth_user_new.id, clientid=client_id, ip_address=0, username=user_name,
                             password='PASSWORD', salt='VINEGAR',
                             email=email, activation_code='',
                             forgotten_password_code='', forgotten_password_time=0, remember_code='',
                             created_on=created_modulus,
                             last_login=created_modulus, active=1, first_name=first_name, last_name=last_name,
                             company=organisation_id, phone=phone)
            user_new.save()

            # create client admin group membership
            user = User.objects.get(id=auth_user_new.id)
            group = Group.objects.get(id=1)
            user.groups.add(group)

            # create client account holder group membership
            group = Group.objects.get(id=6)
            user.groups.add(group)

            # email to new registrant
            subject = "Simpris: New account " + company + " has been created"
            url = str(settings.BASE_URL_DJ + '/auth/logon/')
            message = "Congratulations on setting up your new Simpris account. You can start using the system by clicking on this link: " \
                      + url + " and using your user name and password. Do not forget to look at our help pages for guidance on how to use the system."
            email_from = settings.EMAIL_FROM
            emailer_simpris = emailer
            emailer_simpris.send_smtp_email("re", "i", email_from, auth_user_new.id, subject, message)

            # log the user in
            username = user_name
            password = password
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(settings.BASE_URL_DJ + "/register/welcome")
                else:
                    return render(request, 'simpris/auth/login.html')
            else:
                return render(request, 'simpris/auth/login.html')
        else:
            return render(request, 'simpris/register/new.html', {'form': form})
    else:
        regForm = RegisterForm()
        return render(request, 'simpris/register/new.html', {'form': regForm})


@login_required()
def thankyou(request):
    logger.info('subscription thankyou')

    logger.info('subscription thankyou auth OK')
    return render(request, "simpris/register/thankyou.html")


@login_required
def welcome(request):
    logger.info('register welcome')

    logger.info('register welcome auth OK')
    user_context = UserContextFull(request)
    now = timezone.now()
    user_context_sub_id = "{}-{}-{}{}{}".format(user_context.clientID, user_context.id, now.year, now.month, now.day)
    context_dict = {'client': user_context_sub_id, 'usercontext': user_context,
                    'subscription_url': settings.BASE_URL_SUBSCRIPTION}
    return render(request, "simpris/register/welcome.html", context_dict)
