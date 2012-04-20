from django.http import HttpResponse

def detail(request, pid):
    return HttpResponse('mycompanylab is a project cool')