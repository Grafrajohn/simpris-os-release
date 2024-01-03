import logging, time

from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view

from simpris.models.models import Board
from simpris.library.user_context import UserContextFull


logger = logging.getLogger(__name__)


class APIBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('userid', 'itemid', 'itemtype', 'columnno', 'itemorder')


@api_view(['POST'])
def insert(request):
    # This method is for inserts into the kanban table for the first time. All other moves use the move
    # function

    user_context = UserContextFull(request)
    logger.info(str.format('kanban move : {0}' .format(user_context.id)))

    column_id = request.POST.get('column_id')
    item_type = request.POST.get('item_type') or 1
    item_id = request.POST.get('item_id') # for inserts this is the task or problem id!!
    source_column = request.POST.get('source_column')

    updatedDate = time.strftime('%Y-%m-%d %H:%M:%S')
    updatedBy = user_context.id

    boardSerializer = APIBoardSerializer(data={'id': 0, 'userid': user_context.id, 'itemid': item_id,
                                             'itemtype': item_type, 'columnno': column_id, 'itemorder': 0})

    if boardSerializer.is_valid():

        bd_new = Board(userid=user_context.id, itemid=item_id, itemtype=item_type, columnno=column_id, itemorder=0)
        bd_new.save()

        response = {'itemid': item_id}

    else:

        response = {'responseText': boardSerializer.errors}

    return Response(response)


@api_view(['POST'])
def move(request):

    user_context = UserContextFull(request)
    logger.info(str.format('kanban move : {0}' .format(user_context.id)))

    column_id = request.POST.get('column_id')
    item_type = request.POST.get('item_type') or 1
    item_id = request.POST.get('item_id') # note this is not the task or problem id!!
    source_column = request.POST.get('source_column')

    updatedDate = time.strftime('%Y-%m-%d %H:%M:%S')
    updatedBy = user_context.id

    boardSerializer = APIBoardSerializer(data={'id': 0, 'userid': user_context.id, 'itemid': item_id,
                                             'itemtype': item_type, 'columnno': column_id, 'itemorder': 0})

    if boardSerializer.is_valid():

        bd = Board.objects.get(id=item_id)
        bd.columnno = column_id
        bd.itemorder = 0
        bd.save()

        response = {'itemid': item_id}

    else:

        response = {'responseText': boardSerializer.errors}

    return Response(response)
