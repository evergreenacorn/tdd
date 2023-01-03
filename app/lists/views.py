from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


# Create your views here.
def home_page(request):
  # return JsonResponse({'status': 'success', 'data': 'hello world'})
  # return HttpResponse("<!DOCTYPE html><title>To-Do lists</title></html>")
  return render(request, 'home.html')
