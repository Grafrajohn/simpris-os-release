from django.shortcuts import render
from ...models.db_views import VwSelectOrganisationIndexSidebar, VOrganisations, VOrganisationUsers, \
    VwSelectOrganisationDetailSidebar, VOrganisationPotentialUsers
from ...library.user_context import UserContextFull
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

import logging
logger = logging.getLogger(__name__)
# Create your views here.


@login_required
def list(request):
    logger.info('organisation index')

    userContext = UserContextFull(request)
    organisation_activity = VwSelectOrganisationIndexSidebar.objects.all().filter(Q(userid=userContext.id) | Q(userid='')).distinct()
    context_dict = {'usercontext': userContext}
    return render(request, "simpris/organisation/list.html", context_dict)


@login_required
def activity(request):
    logger.info('organisation activity')

    userContext = UserContextFull(request)
    organisation_activity = VwSelectOrganisationIndexSidebar.objects.all().filter(Q(userid=userContext.id) | Q(userid='')).distinct()
    context_dict = {'sidebar': organisation_activity,'usercontext': userContext}
    return render(request, "simpris/organisation/activity.html", context_dict)


@login_required        
def detail(request,org_id):
    logger.info('client detail')
    
    userContext = UserContextFull(request)    
    organisation_detail = VOrganisations.objects.all().filter(organisationid=org_id,clientid=userContext.clientID)[:1]
    organisation_activity = VwSelectOrganisationDetailSidebar.objects.all().filter(organisationid=org_id)
    context_dict = {'sidebar': organisation_activity,'detail': organisation_detail,'id': org_id}
    
    return render(request,'simpris/organisation/detail.html',context_dict)


@login_required
@permission_required('simpris.add_organisation', '/project/home/')
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('organisation create : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request,'simpris/organisation/create.html',context_dict)


@login_required
@permission_required('simpris.change_organisation', '/project/home/')
def edit(request,org_id):
    logger.info('client edit')

    userContext = UserContextFull(request)
    organisation_detail = VOrganisations.objects.all().filter(organisationid=org_id,clientid=userContext.clientID)[:1]
    organisation_activity = VwSelectOrganisationDetailSidebar.objects.all().filter(organisationid=org_id)
    context_dict = {'sidebar': organisation_activity,'organisation': organisation_detail,'id': org_id, 'usercontext': userContext}

    return render(request,'simpris/organisation/edit.html',context_dict)


@login_required
def history(request,org_id):
    logger.info('client history')

    userContext = UserContextFull(request)
    organisation_detail = VOrganisations.objects.all().filter(organisationid=org_id,clientid=userContext.clientID)[:1]
    organisation_activity = VwSelectOrganisationDetailSidebar.objects.all().filter(organisationid=org_id)
    context_dict = {'sidebar': organisation_activity,'detail': organisation_detail,'id': org_id}

    return render(request,'simpris/organisation/history.html',context_dict)


@login_required
def users(request,org_id):
    logger.info('organisation users')

    user_context = UserContextFull(request)
    organisation_users = VOrganisationUsers.objects.all().filter(organisationid=org_id,clientid=user_context.clientID)
    potential_users = VOrganisationPotentialUsers.objects.all().filter(clientid=user_context.clientID)

    context_dict = {'users': organisation_users,'potentials': potential_users,'id': org_id, 'user_id': user_context.id}

    return render(request,'simpris/organisation/users.html',context_dict)
