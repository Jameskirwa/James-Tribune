from django.http import HttpResponse
import datetime as dt
"""
view takes request from a user prosses it and it returns response to the user
"""

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the James Tribune')