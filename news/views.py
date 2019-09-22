from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
"""
view takes request from a user prosses it and it returns response to the user
"""

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the James Tribune')
# FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY 
def news_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def past_days_news(request,past_date):
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

   