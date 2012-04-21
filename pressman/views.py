from django.http import HttpResponse, HttpResponseNotFound
from pressman.models import PressRelease

def detail(request, pid):
    try:
        p = PressRelease.objects.get(id=pid)
        return HttpResponse(p.pr_title)
    except PressRelease.DoesNotExist:
        return HttpResponseNotFound('No existe lo que esta buscando')