import time, datetime, math, logging, pytz

from django.contrib.auth import hashers
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view

from simpris.api.user.serializers import UserSerializer
from simpris.models.db_views import VMyUsers
from simpris.models.models import Organisation, AuthUser, Users, Userorganisation, \
    UserPayrate, UserTaxrate, UserAttributes
from simpris.library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# serializer for Djano users
class APIAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'is_superuser', 'is_staff', 'is_active', 'last_login',
                  'date_joined')


# serializer for old ion_auth users
class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password', 'first_name', 'last_name', 'company', 'phone', 'created_on', 'active', 'last_login')


# serializer for pay rate users
class APIPayRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayrate
        fields = ('defaultrate','payrateid','effectivedate')


# serializer for tax rate users
class APITaxRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTaxrate
        fields = ('taxrateid','effectivedate', 'defaultrate')


# serializer for user attributes
class APIAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttributes
        fields = ('vip','countryid','mobilephoneno','faxno','photo')


@api_view(['GET'])
def users(request):
    
    user_context = UserContextFull(request)
    logger.info(str.format('user list : {0}' .format(user_context.id)))

    #is_client_admin = User.objects.filter(pk=request.user.id, groups__name='client_admin').exists()

    # user = User.objects.get(id=request.user.id)
    # if user.has_perm('add_users'):
    #     queryset = VMyUsers.objects.all().filter(clientid=user_context.clientID, userid=user_context.id).distinct().order_by('organisationname','last_name')
    # else:
    queryset = VMyUsers.objects.all().filter(clientid=user_context.clientID, userid=user_context.id).order_by('organisationname','last_name')
    serializer_class = UserSerializer(queryset,many=True)   

    return Response(serializer_class.data)


@api_view(['POST'])
def detail(request):

    user_context = UserContextFull(request)
    logger.info(str.format('user detail : {0}' .format(user_context.id)))

    return Response()


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('user create : {0}' .format(user_context.id)))

    user_id = 0
    user_name = request.POST.get('frmUsername')
    active = 1
    organisation_id = request.POST.get('frmOrganisation')
    first_name = request.POST.get('frmFirstName')
    last_name = request.POST.get('frmLastName')
    email = request.POST.get('frmEmail')
    phone = request.POST.get('frmPhone')
    password = request.POST.get('frmPassword')
    password_confirm = request.POST.get('frmPasswordConfirm')
    created_date = timezone.now()
    current_time = timezone.now()
    created_on = current_time.timestamp()
    created_modulus = math.floor(created_on)
    created_by = user_context.id

    organisation = Organisation.objects.get(organisationid=organisation_id)

    auth_user_serializer = APIAuthUserSerializer(data={'first_name': first_name, 'last_name': last_name,
                        'is_superuser': 0, 'username': user_name, 'password': password,
                        'email': email, 'is_staff': 0, 'is_active': active, 'last_login': created_date,
                        'date_joined': created_date})

    user_serializer = APIUserSerializer(data={'clientid': user_context.clientID, 'first_name': first_name, 'last_name': last_name, 'username': user_name,
                        'password': password, 'email': email, 'phone': phone, 'created_on': created_modulus,
                        'active': active, 'company': organisation_id, 'last_login': created_modulus,
                        'clientid': user_context.clientID})

    if auth_user_serializer.is_valid() and user_serializer.is_valid() and password == password_confirm:

        password_hash = hashers.make_password(password)
        auth_user_new = AuthUser(password=password_hash, is_superuser=0, username=user_name, first_name=first_name,
                    last_name=last_name, email=email, is_staff=0, is_active=1, last_login=created_date,
                    date_joined=created_date)
        auth_user_new.save()

        auth_user_object = AuthUser.objects.get(username=user_name)

        user_new = Users(id=auth_user_object.id, password=password, username=user_name, first_name=first_name, last_name=last_name,
                    email=email, created_on=created_modulus, active=1, company=organisation_id, phone=phone,
                    last_login=created_modulus, clientid=user_context.clientID)
        user_new.save()

        user_object = Users.objects.get(username=user_name)

        user_organisation = Userorganisation(userid=user_object.id, organisationid=organisation, createddate=created_date, createdby=created_by)
        user_organisation.save()

        # create standard group membership
        user = User.objects.get(id=auth_user_object.id)
        group = Group.objects.get(id=7)
        user.groups.add(group)

        messages.success(request._request, 'User successfully created. Remember to grant the user acces to projects.')

        response = {'user_id': user_object.id}

    else:

        temp1 = auth_user_serializer.is_valid()
        temp2 = user_serializer.is_valid()
        raise serializers.ValidationError(auth_user_serializer.errors)

    return Response(response)


