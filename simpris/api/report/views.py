from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from simpris.api.project.serializers import UserSerializer, GroupSerializer, VMyCriticalWorkSerializer, \
    VClientsSerializer, VProjectsSerializer, UserProjectSerializer
from simpris.models.db_views import VMyCriticalWork, VMyOrganisations, VMyProjects
from simpris.models.models import Project, Userproject, Organisation
from simpris.library.user_context import UserContextFull
from simpris.library.response_object import ResponseObject
from simpris.library import emailer
from rest_framework.decorators import api_view
from django.conf import settings
import json
# from django.db.models import Q

import logging
import time

logger = logging.getLogger(__name__)


# class APIReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project


# class APIUserProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Userproject


# @api_view(['GET'])
# def datatable(request, report_id):
#     user_context = UserContextFull(request)
#     logger.info(str.format('problem insert : {0}' .format(user_context.id)))

    # if report_id == "vipsum":
    #     $queryString = "call sr_report_vip(";
    # elif report_id == "overproj":
    #     $queryString = "call sr_report_overdue_projects(";
    # elif report_id == "myproj":
    #     $queryString = "call sr_report_my_overdue_projects(";
    # elif report_id == "mytask":
    #     $queryString = "call sr_report_my_overdue_tasks_proj(";
    # elif report_id == "mytaskcom":
    #     $queryString = "call sr_report_my_tasks_complete(";
    # elif report_id == "overtaskproj":
    #     $queryString = "call sr_report_overdue_tasks_proj(";
    # elif report_id == "myovertaskproj":
    #     $queryString = "call sr_report_overdue_tasks_proj(";

    # queryset = VMyCriticalWork.objects.all().filter(assignedto=user_context.id)
    # serializer_class = VMyCriticalWorkSerializer(queryset, many=True)
    #
    # return Response(serializer_class.data)


# @api_view(['GET'])
# def pie(request):
#     user_context = UserContextFull(request)
#     logger.info(str.format('problem insert : {0}'.format(user_context.id)))
#
#     queryset = VMyOrganisations.objects.all().filter(userid=user_context.id,
#                                                      deleteddate=None).order_by('organisationname')
#     serializer_class = VClientsSerializer(queryset, many=True)
#
#     return Response(serializer_class.data)

