from django.http import HttpResponse, HttpResponseNotFound
from pressman.models import PressRelease
from django.shortcuts import get_object_or_404, get_list_or_404
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
    t = loader.get_template('pressman/latest.html')
    c = Context({
        'title':p.pr_title,
        'author':p.pr_author,
        'date':p.pr_date_created,
        'link':p.get_absolute_url()
    })
    return HttpResponse(t.render(c))