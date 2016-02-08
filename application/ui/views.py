from django.shortcuts import render
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


#@login_required(login_url='/login/')
def main(request):
        return render(request, "main/base_general.jade", {})
