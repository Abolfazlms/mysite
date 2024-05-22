from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.datetime.now(),status=1)
    print(posts)
    content = {'posts':posts}
    return render(request,'mysite/index.html',content)

def about_view(request):
    return render(request,'mysite\\about.html')
def contact_view(request):
    return render(request,'mysite\\contact.html')
def elements_view(request):
    return render(request,'mysite\\elements.html')

    