@api_view(['GET'])
def delete(request, user_id):

    user_context = UserContextFull(request)
    logger.info(str.format('user delete : {0}' .format(user_context.id)))

    if user_id == str(user_context.id):
        # messages.error(request._request, 'You cannot delete yourself')
        raise serializers.ValidationError('You cannot delete yourself')
        # response = {'user_id': user_id}
        # return Response(response)

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_users'):
        auth_user_update = AuthUser.objects.get(id=user_id)
        auth_user_update.is_active = 0
        auth_user_update.save(update_fields=['is_active'])

        user_update = Users.objects.get(id=user_id)
        user_update.active = 0
        user_update.save(update_fields=['active'])

        response = {'user_id': user_id}

    else:
        raise serializers.ValidationError('You are not authorised to deactivate users')

    return Response(response)


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('user update : {0}' .format(user_context.id)))

    user_id = request.POST.get('hidUserID')
    user_name = request.POST.get('frmUsername')
    active = 1
    organisation_id = request.POST.get('frmOrganisation')
    first_name = request.POST.get('frmFirstName')
    last_name = request.POST.get('frmLastName')
    email = request.POST.get('frmEmail')
    phone = request.POST.get('frmPhone')
    project_manager = request.POST.get('frmProjectMngr') or '0'
    project_stakeholder = 0
    vip = request.POST.get('frmVIP') or 'n'
    pay_rate = request.POST.get('frmPayRate') or 0
    tax_rate = request.POST.get('frmTaxRate') or 0
    created_date = time.strftime('%Y-%m-%d %H:%M:%S',tz=get_current_timezone())
    current_time = timezone.now()
    created_on = current_time.timestamp()
    created_modulus = math.floor(created_on)
    created_by = user_context.id

    # organisation = Organisation.objects.get(organisationid=organisation_id)

    auth_user_serializer = APIAuthUserSerializer(data={'first_name': first_name, 'last_name': last_name,
                        'is_superuser': 0, 'username': 'TESTONLY', 'password': 'TESTONLY',
                        'email': email, 'is_staff': 0, 'is_active': active, 'last_login': created_date,
                        'date_joined': created_date})

    user_serializer = APIUserSerializer(data={'first_name': first_name, 'last_name': last_name, 'username': 'TESTONLY',
                          'email': email, 'phone': phone, 'created_on': created_modulus, 'password': 'TESTONLY',
                          'active': active, 'company': organisation_id, 'last_login': created_modulus})

    payrate_serializer = APIPayRateSerializer(data={'defaultrate': pay_rate, 'payrateid': 0, 'effectivedate': created_date})

    taxrate_serializer = APITaxRateSerializer(data={'taxrateid': 0, 'defaultrate': tax_rate, 'effectivedate': created_date})

    attribute_serializer = APIAttributeSerializer(data={'vip': vip, 'countryid': None, 'mobilephoneno': 'None',
                                                      'faxno': 'None', 'photo': 'None'})

    if auth_user_serializer.is_valid() and user_serializer.is_valid() \
            and payrate_serializer.is_valid() and taxrate_serializer.is_valid() and attribute_serializer.is_valid():# and password == password_confirm:

        auth_user_update = AuthUser.objects.get(username=user_name)
        auth_user_update.first_name = first_name
        auth_user_update.last_name = last_name
        auth_user_update.email = email
        auth_user_update.save(update_fields=['first_name','last_name','email'])

        user_update = Users.objects.get(id=user_id)
        user_update.first_name = first_name
        user_update.last_name = last_name
        user_update.email = email
        user_update.phone = phone
        user_update.company = organisation_id
        user_update.save(update_fields=['first_name','last_name','email','phone','company'])

        user_payrate_update = UserPayrate(userid=user_id,payrateid=0,effectivedate=created_date,defaultrate=pay_rate,
                                          createddate=created_date,createdby=user_context.id)
        user_payrate_update.save()

        user_taxrate_update = UserTaxrate(userid=user_id,taxrateid=0,effectivedate=created_date,defaultrate=tax_rate,
                                          createddate=created_date,createdby=user_context.id)
        user_taxrate_update.save()

        user_attribute_update = UserAttributes(userid=user_id,vip=vip,countryid=0,mobilephoneno='None',
                                          faxno='None',photo='None')
        user_attribute_update.save()

        # if project manager create project manager membership
        if project_manager != '0':
            user = User.objects.get(id=user_id)
            group = Group.objects.get(id=3)
            user.groups.add(group)
        else:
            user = User.objects.get(id=user_id)
            group = Group.objects.get(id=3)
            group.user_set.remove(user)

        messages.success(request._request, 'User successfully updated.')

        response = {'user_id': user_id}

    else:
        if not auth_user_serializer.is_valid():
            raise serializers.ValidationError(auth_user_serializer.errors)
        elif not user_serializer.is_valid():
            raise serializers.ValidationError(user_serializer.errors)
        elif not payrate_serializer.is_valid():
            raise serializers.ValidationError(payrate_serializer.errors)
        elif not taxrate_serializer.is_valid():
            raise serializers.ValidationError(taxrate_serializer.errors)
        elif not attribute_serializer.is_valid():
            raise serializers.ValidationError(attribute_serializer.errors)

    return Response(response)


