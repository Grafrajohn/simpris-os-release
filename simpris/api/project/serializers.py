from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyCriticalWork, VMyOrganisations, VMyProjects,\
    VProjectTasklists
from simpris.models.models import Userproject, Project, Document, Link, Tasklist, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class VMyCriticalWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyCriticalWork
        fields = ('ordercol', 'projectid', 'itemid', 'type', 'projectname', 'taskdescription')


class VClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyOrganisations
        fields = ('clientid', 'organisationid', 'organisationname', 'userid')


class VProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyProjects
        fields = ('projectid', 'organisationid', 'organisationname', 'userid', 'projectname', 'projectdescription')


class VProjectTasklistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VProjectTasklists
        fields = ('projectid', 'projectname', 'tasklistid', 'tasklistname')


class VProjectTasklistsSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VProjectTasklists
        fields = ('projectname', 'tasklistid', 'tasklistname')


class VProjectSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('projectname', 'projectid')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TasklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userproject
        fields = ('projectid', 'userid')
        fields = '__all__'


class APIProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class APIUserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userproject
        fields = '__all__'


class WholeTaslistSerializer(serializers.Serializer):
    tasklist = TasklistSerializer
    tasks = TaskSerializer(many=True)
    fields = '__all__'


class WholeProjectSerializer(serializers.Serializer):
    project = ProjectSerializer
    users = UserProjectSerializer(many=True)
    documents = DocumentSerializer(many=True)
    links = LinkSerializer(many=True)
    tasklists = TasklistSerializer(many=True)
    fields = '__all__'
