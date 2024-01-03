from django.conf import settings # import the settings file

def get_base_url(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'BASE_URL_DJ': settings.BASE_URL_DJ}

def get_base_web(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'BASE_URL_WEB': settings.BASE_URL_WEB}

def get_subscription_url(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'BASE_URL_SUBSCRIPTION': settings.BASE_URL_SUBSCRIPTION}

def get_recaptcha_site_key(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY}    
