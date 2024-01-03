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
def dashboard(request):
    user_context = UserContextFull(request)
    logger.info(str.format('dashboard : {0}' .format(user_context.id)))

    userContext = UserContextFull(request)
    logger.info(userContext)
    organisation_activity = VwSelectOrganisationIndexSidebar.objects.all().filter(Q(userid=userContext.id) | Q(userid='')).distinct()
    context_dict = {'sidebar': organisation_activity,'usercontext': userContext}
    return render(request, "simpris/dashboard/dashboard.html", context_dict)
