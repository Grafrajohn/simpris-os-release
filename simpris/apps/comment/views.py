# Create your views here.
import logging
import time

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ...models.models import Comment
from ...library.user_context import UserContextFull
from ..comment.forms import CommentForm

logger = logging.getLogger(__name__)


@login_required
def insert(request, parent_id):
    user_context = UserContextFull(request)
    logger.info(str.format('comment insert : {0}' .format(user_context.id)))

    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    form = CommentForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        entity_id = data['hidParentID']
        parent_type = data['hidParentType']
        entity = None
        page = None
        if parent_type == '4':
            entity = 'problem'
            page = 'log'
        elif parent_type == '3':
            entity = 'task'
            page = 'detail'
        elif parent_type == '2':
            entity = 'project'
            page = 'detail'
        comment_text = data['frmTextComment']
        comment_new = Comment(parentid=entity_id, parenttypeid=parent_type, commenttypeid=3,
                  commenttext=comment_text, createddate=created_date, createdby=created_by)
        comment_new.save()
        messages.success(request, 'Entry successfully created')
        return redirect('/' + entity + '/' + page + '/' + entity_id)
    else:
        messages.error(request, 'Entry not created')
        #return redirect('/task/detail/' + parent_id)
        return render(request)   #, "simpris/problem/log.html", context_dict)
