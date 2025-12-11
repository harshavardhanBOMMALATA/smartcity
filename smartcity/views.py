from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello ✔ Default view working")
