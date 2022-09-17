from django.shortcuts import HttpResponse


def special_case_2003(request):
    return HttpResponse('special_case_2003')


def year_archive(request, year):
    return HttpResponse(f'year_archive {year}')


def month_archive(request, year, month):
    return HttpResponse(f'month_archive {year} - {month} ')
