import time, logging, pytz
from datetime import datetime

from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view

from simpris.api.problem.serializers import VProblemsSerializer
from simpris.models.db_views import VMyProblems
from simpris.models.models import Organisation, Problem, Problemlink
from simpris.library.user_context import UserContextFull

logger = logging.getLogger(__name__)


class APIProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('clientid','organisationid','problemtypeid','problemsubtypeid','problemheader','problemdescription',
                  'noofpeopleaffected','assignedto','scope','problemstatusid','problempriorityid', 'queueid')


@api_view(['GET'])
def problems(request, prob_range):
    
    user_context = UserContextFull(request)
    logger.info(str.format('problem list : {0}' .format(user_context.id)))

    if prob_range == 'all':
        queryset = VMyProblems.objects.all().filter(Q(clientid=user_context.clientID)).order_by('problempriority')
    elif prob_range == 'my':
        queryset = VMyProblems.objects.all().filter(Q(clientid=user_context.clientID) & (Q(assignedto=user_context.id) |
                                                Q(createdby=user_context.id))).order_by('problempriority')
    else:
        # queue selected
        queryset = VMyProblems.objects.all().filter(Q(clientid=user_context.clientID) & (Q(queueid=prob_range))).order_by('problempriority')
    serializer_class = VProblemsSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):
    user_context = UserContextFull(request)
    logger.info(str.format('problem insert : {0}' .format(user_context.id)))

    problem_id = 0
    organisation_id = request.POST.get('frmOrganisation')
    problem_header = request.POST.get('frmProblemHeader')
    problem_description = request.POST.get('frmProblemDescription')
    problem_type = request.POST.get('frmProblemType')
    problem_subtype = request.POST.get('frmProblemSubType')
    problem_no_affected = request.POST.get('frmNoofPeopleAffected')
    problem_scope = request.POST.get('frmProblemScope')
    problem_status = request.POST.get('frmProblemStatus')
    problem_priority = request.POST.get('frmProblemPriority')
    problem_queue = request.POST.get('frmProblemQueue') or None
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    organisation = Organisation.objects.get(organisationid=organisation_id)

    problem_serializer = APIProblemSerializer(data={'problemid': problem_id,
                                                    'clientid': user_context.clientID,
                                                    'organisationid': organisation_id,
                                                    'problemtypeid': problem_type,
                                                    'problemsubtypeid': problem_subtype,
                                                    'problemheader': problem_header,
                                                    'problemdescription': problem_description,
                                                    'noofpeopleaffected': problem_no_affected,
                                                    'scope': problem_scope,
                                                    'problemstatusid': problem_status,
                                                    'problempriorityid': problem_priority,
                                                    'queueid': problem_queue,
                                                    'assignedto': 0, 'createdby': created_by,
                                                    'createddate': created_date})

    if problem_serializer.is_valid():

        problem_new = Problem(clientid=user_context.clientID, organisationid=organisation,
                      problemtypeid=problem_type, problemdescription=problem_description,
                      problemheader=problem_header, problemsubtypeid=problem_subtype,
                      noofpeopleaffected=problem_no_affected, scope=problem_scope,
                      problemstatusid=problem_status, problempriorityid=problem_priority,
                      queueid=problem_queue,
                      createdby=created_by, createddate=created_date)
        problem_new.save(force_insert=True)

        problem_object = Problem.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('problemid')

        messages.success(request._request, 'Problem successfully created')

        response = {'problem_id': problem_object.problemid}

    else:
        messages.error(request._request, 'Incorrect problem data')
        raise serializers.ValidationError(problem_serializer.errors)

    return Response(response)


@api_view(['GET','POST'])
def delete(request,prob_id):
    user_context = UserContextFull(request)
    logger.info(str.format('problem delete : {0}' .format(user_context.id)))

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_problem'):

        deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
        deleted_by = user_context.id

        prob = Problem.objects.get(problemid=prob_id, clientid=user_context.clientID)
        prob.deletedby = deleted_by
        prob.deleteddate = deleted_date
        prob.save()

        messages.success(request._request, 'Problem successfully deleted')

        response = {'problem_id': prob.problemid}

    else:
        raise serializers.ValidationError("User is not authorised to delete problem")

    return Response(response)


