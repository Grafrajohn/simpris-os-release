from simpris.models.db_views import VUserContextFull
from django.conf import settings

class UserContextFull:
    def __init__(self, request):
        user_full = VUserContextFull.objects.all().filter(username=request.user)
        if user_full:
            for UserRow in user_full:   
                self.id = request.user.id
                self.clientID = UserRow.clientid
                self.username = request.user.username
                self.organisationID = UserRow.organisationid
                self.organisationName = UserRow.organisationname
                self.firstName = request.user.first_name
                self.lastName = request.user.last_name
                self.isSuperUser = request.user.is_superuser
                self.isClientAdmin = request.user.is_staff
                self.fullname = self.firstName + ' ' + self.lastName
                self.clientName = UserRow.clientname
                self.teamName = UserRow.teamname
        else:
            self.id = None
            self.clientID = None 
            self.username = None
            self.organisationID = None
            self.organisationName = None
            self.firstName = None
            self.lastName = None  
            self.isSuperUser = None
            self.isClientAdmin = None
            self.fullname = None
            self.clientName = None
            self.teamName = None

    
    def getFullName(self):
        fullname = self.firstName + ' ' + self.lastName 
        return fullname
