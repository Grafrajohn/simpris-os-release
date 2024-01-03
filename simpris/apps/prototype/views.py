from django.shortcuts import render
from ...library.user_context import UserContextFull
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

import logging
logger = logging.getLogger(__name__)
# Create your views here.


@login_required
def vue(request):
    user_context = UserContextFull(request)
    logger.info(str.format('dashboard : {0}' .format(user_context.id)))

    userContext = UserContextFull(request)
    logger.info(userContext)
    context_dict = {'usercontext': userContext}
    return render(request, "prototype/vue.html", context_dict)