@api_view(['POST'])
def update(request):
    user_context = UserContextFull(request)
    logger.info(str.format('problem update : {0}' .format(user_context.id)))

    problem_id = request.POST.get('hidProblemID')
    organisation_id = request.POST.get('hidOrganisationID')
    problem_header = request.POST.get('frmProblemHeader')
    problem_description = request.POST.get('frmProblemDescription')
    problem_type = request.POST.get('frmProblemType')
    problem_subtype = request.POST.get('frmProblemSubType')
    problem_no_affected = request.POST.get('frmNoofPeopleAffected')
    problem_scope = request.POST.get('frmProblemScope')
    problem_status = request.POST.get('frmProblemStatus')
    problem_priority = request.POST.get('frmProblemPriority')
    problem_queue = request.POST.get('frmProblemQueue') or None
    problem_assignee = request.POST.get('frmProblemAssignee') or 0
    problem_link = request.POST.get('frmProblemLink') or 0
    project_link = request.POST.get('frmProjectLink') or 0
    problem_link_exists = request.POST.get('hidProblemLink') or 0
    project_link_exists = request.POST.get('hidProjectLink') or 0
    updated_date = timezone.now()#time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    problem_serializer = APIProblemSerializer(data={
                                                    'clientid': user_context.clientID,
                                                    'organisationid': organisation_id,
                                                    'problemtypeid': problem_type,
                                                    'problemsubtypeid': problem_subtype,
                                                    'problemheader': problem_header,
                                                    'problemdescription': problem_description,
                                                    'noofpeopleaffected': problem_no_affected,
                                                    'scope': problem_scope,
                                                    'problemstatusid': problem_status,
                                                    'problempriorityid': problem_priority,
                                                    'queueid': problem_queue,
                                                    'assignedto': problem_assignee,
                                                    'updatedby': updated_by,
                                                    'updateddate': updated_date})

    if problem_serializer.is_valid():

        prob = Problem.objects.get(problemid=problem_id)
        prob.problemtypeid = problem_type
        prob.problemsubtypeid = problem_subtype
        prob.problemheader = problem_header
        prob.problemdescription = problem_description
        prob.noofpeopleaffected = problem_no_affected
        prob.scope = problem_scope
        prob.problemstatusid = problem_status
        prob.problempriorityid = problem_priority
        prob.queueid = problem_queue
        if problem_assignee != '':
            prob.assignedto = problem_assignee
        prob.updatedby = updated_by
        prob.updateddate = updated_date
        prob.save()

        # if the problem is linked to a project
        if not str(project_link) == str(project_link_exists):
            if project_link_exists == "0":
                insert_problem_link(problem_id, project_link, 1, user_context.id)
            else:
                update_problem_link(problem_id, project_link, 1, project_link_exists, user_context.id)

        # if the problem is linked to a problem
        if not str(problem_link) == str(problem_link_exists):
            if problem_link_exists == "0":
                insert_problem_link(problem_id, problem_link, 2, user_context.id)
            else:
                update_problem_link(problem_id, problem_link, 2, problem_link_exists, user_context.id)

        messages.success(request._request, 'Problem successfully updated')

        response = {'problem_id': prob.problemid}

    else:

        raise serializers.ValidationError(problem_serializer.errors)

    return Response(response)


# insert a new problem link
def insert_problem_link(problemid, problemlinkid, problemlinktype, user_id):
    problem_link_new = Problemlink(problemid=problemid, problemlinkid=problemlinkid, problemlinktype=problemlinktype,
                                   createddate = time.strftime('%Y-%m-%d %H:%M:%S'), createdby = user_id)
    problem_link_new.save()


# delete old link and insert new one. At present only one project and problem link per problem.
def update_problem_link(problemid, problemlinkid, problemlinktype, problem_link_exists, user_id):
        # do the delete
        for probs in Problemlink.objects.filter(problemid=problemid,problemlinktype=problemlinktype):
            probs.deleteddate=time.strftime('%Y-%m-%d %H:%M:%S')
            probs.deletedby=user_id
            probs.save()

        # do the insert
        if problemlinkid != '':
            insert_problem_link(problemid, problemlinkid, problemlinktype, user_id)
