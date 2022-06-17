from django.http import HttpRequest, HttpResponse, HttpResponseNotFound


def hellodjango(request: HttpRequest):
    return HttpResponse('Hello Django!')


def greeting(request: HttpRequest, name):
    return HttpResponse(f'Hello {name}!')
