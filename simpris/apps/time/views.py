import logging, time, datetime, pytz

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ...models.db_views import VTimeDetail, VwSelectTimeIndexSidebar, VTimeType, VMyOrgTasks, VMyTimesheet
from ...library.user_context import UserContextFull

logger = logging.getLogger(__name__)


@login_required
def activity(request):
    user_context = UserContextFull(request)
    logger.info(str.format('time activity : {0}' .format(user_context.id)))

    type_data = VTimeType.objects.all().filter(Q(clientid=0))
    task_data = VMyOrgTasks.objects.all().filter(Q(userid=user_context.id) & Q(deleteddate__isnull=True)).order_by('taskname')

    context_dict = {'time_types': type_data, 'tasks': task_data, 'usercontext': user_context}

    return render(request, "simpris/time/activity.html", context_dict)


@login_required
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('time create : {0}' .format(user_context.id)))

    type_data = VTimeType.objects.all().filter(Q(clientid=0))
    task_data = VMyOrgTasks.objects.all().filter(Q(userid=user_context.id) & Q(deleteddate__isnull=True)).order_by('taskname')

    context_dict = {'time_types': type_data, 'tasks': task_data, 'usercontext': user_context}

    return render(request, "simpris/time/create.html", context_dict)


@login_required
def detail(request, time_id):
    user_context = UserContextFull(request)
    logger.info(str.format('time detail : {0}' .format(user_context.id)))

    time_data = VTimeDetail.objects.all().filter(Q(timeid=time_id))

    context_dict = {'id': time_id, 'times': time_data}

    return render(request, "simpris/time/detail.html", context_dict)


@login_required
def edit(request, time_id):
    user_context = UserContextFull(request)
    logger.info(str.format('time detail : {0}' .format(user_context.id)))

    time_data = VTimeDetail.objects.all().filter(Q(timeid=time_id))
    type_data = VTimeType.objects.all().filter(Q(clientid=0))

    context_dict = {'id': time_id, 'times': time_data, 'time_types': type_data}

    return render(request, "simpris/time/edit.html", context_dict)


@login_required
def timegrid(request):
    logger.info('timegrid index')
        
    logger.info('timegrid index auth OK')
    userContext = UserContextFull(request)
    logger.info(userContext)
    context_dict = {'usercontext':userContext}
    return render(request, "simpris/time/timegrid.html", context_dict)


@login_required
def timesheet(request):
    user_context = UserContextFull(request)
    logger.info(str.format('timesheet : {0}' .format(user_context.id)))

    if request.POST.get('frmDatePicker'):
        time_start_init = request.POST.get('frmDatePicker')
        time_start = pytz.utc.localize(datetime.datetime.strptime(request.POST.get('frmDatePicker') + ' 00:00:00','%Y/%m/%d %H:%M:%S'))
        #time_start = time_start.replace('/','-')
    else:
        time_start_init = time.strftime('%Y/%m/%d')
        time_start = timezone.localtime()
    if request.POST.get('frmDatePicker2'):
        time_end_init = request.POST.get('frmDatePicker2')
        time_end = pytz.utc.localize(datetime.datetime.strptime(request.POST.get('frmDatePicker2') + ' 23:59:59','%Y/%m/%d %H:%M:%S'))
        #time_end = time_end.replace('/','-')
    else:
        time_now = timezone.localtime() + datetime.timedelta(days=7)
        time_end = timezone.localtime()
        time_end_init = time_now.strftime('%Y/%m/%d')

    time_start_print = time_start  #[0:10]
    time_end_print = time_end#[0:10]

    timesheet_data = VMyTimesheet.objects.filter(Q(userid=user_context.id) & Q(timeday__range=[time_start, time_end]))
    total = 0
    for time_item in timesheet_data:
        if time_item.taskdescription != None:
            total += time_item.hours

    context_dict = {'time_start': time_start_init, 'time_end': time_end_init, 'timesheets': timesheet_data,
                    'time_start_print': time_start_print, 'time_end_print': time_end_print, 'total': total,
                    'usercontext': user_context}

    return render(request, "simpris/time/timesheet.html", context_dict)


@login_required
def timeprint(request, time_start, time_end):
    user_context = UserContextFull(request)
    logger.info(str.format('timesheet : {0}' .format(user_context.id)))

    time_start_print = time_start[0:10]
    time_end_print = time_end[0:10]

    timesheet_data = VMyTimesheet.objects.filter(Q(userid=user_context.id) & Q(timeday__range=[time_start, time_end]))
    total = 0
    for time_item in timesheet_data:
        if time_item.taskdescription != None:
            total += time_item.hours

    context_dict = {'time_start': time_start, 'time_end': time_end, 'timesheets': timesheet_data, 'total': total}

    return render(request, "simpris/time/timeprint.html", context_dict)


@login_required
def timelist(request):
    logger.info('timelist index')
        
    logger.info('time timelist auth OK')
    userContext = UserContextFull(request)
    logger.info(userContext)
    time_activity = VwSelectTimeIndexSidebar.objects.all().filter(Q(userid=userContext.id) | Q(userid=''))
    context_dict = {'sidebar': time_activity,'usercontext':userContext}
    return render(request, "simpris/time/timelist.html", context_dict)