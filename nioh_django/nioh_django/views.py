from django.http import HttpResponse

def initPage(request):
    return HttpResponse("<h1>Hello</h1>")