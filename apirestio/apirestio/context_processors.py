from django.conf import settings
from datetime import date, datetime, time

today = datetime.now().replace(tzinfo=None)

def mydata(request):
    
    return {'todays': today}