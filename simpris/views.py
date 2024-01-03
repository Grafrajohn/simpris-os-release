from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def error(request):
    logger.info('error')
    
    return render(request, "simpris/error.html")