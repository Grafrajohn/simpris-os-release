import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view

from simpris.library.user_context import UserContextFull
from ...models.models import Error

logger = logging.getLogger(__name__)


# @api_view(['POST'])
# def logerror(request):
#     user_context = UserContextFull(request)
#     error_message = request.POST.get('str_error')
#     module = request.POST.get('module')
#     error_detail = request.POST.get('str_error_detail')
#     Error_new = Error(clientid=user_context.clientID, organisationid=user_context.organisationID, userid=user_context.id,
#                       description=error_message,
#                       error_message=error_message, error_detail=error_detail)
#
#     logger.error(str.format('JS error in module {0}: User: {1} >>  {2} >> {3}' .format(module, user_context.id, error_message, error_detail)))
#
#     return Response("OK")
