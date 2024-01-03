import logging
import time
import datetime
import pytz

from django.contrib.auth import logout, login, authenticate

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed

from ...library import slog


@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
def authenticate(request):

    if request.user is not None:
        if request.user.is_active:
            # get token for user
            token = Token.objects.get(user=request.user)
            # if no token create one
            if token is None:
                token = Token.objects.create(user=request.user)
            else:
                # check if token expired
                three_months = datetime.timedelta(3 * 365 / 12)
                expiry_date = pytz.UTC.localize(datetime.datetime.today() - three_months)
                # if token expired delete and create new one
                if token.created < expiry_date:
                    token.delete()
                    token = Token.objects.create(user=request.user)
                    # return token
                    return Response({'token': token.key})
                else:
                    return Response({'token': token.key})
        else:
            raise exceptions.AuthenticationFailed('User inactive or deleted')
    else:
        raise exceptions.AuthenticationFailed('Invalid token')


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def create(request, format=None):

    # check if token exists for user

    # if no token then issue one
    token = Token.objects.create(user=request.user)

    # check if token created more than 3 months ago

    # if token > 3 months old reissue
    token = Token.objects.create(user=request.user)

    return Response(token.key)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def token(request, format=None):

    token = Token.objects.get(user=request.user)

    return Response({'token': token.key})

