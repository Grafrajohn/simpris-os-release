from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from ...models.db_views import VSearch
from django.db.models import Q
from ...library.user_context import UserContextFull

import logging
logger = logging.getLogger(__name__)

class SearchForm(forms.Form):
    frmSearchText = forms.CharField(label='frmSearchText',max_length=100)


# Create your views here.
@login_required
def index(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project detail : {0}' .format(user_context.id)))
        
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            searchterm = form.cleaned_data['frmSearchText']
            search_results = VSearch.objects.all().filter((Q(projectname__contains=searchterm) | Q(projectdescription__contains=searchterm) |
                                                           Q(tasklistname__contains=searchterm) | Q(tasklistdescription__contains=searchterm) |
                                                           Q(taskname__contains=searchterm) | Q(taskdescription__contains=searchterm)) &
                                                          Q(clientid=user_context.clientID) & Q(userid=user_context.id)).distinct()
            search_result_json = []
            for result in search_results:
                search_result_json.append(
                    {'projectid': result.projectid,
                     'projectname': result.projectname or ' ',
                     'tasklistname': result.tasklistname or ' ',
                     'taskdescription': result.taskdescription or ' '}
                )
            context_dict = {'searchResult': search_result_json}                   
            return render(request, "simpris/search/results.html", context_dict)                        
  
    return render(request,'simpris/search/results.html')             