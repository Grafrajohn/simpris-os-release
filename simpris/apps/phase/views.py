# python imports
import logging, time, datetime

# django imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# simpris imports
from ...models.models import Phase
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def phaselist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('phase list : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/phase/phaselist.html", context_dict)


@login_required
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('phase create : {0}' .format(user_context.id)))

    context_dict = {'mode': "create", 'usercontext': user_context}

    return render(request, "simpris/phase/create.html", context_dict)


@login_required
def detail(request, phase_id):
    user_context = UserContextFull(request)
    logger.info(str.format('phase create : {0}' .format(user_context.id)))

    phase_data = Phase.objects.all().filter(Q(clientid=user_context.clientID) &
                                            Q(phaseid=phase_id) & Q(deleteddate__isnull=True))

    context_dict = {'phase': phase_data, 'id': phase_id, 'usercontext': user_context}

    return render(request, "simpris/phase/detail.html", context_dict)


@login_required
def edit(request, phase_id):
    user_context = UserContextFull(request)
    logger.info(str.format('phase create : {0}' .format(user_context.id)))

    phase_data = Phase.objects.all().filter(Q(clientid=user_context.clientID) & Q(phaseid=phase_id) &
                                            Q(deleteddate__isnull=True))

    context_dict = {'mode': "edit", 'phase': phase_data, 'id': phase_id, 'usercontext': user_context}

    return render(request, "simpris/phase/edit.html", context_dict)
