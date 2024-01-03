import time

from ..models.models import Error

def log_error(user_id,description,module,submodule,action,subaction,organisation_id,client_id):

    created_date = time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        error = Error(clientid=client_id,organisationid=organisation_id,userid=user_id,description=description,module=module,
            submodule=submodule,action=action,subaction=subaction,createddate=created_date)

        error.save()
    except:
        pass