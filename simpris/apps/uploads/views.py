__author__ = 'Graham'

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from ...models.models import Document
from ...apps.uploads.forms import DocumentForm
from ...library.user_context import UserContextFull
import time
import logging

logger = logging.getLogger(__name__)


def upload(request):
    user_context = UserContextFull(request)
    logger.info(str.format('document upload : {0}' .format(user_context.id)))

    # Handle file upload
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            upload_source = data['hidItemType']
            item_id = data['hidItemID']
            document_file_name = request.FILES['frmUserFile'].name
            document_parts = document_file_name.split('.')
            file_extension = document_parts[-1]
            document_parent_id = item_id
            if upload_source == 'tsk':
                document_type_id = 3
                document_name = 'tk' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '_thumb.' + file_extension
                document_file_name = 'tk' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '.' + file_extension
                destination_folder = 'task'
            elif upload_source == 'prj':
                document_type_id = 1
                document_name = 'pr' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '_thumb.' + file_extension
                document_file_name = 'pr' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '.' + file_extension
                destination_folder = 'project'
            elif upload_source == 'cmt':
                document_type_id = 2
                document_name = 'cm' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '_thumb.' + file_extension
                document_file_name = 'cm' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '.' + file_extension
                destination_folder = 'comment'
                comment_parent_id = data['hidParentID']
            elif upload_source == 'prb':
                document_type_id = 4
                document_name = 'pb' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '_thumb.' + file_extension
                document_file_name = 'pb' + '_' + str(item_id) + '-' + str(user_context.id) + '-' + str(time.strftime('%Y%m%d%H%M%S')) + '.' + file_extension
                destination_folder = 'problem'
            document_title = request.FILES['frmUserFile'].name
            created_date = time.strftime('%Y-%m-%d %H:%M:%S')
            created_by = user_context.id
            handle_uploaded_file(request.FILES['frmUserFile'],document_file_name,destination_folder)
            newdoc = Document(documenttypeid=document_type_id, documentparentid=document_parent_id, documentname=document_name,
                              documentfilename=document_file_name, documenttitle = document_title, createddate=created_date,
                              createdby=created_by)
            newdoc.save()

            # Redirect to the document list after POST
            if upload_source == 'tsk':
                return HttpResponseRedirect('/task/detail/' + item_id + '/')
            elif upload_source == 'prj':
                return HttpResponseRedirect('/project/detail/' + item_id + '/')
            elif upload_source == 'cmt':
                return HttpResponseRedirect('/task/detail/' + comment_parent_id + '/')
            elif upload_source == 'prb':
                return HttpResponseRedirect('/problem/detail/' + item_id + '/')
            else:
                return HttpResponseRedirect(request,'simpris/error.html')
        else:
            logger.error('invalid upload: ' )
            return render(request,'simpris/error.html')
    else:
        form = DocumentForm() # A empty, unbound form


def handle_uploaded_file(f, filename, destination_folder):
    with open(settings.UPLOAD_DIR + destination_folder + '/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