@api_view(['POST'])
def profile(request):

    user_context = UserContextFull(request)
    logger.info(str.format('user profile : {0}' .format(user_context.id)))

    email = request.POST.get('frmEmail')
    phone = request.POST.get('frmPhone')

    current_time = timezone.now()
    created_on = current_time.timestamp()
    created_modulus = math.floor(created_on)
    created_date = time.strftime('%Y-%m-%d %H:%M:%S',tz=get_current_timezone())

    auth_user_serializer = APIAuthUserSerializer(data={'first_name': 'validate', 'last_name': 'validate',
                        'is_superuser': 0, 'username': 'TESTONLY', 'password': 'TESTONLY',
                        'email': email, 'is_staff': 0, 'is_active': 1, 'last_login': created_date,
                        'date_joined': created_date})

    if auth_user_serializer.is_valid():
        auth_user_update = AuthUser.objects.get(username=user_context.username)
        auth_user_update.email = email
        auth_user_update.save(update_fields=['email'])
    else:
        raise serializers.ValidationError(auth_user_serializer.errors)

    user_serializer = APIUserSerializer(data={'first_name': 'validate', 'last_name': 'validate', 'username': 'TESTONLY',
                          'email': email, 'phone': phone, 'created_on': created_modulus, 'password': 'TESTONLY',
                          'active': 1, 'company': 0, 'last_login': created_modulus})

    if user_serializer.is_valid():
        user_update = Users.objects.get(id=user_context.id)
        user_update.email = email
        user_update.phone = phone
        user_update.save(update_fields=['email','phone'])
    else:
        raise serializers.ValidationError(user_serializer.errors)

    messages.success(request._request, 'Profile successfully updated.')

    return Response()


@api_view(['POST'])
def password(request):

    user_context = UserContextFull(request)
    logger.info(str.format('user password : {0}' .format(user_context.id)))

    return Response()


@api_view(['GET'])
def projectusers(request, task_id):
    user_context = UserContextFull(request)
    logger.info(str.format('project users : {0}'.format(user_context.id)))

    queryset = VMyUsers.objects.all().filter(clientid=user_context.clientID, userid=user_context.id).order_by(
        'organisationname', 'last_name')
    serializer_class = UserSerializer(queryset, many=True)

    return Response(serializer_class.data)