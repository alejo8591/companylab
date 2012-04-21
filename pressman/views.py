from django.http import HttpResponse, HttpResponseNotFound
from pressman.models import PressRelease
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.template import loader, Context
from pressman.models import PressMan, PressRelease

def detail(request, pid):
    p = get_object_or_404(PressRelease, id=pid)
    t = loader.get_template('pressman/detail.html')
    c = Context({'pressman':p})
    return HttpResponse(t.render(c))
    
def pressman_list(request):
    pl = get_list_or_404(PressRelease)
    t = loader.get_template('pressman/list.html')
    c = Context({'pressman_list':pl})
    return HttpResponse(t.render(c))
    
def latest(request):
    """ Retornando info del ultimo post """
    p = PressRelease.objects.latest()
    return render_to_response('pressman/latest.html',{ 'pressman':p, })