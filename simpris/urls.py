from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken import views

import simpris.apps.account.views
import simpris.apps.activity.views
import simpris.apps.auth.views
import simpris.apps.bootstrap4.views
import simpris.apps.comment.views
import simpris.apps.dashboard.views
import simpris.apps.error.views
import simpris.apps.idea.views
import simpris.apps.interaction.views
import simpris.apps.invoice.views
import simpris.apps.lookup.views
import simpris.apps.organisation.views
import simpris.apps.phase.views
import simpris.apps.problem.views
import simpris.apps.programme.views
import simpris.apps.project.views
import simpris.apps.prototype.views
import simpris.apps.queue.views
import simpris.apps.register.views
import simpris.apps.report.views
import simpris.apps.schedule.views
import simpris.apps.search.views
import simpris.apps.system.views
import simpris.apps.task.views
import simpris.apps.tasklist.views
import simpris.apps.calendartab.views
import simpris.apps.team.views
import simpris.apps.time.views
import simpris.apps.uploads.views
import simpris.apps.user.views
import simpris.apps.administration.views
import simpris.views
import simpris.api.account.views
import simpris.api.activity.views
import simpris.api.auth.views
import simpris.api.idea.views
import simpris.api.ideamap.views
import simpris.api.interaction.views
import simpris.api.invoice.views
import simpris.api.kanban.views
import simpris.api.link.views
import simpris.api.lookup.views
import simpris.api.organisation.views
import simpris.api.phase.views
import simpris.api.problem.views
import simpris.api.programme.views
import simpris.api.project.views
import simpris.api.queue.views
import simpris.api.report.views
import simpris.api.schedule.views
import simpris.api.task.views
import simpris.api.tasklist.views
import simpris.api.team.views
import simpris.api.time.views
import simpris.api.user.views
import simpris.api.utility.views
import rest_framework.authtoken.views

admin.autodiscover()

router = routers.DefaultRouter()

