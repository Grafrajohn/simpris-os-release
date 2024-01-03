from django.shortcuts import render
from ...library.user_context import UserContextFull
import logging, time, json
from django.contrib.auth.decorators import login_required
from ...models.db_views import VProjectDetail, VProjectganttJq, VProjectPie, VChartProjectBehindTasks, \
        VChartTasksByStatus
from django.db.models import Q
from django.core import serializers
from django.db import connection, transaction
import decimal

logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('report list : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/report/list.html",context_dict)


@login_required
def project(request):
    user_context = UserContextFull(request)
    logger.info(str.format('report project : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/report/project.html",context_dict)


@login_required
def metric(request, report_id):
    user_context = UserContextFull(request)
    logger.info(str.format('report metric : {0}' .format(user_context.id)))

    metric_data = None
    report = None

    if report_id == "projprob":
        report = "No of problems per project"
        metric_data = __get_metric_data('simpricity.sr_metric_problems_project', user_context.id)
    elif report_id == "myprobperproj":
        report = "No of problems on my projects"
        metric_data = __get_metric_data('simpricity.sr_metric_my_problems_project', user_context.id)
    elif report_id == "billcli":
        report = "Revenue invoiced per client"
        metric_data = __get_metric_data('simpricity.sr_metric_client_revenue', user_context.id)
    elif report_id == "mybilledrev":
        report = "Revenue invoiced for my clients"
        metric_data = __get_metric_data('simpricity.sr_metric_my_client_revenue', user_context.id)

    metric_json = json.dumps(metric_data, default=__decimal_default)

    context_dict = {'metric_data': metric_json, 'title': report, 'usercontext': user_context}

    return render(request, "simpris/report/metric.html",context_dict)


@login_required
def datatable(request, report_id):
    user_context = UserContextFull(request)
    logger.info(str.format('report datatable : {0}' .format(user_context.id)))

    report_data = None

    if report_id == "vipsum":
        report_title = "VIP summary"
        report_data = __get_datatable_data('simpricity.sr_report_vip', user_context.id)
    elif report_id == "overproj":
        report_title = "Overdue projects"
        report_data = __get_datatable_data('simpricity.sr_report_overdue_projects', user_context.id)
    elif report_id == "overtaskproj":
        report_title = "Overdue tasks by project"
        report_data = __get_datatable_data('simpricity.sr_report_overdue_tasks_proj', user_context.id)
    # elif report_id == "projprob":
    #     report_title = "Problems per project"
    #     report_data = __get_datatable_data('simpricity.sr_report_overdue_projects', user_context.id)
    elif report_id == "myoverproj":
        report_title = "My overdue projects"
        report_data = __get_datatable_data('simpricity.sr_report_my_overdue_projects', user_context.id)
    elif report_id == "myovertask":
        report_title = "My overdue tasks"
        report_data = __get_datatable_data('simpricity.sr_report_my_overdue_tasks_proj', user_context.id)
    elif report_id == "mytaskcom":
        report_title = "My tasks completed"
        report_data = __get_datatable_data('simpricity.sr_report_my_tasks_complete', user_context.id)
    elif report_id == "myovertaskproj":
        report_title = "My overdue tasks by project"
        report_data = __get_datatable_data('simpricity.sr_report_my_overdue_tasks_proj', user_context.id)
    else:
        report_title = "Report not found"

    json_data = json.dumps(report_data)

    context_dict = {'report': report_id, 'report_title': report_title, 'report_data': json_data, 'usercontext': user_context}

    return render(request, "simpris/report/detail.html",context_dict)


@login_required
def chart(request, chart_id, item_id):
    user_context = UserContextFull(request)
    logger.info(str.format('report chart : {0}' .format(user_context.id)))

    project_data = VProjectDetail.objects.all().filter(Q(projectid=item_id) & Q(userid=user_context.id))
    project_pie = VProjectPie.objects.all().filter(Q(projectid=item_id) & Q(deleteddate__isnull=True))
    behind_tasks = VChartProjectBehindTasks.objects.all().filter(Q(projectid=item_id) & Q(deleteddate__isnull=True))
    tasks_status = VChartTasksByStatus.objects.all().filter(Q(projectid=item_id) & Q(deleteddate__isnull=True))

    # serialize to JSON
    pie_json = serializers.serialize('json', project_pie)
    behind_json = serializers.serialize('json', behind_tasks)
    tasks_json = serializers.serialize('json', tasks_status)

    context_dict = {'project': project_data, 'pie_json': pie_json, 'behind_json': behind_json, 'tasks': tasks_json,
        'usercontext': user_context}

    return render(request, "simpris/report/chart.html",context_dict)


@login_required
def gantt(request):
    user_context = UserContextFull(request)
    logger.info(str.format('report gantt : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/project/gantt.html",context_dict)


@login_required
def gantt_jq(request, proj_id):
    user_context = UserContextFull(request)
    logger.info(str.format('report gantt jquery : {0}' .format(user_context.id)))

    project_data = VProjectganttJq.objects.all().filter(Q(projectid=proj_id) & Q(deleteddate__isnull=True))

    json_objects = serializers.serialize('json', project_data)

    project = VProjectDetail.objects.all().filter(Q(userid=user_context.id) & Q(projectid=proj_id) &
                                                  Q(clientid=user_context.clientID))

    context_dict = {'projects': project, 'times_formatted': json_objects, 'usercontext': user_context}
    return render(request, "simpris/report/gantt_jq.html", context_dict)


@login_required
def generic(request, report_id):
    user_context = UserContextFull(request)
    logger.info(str.format('report gantt jquery : {0}' .format(user_context.id)))

    if report_id == 'proj':
        chart_title = 'Project charts'
        chart_type = 'bar'
        chart_data = __get_generic_data('project','importance',19)
    elif report_id == 'task':
        chart_title = 'Task charts'
        chart_type = 'bar'
        chart_data = __get_generic_data('task','taskpriorityid',4)
    elif report_id == 'prob':
        chart_title = 'Problem charts'
        chart_type = 'bar'
        chart_data = __get_generic_data('problem','problempriorityid',12)
    elif report_id == 'user':
        chart_title = 'User charts'
        chart_type = 'bar'
        chart_data = __get_generic_data('users','problempriorityid',12)
    elif report_id == 'time':
        chart_title = 'Time charts'
        chart_type = 'bar'
        chart_data = __get_generic_data('time','timetypeid',13)
    elif report_id == 'inv':
        chart_title = 'Invoice charts'
        chart_type = 'bar'
        chart_data = __get_generic_data('invoice','statusid',18)
    else:
        chart_title = 'Generic'
        chart_type = 'bar'
        chart_data = ''

    chart_json = json.dumps(chart_data)

    context_dict = {'title': chart_title, 'type': chart_type, 'chart_json': chart_json, 'usercontext': user_context}
    return render(request, "simpris/report/generic.html", context_dict)


def __get_datatable_data(stored_routine, user_id):

    cur = connection.cursor()
    try:
        cur.callproc(stored_routine, [user_id])
        report_data_fetched = cur.fetchall()

    finally:
        cur.close()

    report_data = report_data_fetched

    return report_data


def __get_metric_data(stored_routine, user_id):

    cur = connection.cursor()
    try:
        cur.callproc(stored_routine, [user_id])
        report_data_fetched = cur.fetchall()

    finally:
        cur.close()

    report_data = report_data_fetched

    return report_data


def __get_generic_data(data_table, lookup_item, lookup_id):

    cur = connection.cursor()
    try:
        cur.callproc('sr_generic_chart', [data_table, lookup_item, lookup_id])
        report_data_fetched = cur.fetchall()

    finally:
        cur.close()

    report_data = report_data_fetched

    return report_data


def __decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
        raise TypeError