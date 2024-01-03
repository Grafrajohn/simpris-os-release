from django.shortcuts import render
import logging
from ...models.db_views import VAccountDetail
from ...library.user_context import UserContextFull
from django.contrib.auth.decorators import login_required, permission_required

logger = logging.getLogger(__name__)


@login_required
@permission_required('simpris.change_account', '/project/home/')
def home(request):
    user_context = UserContextFull(request)
    logger.info(str.format('admin index : {0}' .format(user_context.id)))

    account_data = VAccountDetail.objects.all().filter(clientid=user_context.clientID)

    context_dict = {'accounts': account_data, 'usercontext': user_context}

    return render(request, "simpris/administration/home.html", context_dict)
