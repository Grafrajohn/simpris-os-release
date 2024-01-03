import time, pytz

from django.utils import timezone

from ..models.models import Useractivity, Error

def log_activity(user_id,activity_type,activity_data,activity_module,activity_sub_module,client_id):

    created_date = timezone.now()

    try:
        user_activity = Useractivity(userid=user_id,activitytype=activity_type,activitydata=activity_data,
                activity_module=activity_module,client_id=client_id,activity_submodule=activity_sub_module,
                activitydate=created_date)

        user_activity.save()
    except:
        pass


def log_error(user_id, client_id, organisation_id, description, module_, submodule, action, subaction):

    created_date = timezone.now()

    error = Error(clientid=client_id, organisationid=organisation_id, userid=user_id, description=description,
                module=module_, submodule=submodule, action=action, subaction=subaction, createddate=created_date)

    error.save()
