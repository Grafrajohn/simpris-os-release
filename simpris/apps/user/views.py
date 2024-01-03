from django.shortcuts import render, redirect, get_object_or_404
import logging
from ...models.db_views import VwSelectUserIndexSidebar, VUserAssigned, VUserDetail, VwSelectUserDetailSidebar, \
        VUserGroupDetail, VMyOrganisations, VUserCurrentProjects, VOrganisationProjectUsers
from ...library.user_context import UserContextFull
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.forms.utils import ErrorList

logger = logging.getLogger(__name__)


class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(label='oldpassword',min_length=8,max_length=128)
    newpassword = forms.CharField(label='newpassword',min_length=8,max_length=128)
    newpassword_confirm = forms.CharField(label='newpassword_confirm',min_length=8,max_length=128)


@login_required
def userlist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('user list : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}
    return render(request, "simpris/user/userlist.html", context_dict)


@login_required
def activity(request):
    user_context = UserContextFull(request)
    logger.info(str.format('user activity : {0}' .format(user_context.id)))

    user_activity = VwSelectUserIndexSidebar.objects.all().filter(Q(userid=user_context.id) | Q(userid='') | Q()).distinct()
    context_dict = {'sidebar': user_activity,'usercontext': user_context}
    return render(request, "simpris/user/activity.html", context_dict)


@login_required
@permission_required('simpris.add_users','/project/home/')
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('user create : {0}' .format(user_context.id)))

    organisations = VMyOrganisations.objects.values('organisationid', 'organisationname').filter(Q(clientid=user_context.clientID))\
        .order_by('organisationname').distinct()

    context_dict = {'organisations': organisations, 'usercontext': user_context}

    return render(request, "simpris/user/create.html", context_dict)


@login_required
def detail(request, user_id):
    user_context = UserContextFull(request)
    logger.info(str.format('user detail : {0}' .format(user_context.id)))

    user_data = VUserDetail.objects.all().filter(Q(id=user_id) &
                                                  Q(clientid=user_context.clientID))
    roles = VUserGroupDetail.objects.all().filter(Q(userid=user_id))
    projects = VUserAssigned.objects.all().filter(Q(assignedto=user_id))

    context_dict = {'id': user_id, 'user_data': user_data, 'roles': roles, 'projects': projects, 'usercontext': user_context}

    return render(request, "simpris/user/detail.html", context_dict)


@login_required
@permission_required('simpris.change_users', '/user/list/')
def edit(request, user_id):
    user_context = UserContextFull(request)
    logger.info(str.format('user edit : {0}' .format(user_context.id)))

    user_data = VUserDetail.objects.all().filter(Q(id=user_id))
    organisations = VMyOrganisations.objects.values('organisationid', 'organisationname').filter(Q(clientid=user_context.clientID) &
                                                  Q(clientid=user_context.clientID)).order_by('organisationname').distinct()
    projects = VUserCurrentProjects.objects.all().filter(Q(userid=user_id))
    potentials = VOrganisationProjectUsers.objects.all().filter(Q(userid=user_id)).order_by('projectname')

    is_project_manager = False
    is_vip = False

    if User.objects.filter(pk=user_id, groups__name='client_project_manager').exists():
        is_project_manager = True

    if User.objects.filter(pk=user_id, groups__name='client_vip').exists():
        is_vip = True

    context_dict = {'id': user_id, 'users': user_data, 'organisations': organisations, 'projects': projects,
                    'potentials': potentials, 'is_project_manager': is_project_manager,
                    'is_vip': is_vip, 'usercontext': user_context}

    return render(request, "simpris/user/edit.html", context_dict)


@login_required
def history(request, user_id):
    user_context = UserContextFull(request)
    logger.info(str.format('user history : {0}' .format(user_context.id)))

    user_data = VwSelectUserDetailSidebar.objects.all().filter(Q(userid=user_id)) # &
                                                  # Q(clientid=user_context.clientID))
    # link_data = VActualProblemLinks.objects.all().filter(Q(problemid=prob_id))

    context_dict = {'id': user_id, 'user': user_data}

    return render(request, "simpris/user/history.html", context_dict)


@login_required
def password(request):
    user_context = UserContextFull(request)
    logger.info(str.format('user change password : {0}' .format(user_context.id)))
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['oldpassword']
            user = authenticate(username=user_context.username,password=old_password)
            if user is not None:
                if user.is_active:
                    new_password = form.cleaned_data['newpassword']
                    u = User.objects.get(username__exact=user_context.username)
                    u.set_password(new_password)
                    u.save()
                    messages.add_message(request, messages.SUCCESS, 'You have successfully updated your password.')
                    return redirect(settings.BASE_URL_DJ + "/user/profile")
                else:
                    errors = form._errors.setdefault("user",ErrorList())
                    errors.append(u'User is not active')
                    return render(request, 'simpris/user/password.html', { 'form': form, 'usercontext': user_context })
            else:
                errors = form._errors.setdefault("user",ErrorList())
                errors.append(u'User not found')
                return render(request, 'simpris/user/password.html', { 'form': form, 'usercontext': user_context })

        return render(request, "simpris/user/password.html", { 'form': form, 'usercontext': user_context })

    return render(request, "simpris/user/password.html", {'usercontext': user_context})


@login_required
def profile(request):
    user_context = UserContextFull(request)
    logger.info(str.format('user profile : {0}' .format(user_context.id)))

    user_id = user_context.id
    user_data = VUserDetail.objects.all().filter(Q(id=user_id) & Q(clientid=user_context.clientID))

    context_dict = {'id': user_id, 'users': user_data, 'usercontext': user_context}

    return render(request, "simpris/user/profile.html", context_dict)