urlpatterns = [
    # Examples:
    #-------------------------------------------------------------------------------------------------------------------
    # App
    #
    # account
    path('account/upgrade/', simpris.apps.account.views.upgrade, name='upgrade'),
    # activity
    path('activity/index/', simpris.apps.activity.views.index, name='index'),
    # auth
    path('auth/change-password/', auth_views.PasswordChangeView.as_view),
    path('auth/forgot_password', simpris.apps.auth.views.logoff, name='logoff'),
    path('auth/login/', auth_views.LoginView.as_view, name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view, name='logout'),
    path('auth/logon', simpris.apps.auth.views.logon, name='logon'),
    path('auth/logoff', simpris.apps.auth.views.logoff, name='logoff'),
    # comment
    path('comment/insert/<int:parent_id>/', simpris.apps.comment.views.insert, name='insert'),
    # dashboard
    path('home/dashboard/', simpris.apps.dashboard.views.dashboard, name='dashboard'),
    # default
    path('', simpris.apps.auth.views.logon, name='logon'),
    # error
    path('error/list/', simpris.apps.error.views.list, name='errorlist'),
    # home
    path('project/home/', simpris.apps.project.views.index, name='index'),
    # ideas
    path('ideas/detail/', simpris.apps.idea.views.detail, name='detail'),
    path('ideas/index/', simpris.apps.idea.views.index, name='index'),
    path('ideas/index1/', simpris.apps.idea.views.index1, name='index1'),
    path('ideas/index2/', simpris.apps.idea.views.index2, name='index2'),
    path('ideas/index3/', simpris.apps.idea.views.index3, name='index3'),
    path('ideas/index4/', simpris.apps.idea.views.index4, name='index4'),
    path('ideas/index5/', simpris.apps.idea.views.index5, name='index5'),
    # interaction
    path('interaction/index/', simpris.apps.interaction.views.index, name='index'),
    # invoice
    path('invoice/activity/', simpris.apps.invoice.views.activity, name='activity'),
    path('invoice/list/', simpris.apps.invoice.views.invoicelist, name='invoicelist'),
    path('invoice/create/', simpris.apps.invoice.views.create, name='create'),
    path('invoice/detail/<int:inv_id>/', simpris.apps.invoice.views.detail, name='detail'),
    path('invoice/insertitems/', simpris.apps.invoice.views.insertitems, name='insertitems'),
    path('invoice/format/', simpris.apps.invoice.views.format, name='format'),
    path('invoice/prepare/', simpris.apps.invoice.views.prepare, name='prepare'),
    path('invoice/printout/<int:inv_id>/', simpris.apps.invoice.views.printout, name='printout'),
    # lookup
    path('lookup/index/', simpris.apps.lookup.views.index, name='index'),
    # organisation
    path('organisation/activity/', simpris.apps.organisation.views.activity, name='actiity'),
    path('organisation/list/', simpris.apps.organisation.views.list, name='list'),
    path('client/list/', simpris.apps.organisation.views.list, name='list'),
    path('organisation/create/', simpris.apps.organisation.views.create, name='create'),
    path('organisation/detail/<int:org_id>/', simpris.apps.organisation.views.detail, name='detail'),
    path('organisation/edit/<int:org_id>/', simpris.apps.organisation.views.edit, name='edit'),
    path('organisation/history/<int:org_id>/', simpris.apps.organisation.views.history, name='history'),
    path('organisation/users/<int:org_id>/', simpris.apps.organisation.views.users, name='users'),
    # phase
    path('phase/create/', simpris.apps.phase.views.create, name='create'),
    path('phase/detail/<int:phase_id>/', simpris.apps.phase.views.detail, name='detail'),
    path('phase/edit/<int:phase_id>/', simpris.apps.phase.views.edit, name='edit'),
    path('phase/list/', simpris.apps.phase.views.phaselist, name='phaselist'),
    # problem
    path('problem/activity/', simpris.apps.problem.views.activity, name='activity'),
    path('problem/create/', simpris.apps.problem.views.create, name='create'),
    path('problem/detail/<int:prob_id>/', simpris.apps.problem.views.detail, name='detail'),
    path('problem/edit/<int:prob_id>/', simpris.apps.problem.views.edit, name='edit'),
    path('problem/history/<int:prob_id>/', simpris.apps.problem.views.history, name='history'),
    path('problem/log/<int:prob_id>/', simpris.apps.problem.views.log, name='log'),
    path('problem/list/', simpris.apps.problem.views.problemlist, name='problemlist'),
    # programme
    path('programme/activity/', simpris.apps.programme.views.activity, name='activity'),
    path('programme/create/', simpris.apps.programme.views.create, name='create'),
    path('programme/detail/<int:programme_id>/', simpris.apps.programme.views.detail, name='detail'),
    path('programme/edit/<int:programme_id>/', simpris.apps.programme.views.edit, name='edit'),
    path('programme/history/<int:programme_id>/', simpris.apps.programme.views.history, name='history'),
    path('programme/list/', simpris.apps.programme.views.list, name='list'),
    # project
    path('project/activity/', simpris.apps.project.views.activity, name='activity'),
    path('project/create/', simpris.apps.project.views.create, name='create'),
    path('project/detail/<int:proj_id>/', simpris.apps.project.views.detail, name='detail'),
    path('project/edit/<int:proj_id>/', simpris.apps.project.views.edit, name='edit'),
    path('project/gantt/<int:proj_id>/', simpris.apps.project.views.gantt, name='gantt'),
    path('project/history/<int:proj_id>/', simpris.apps.project.views.history, name='history'),
    path('project/ideas/<int:proj_id>/', simpris.apps.project.views.ideas, name='ideas'),
    path('project/list/', simpris.apps.project.views.projectlist, name='projectlist'),
    path('project/log/<int:proj_id>/', simpris.apps.project.views.log, name='log'),
    path('project/users/<int:proj_id>/', simpris.apps.project.views.users, name='users'),
    # queue
    path('queue/create/', simpris.apps.queue.views.create, name='create'),
    path('queue/detail/<int:queue_id>/', simpris.apps.queue.views.detail, name='detail'),
    path('queue/edit/<int:queue_id>/', simpris.apps.queue.views.edit, name='edit'),
    path('queue/list/', simpris.apps.queue.views.list, name='queuelist'),
    path('queue/members/<int:queue_id>/', simpris.apps.queue.views.members, name='members'),
    # register
    path('register/new', simpris.apps.register.views.new, name='new'),
    path('register/thankyou', simpris.apps.register.views.thankyou, name='thankyou'),
    path('register/welcome', simpris.apps.register.views.welcome, name='welcome'),
    # report
    path('report/project', simpris.apps.report.views.datatable, name='datatable'),
    path('report/chart/<int:chart_id>/<int:item_id>/', simpris.apps.report.views.chart, name='chart'),
    path('report/gantt/<int:proj_id>/', simpris.apps.report.views.gantt_jq, name='gantt_jq'),
    path('report/generic/<int:report_id>/', simpris.apps.report.views.generic, name='generic'),
    path('report/detail/<str:report_id>/', simpris.apps.report.views.datatable, name='datatable'),
    path('report/list/', simpris.apps.report.views.list, name='list'),
    path('report/metric/<str:report_id>/', simpris.apps.report.views.metric, name='metric'),
    # schedule
    path('schedule/kanban', simpris.apps.schedule.views.kanban, name='kanban'),
    path('schedule/schedule', simpris.apps.schedule.views.schedule, name='schedule'),
    # search
    path('search/index', simpris.apps.search.views.index, name='index'),
    # system
    path('system/dashboard/', simpris.apps.system.views.dashboard, name='dashboard'),
    path('system/index/', simpris.apps.system.views.index, name='index'),
    # task
    path('task/activity/', simpris.apps.task.views.activity, name='activity'),
    path('task/list/', simpris.apps.task.views.tasklist, name='tasklist'),
    path('task/detail/<int:task_id>/', simpris.apps.task.views.detail, name='detail'),
    path('task/edit/<int:task_id>/', simpris.apps.task.views.edit, name='edit'),
    path('task/history/<int:task_id>/', simpris.apps.task.views.history, name='history'),
    path('task/move/<int:task_id>/', simpris.apps.task.views.move, name='move'),
    # tasklist
    path('tasklist/', simpris.apps.tasklist.views.move, name='move'),
    # team
    path('team/create/', simpris.apps.team.views.create, name='create'),
    path('team/detail/<int:team_id>/', simpris.apps.team.views.detail, name='detail'),
    path('team/edit/<int:team_id>/', simpris.apps.team.views.edit, name='edit'),
    path('team/list/', simpris.apps.team.views.list, name='teamlist'),
    path('team/members/<int:team_id>/', simpris.apps.team.views.members, name='members'),
    # time
    path('time/activity/', simpris.apps.time.views.activity, name='activity'),
    path('time/calendar/', simpris.apps.calendartab.views.calendartab, name='calendartab'),
    path('time/timegrid/', simpris.apps.time.views.timegrid, name='timegrid'),
    path('time/list/', simpris.apps.time.views.timelist, name='timelist'),
    path('time/timesheet/', simpris.apps.time.views.timesheet, name='timesheet'),
    path('time/timeprint/<int:time_start>/<int:time_end>/', simpris.apps.time.views.timeprint, name='timeprint'),
    path('time/create/', simpris.apps.time.views.create, name='create'),
    path('time/detail/<int:time_id>/', simpris.apps.time.views.detail, name='detail'),
    path('time/edit/<int:time_id>/', simpris.apps.time.views.edit, name='edit'),
    # upload
    path('uploads/upload/', simpris.apps.uploads.views.upload, name='upload'),
    # user
    path('user/activity/', simpris.apps.user.views.activity, name='activity'),
    path('user/create/', simpris.apps.user.views.create, name='create'),
    path('user/detail/<int:user_id>/', simpris.apps.user.views.detail, name='detail'),
    path('user/edit/<int:user_id>/', simpris.apps.user.views.edit, name='edit'),
    path('user/history/<int:user_id>/', simpris.apps.user.views.history, name='history'),
    path('user/password/', simpris.apps.user.views.password, name='password'),
    path('user/profile/', simpris.apps.user.views.profile, name='profile'),
    path('user/list/', simpris.apps.user.views.userlist, name='userlist'),
    # catch-all default
    # path('$', 'simpris.apps.project.views.index', name='index'),
    path('', TemplateView.as_view(template_name="web/index.html"), name='index'),
    # stress
    # path('stress/', 'index'),
    path('error/', simpris.views.error, name='error'),
    #--------------------------------------------------------------------------------------------------------------------
    # Admin    
    # path('admin/', include(admin.site.urls)), deprecated v2
    path('admin/', admin.site.urls),
    path('admin/home/', simpris.apps.administration.views.home, name='home'),
    # -------------------------------------------------------------------------------------------------------------------
    # Web-related pages
    #
    # url('BingSiteAuth\.xml/$', TemplateView.as_view(template_name='BingSiteAuth.xml', content_type='text/plain')),
    # url('robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    # url('humans\.txt/$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    # url('sitemap\.xml/$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain')),
    # -------------------------------------------------------------------------------------------------------------------
    # Prototype
    #
    path('react', TemplateView.as_view(template_name="prototype/react/index.html"), name='index'),
    #path('angular2', TemplateView.as_view(template_name="prototype/angular2/index.html"), name='index'),
    path('alt', TemplateView.as_view(template_name="prototype/react-alt/index.html"), name='index'),
    #path('/app/.*$', simpris.static.js.angular2.app.my_angular_homepage),
    path('redux', TemplateView.as_view(template_name="prototype/redux/index.html"), name='index'),
    path('mredux', TemplateView.as_view(template_name="prototype/redux-medium/index.html"), name='index'),
    path('basicreact', TemplateView.as_view(template_name="simpris/react/basic.html"), name='index'),
    path('basiccomponent', TemplateView.as_view(template_name="simpris/react/component.html"), name='index'),
    path('basicstate', TemplateView.as_view(template_name="simpris/react/basic.html"), name='index'),
    path('basiccombined', TemplateView.as_view(template_name="simpris/react/state.html"), name='index'),
    path('basicwhole', TemplateView.as_view(template_name="simpris/react/whole.html"), name='index'),
    path('prototype/vue/', simpris.apps.prototype.views.vue, name='vue'),
    # bootstrap 4
    path('bootstrap4/dashboard/', simpris.apps.bootstrap4.views.dashboard, name='dashboard'),
    #-------------------------------------------------------------------------------------------------------------------
    # Help
    #
    path('help', TemplateView.as_view(template_name="help/index.html"), name='index'),
    #-------------------------------------------------------------------------------------------------------------------
    # API
    #
    # account api
    path('api/account/auto/', simpris.api.account.views.auto, name='auto'),
    # activity api
    path('api/activity/list/', simpris.api.activity.views.list, name='list'),
    # auth
    path('api/api-token-auth/', views.obtain_auth_token), # generic DRF view
    path('api/auth/authenticate/', simpris.api.auth.views.authenticate),
    path('api/auth/token/', simpris.api.auth.views.token),
    # error
    path('api/error/insert/', simpris.api.idea.views.insert, name='insert'),
    # home api
    path('api/project/home/', simpris.api.project.views.home, name='home'),
    # idea api
    path('api/idea/delete/', simpris.api.idea.views.delete, name='delete'),
    path('api/idea/insert/', simpris.api.idea.views.insert, name='insert'),
    path('api/idea/list/', simpris.api.idea.views.list, name='list'),
    path('api/idea/update/', simpris.api.idea.views.update, name='update'),
    # idea map api
    path('api/ideamap/delete/', simpris.api.ideamap.views.delete, name='delete'),
    path('api/ideamap/insert/', simpris.api.ideamap.views.insert, name='insert'),
    path('api/ideamap/list/', simpris.api.ideamap.views.list, name='list'),
    path('api/ideamap/update/', simpris.api.ideamap.views.update, name='update'),
    # interactions api
    path('api/interaction/detail/<int:int_id>/', simpris.api.interaction.views.detail, name='detail'),
    path('api/interaction/insert/', simpris.api.interaction.views.insert, name='insert'),
    path('api/interaction/list/', simpris.api.interaction.views.list, name='list'),
    # invoices api
    path('api/invoice/invoices/', simpris.api.invoice.views.invoices, name='invoices'),
    path('api/invoice/delete/<int:inv_id>/', simpris.api.invoice.views.delete, name='delete'),
    path('api/invoice/insert/', simpris.api.invoice.views.insert, name='insert'),
    # kanban api
    path('api/kanban/insert/', simpris.api.kanban.views.insert, name='insert'),
    path('api/kanban/move/', simpris.api.kanban.views.move, name='move'),
    # link api
    path('api/link/delete/<int:link_id>/', simpris.api.link.views.delete, name='delete'),
    path('api/link/insert/', simpris.api.link.views.insert, name='insert'),
    path('api/link/list/<int:entity_id>/<int:entity_type>/', simpris.api.link.views.list, name='list'),
    path('api/link/update/<int:link_id>/', simpris.api.link.views.update, name='update'),
    # lookup api
    path('api/lookup/insert/', simpris.api.lookup.views.insert, name='insert'),
    path('api/lookup/list/', simpris.api.lookup.views.list, name='list'),
    path('api/lookup/lookuptypes/', simpris.api.lookup.views.lookuptypes, name='lookuptypes'),
    path('api/lookup/lookups/<int:lookup_type_id>/', simpris.api.lookup.views.lookups, name='lookups'),
    path('api/lookup/update/', simpris.api.lookup.views.update, name='update'),
    # organisation api
    path('api/organisation/organisations/', simpris.api.organisation.views.organisations, name='organisations'),
    path('api/organisation/adduser/', simpris.api.organisation.views.adduser, name='adduser'),
    path('api/organisation/delete/<int:org_id>/', simpris.api.organisation.views.delete, name='delete'),
    path('api/organisation/deleteuser/', simpris.api.organisation.views.deleteuser, name='deleteuser'),
    path('api/organisation/update/', simpris.api.organisation.views.update, name='update'),
    path('api/organisation/insert/', simpris.api.organisation.views.insert, name='insert'),
    # phases api
    path('api/phase/delete/<int:phase_id>/', simpris.api.phase.views.delete, name='delete'),
    path('api/phase/insert/', simpris.api.phase.views.insert, name='insert'),
    path('api/phase/list/', simpris.api.phase.views.phaselist, name='phaselist'),
    path('api/phase/update/', simpris.api.phase.views.update, name='update'),
    # problems api
    path('api/problem/problems/<slug:prob_range>/', simpris.api.problem.views.problems, name='problems'),
    path('api/problem/delete/<int:prob_id>/', simpris.api.problem.views.delete, name='delete'),
    path('api/problem/update/', simpris.api.problem.views.update, name='update'),
    path('api/problem/insert/', simpris.api.problem.views.insert, name='insert'),
    # programmes api
    path('api/programme/programmes/', simpris.api.programme.views.programmes, name='programmes'),
    path('api/programme/delete/<int:programme_id>/', simpris.api.programme.views.delete, name='delete'),
    path('api/programme/update/', simpris.api.programme.views.update, name='update'),
    path('api/programme/insert/', simpris.api.programme.views.insert, name='insert'),
    # projects api
    path('api/project/delete/<int:proj_id>/', simpris.api.project.views.delete, name='delete'),
    path('api/project/deleteuser/', simpris.api.project.views.deleteuser, name='deleteuser'),
    path('api/project/programme/', simpris.api.project.views.programme, name='programme'),
    path('api/project/programme_project_delete/', simpris.api.project.views.programme_project_delete, name='programme_project_delete'),
    path('api/project/projects/', simpris.api.project.views.projects, name='projects'),
    path('api/project/search/', simpris.api.project.views.project_search, name='project_search'),
    path('api/project/searchj/', simpris.api.project.views.project_search_json, name='project_search_json'),
    path('api/project/update/', simpris.api.project.views.update, name='update'),
    path('api/project/insertuser/', simpris.api.project.views.insertuser, name='insertuser'),
    path('api/project/insert/', simpris.api.project.views.insert, name='insert'),
    # queues api
    path('api/queue/delete/<int:queue_id>/', simpris.api.queue.views.delete, name='delete'),
    path('api/queue/insert/', simpris.api.queue.views.insert, name='insert'),
    path('api/queue/list/', simpris.api.queue.views.queuelist, name='queuelist'),
    path('api/queue/member_create/', simpris.api.queue.views.member_create, name='member_create'),
    path('api/queue/member_delete/', simpris.api.queue.views.member_delete, name='member_delete'),
    path('api/queue/team_create/', simpris.api.queue.views.team_create, name='team_create'),
    path('api/queue/team_delete/', simpris.api.queue.views.team_delete, name='team_delete'),
    path('api/queue/update/', simpris.api.queue.views.update, name='update'),
    # reports api
    # schedule api
    path('api/schedule/move/', simpris.api.schedule.views.move, name='move'),
    # tasks api
    path('api/task/delete/<int:task_id>/', simpris.api.task.views.delete, name='delete'),
    path('api/task/dependencies/', simpris.api.task.views.dependencies, name='dependencies'),
    path('api/task/delete_post/', simpris.api.task.views.delete_post, name='delete_post'),
    path('api/task/detail/', simpris.api.task.views.detail, name='detail'),
    path('api/task/insert/', simpris.api.task.views.insert, name='insert'),
    path('api/task/searchj/', simpris.api.task.views.search_json, name='search_json'),
    path('api/task/tasks/', simpris.api.task.views.tasks, name='tasks'),
    path('api/task/update/', simpris.api.task.views.update, name='update'),
    path('api/task/update_quick/', simpris.api.task.views.update_quick, name='update_quick'),
    path('api/task/move/', simpris.api.task.views.move, name='move'),
    # tasklists api
    path('api/tasklist/delete/', simpris.api.tasklist.views.delete, name='delete'),
    path('api/tasklist/insert/', simpris.api.tasklist.views.insert, name='insert'),
    # path('api/tasklist/list/(<task_id>\d{1,})/', simpris.api.tasklist.views.insert, name='insert'),
    path('api/tasklist/update/', simpris.api.tasklist.views.update, name='update'),
    # teams api
    path('api/team/delete/<int:team_id>/', simpris.api.team.views.delete, name='delete'),
    path('api/team/insert/', simpris.api.team.views.insert, name='insert'),
    path('api/team/list/', simpris.api.team.views.teamlist, name='teamlist'),
    path('api/team/member_create/', simpris.api.team.views.member_create, name='member_create'),
    path('api/team/member_delete/', simpris.api.team.views.member_delete, name='member_delete'),
    path('api/team/update/', simpris.api.team.views.update, name='update'),
    # time api  
    path('api/time/calendar/', simpris.api.time.views.calendar, name='calendar'),
    path('api/time/timegrid/', simpris.api.time.views.timegrid, name='timegrid'),
    path('api/time/timetask/', simpris.api.time.views.timetask, name='timetask'),
    path('api/time/timesave/', simpris.api.time.views.calendar, name='calendar'),
    path('api/time/inserttime/', simpris.api.time.views.insert_time, name='insert_time'),
    path('api/time/updatetime/', simpris.api.time.views.update_time, name='update_time'),
    path('api/time/deletetime/', simpris.api.time.views.delete_time, name='delete_time'),
    path('api/time/times/', simpris.api.time.views.times, name='times'),
    path('api/time/delete/<int:time_id>/', simpris.api.time.views.delete, name='delete'),
    path('api/time/insert/', simpris.api.time.views.insert, name='insert'),
    path('api/time/update/', simpris.api.time.views.update, name='update'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('api-token-auth/', rest_framework.authtoken.views.obtain_auth_token),
    # user api
    path('api/user/detail/', simpris.api.user.views.detail, name='detail'),
    path('api/user/delete/<int:user_id>/', simpris.api.user.views.delete, name='delete'),
    path('api/user/password/', simpris.api.user.views.password, name='password'),
    path('api/user/profile/', simpris.api.user.views.profile, name='profile'),
    path('api/user/projectusers/<int:task_id>/', simpris.api.user.views.projectusers, name='projectusers'),
    path('api/user/insert/', simpris.api.user.views.insert, name='insert'),
    path('api/user/update/', simpris.api.user.views.update, name='update'),
    path('api/user/users/', simpris.api.user.views.users, name='users'),
    # utility api
    # path('api/utility/logerror/', simpris.api.utility.views.logerror, name='logerror'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
