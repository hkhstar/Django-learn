from django.http import HttpResponse , JsonResponse


def http_test(request):
    return HttpResponse('<h1>hi django</h1>')




def json_test(request):
    return JsonResponse({'name':'ali'})