from django.http import HttpResponse, JsonResponse
def http_test(request):
    return HttpResponse('<h2>Hello World!</h2>')
def json_test(request):
    return JsonResponse({'name':'ali'})