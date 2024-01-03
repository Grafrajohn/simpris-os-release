from django.shortcuts import render
import logging
from ...library.user_context import UserContextFull
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def calendartab(request):
    logger.info('calendar index')

    logger.info('calendar index auth OK')
    userContext = UserContextFull(request)
    logger.info(userContext)

    context_dict = {'usercontext': userContext}
    return render(request, "simpris/time/calendar.html", context_dict)
