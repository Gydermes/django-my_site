from django.shortcuts import HttpResponse


def base(request):
    return HttpResponse(f'This is the first page my site')