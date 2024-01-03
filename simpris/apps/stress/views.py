from django.shortcuts import render

# Create your views here.
@render_to('your_app_name:template_name.html')
@login_required
def view_name(request):
    # ...python code...
    return {
        parameters
    }

def index(request):
    logger.info("search index")