from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


# Create your views here.
def home_page(request):
    # return render(request, 'home.html')
    return JsonResponse({'status': 'success', 'data': 'hello world'})
