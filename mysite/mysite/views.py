from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> The time is %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> The time after  %s hours is %s.</body></html>" % (offset, now)
    return HttpResponse(html)