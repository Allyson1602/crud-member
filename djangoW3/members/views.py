from django.http import HttpResponse
from .models import Members


def index(request):
    output = ""
    mymembers = Members.objects.all().values()

    for x in mymembers:
        output += x['firstname']

    return HttpResponse(output)
