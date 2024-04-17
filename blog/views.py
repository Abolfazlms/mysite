from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def blog_view(request):
    #'blog/blog-home.html' or 'blog\\blog-home.html'
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    return render(request, 'blog/blog-single.html')