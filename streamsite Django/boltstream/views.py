from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Stream


def shiny_auth(request):
    if request.user.is_authenticated:
        return HttpResponse(status=200)
    return HttpResponse(status=403)

@csrf_exempt
def shiny_auth2(request):
    if 'psk' in request.POST:
        if request.POST['psk'] == 'totallysecretpassword':
            return HttpResponse(status=200)
    return HttpResponse(status=403)