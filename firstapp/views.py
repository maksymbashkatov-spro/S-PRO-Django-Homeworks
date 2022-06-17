from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
import datetime


dd = datetime.date.today().strftime('%d.%m.%Y')
dd_lst = tuple(dd.split('.'))


def hellodjango(request: HttpRequest):
    return HttpResponse('Hello Django!')


def greeting(request: HttpRequest, name):
    return HttpResponse(f'Hello {name}!')


def get_date(request: HttpRequest):
    return HttpResponse(dd)


def get_concrete_date(request: HttpRequest, date_format):
    if date_format == 'year':
        return HttpResponse(dd_lst[2])
    elif date_format == 'month':
        return HttpResponse(dd_lst[1])
    elif date_format == 'day':
        return HttpResponse(dd_lst[0])
    else:
        return HttpResponseNotFound(f'Date format {date_format} is not found.')
