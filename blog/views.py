from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
#from django.http import HttpResponse, JsonResponse

# Create your views here.
def blog_view(request):
    #'blog/blog-home.html' or 'blog\\blog-home.html'
    post = Post.objects.filter(published_date__lte=timezone.now())#if postTime < now, post published.
    content = {'posts':post}
    return render(request, 'blog/blog-home.html',content)

def blog_single(request,pid):    
    post = get_object_or_404(Post,id=pid)
    post.counted_views = post.counted_views+1
    post.save()
    content = {'post':post}
    return render(request, 'blog/blog-single.html',content)

def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,id=pid)
    content = {'post':post}
    return render(request, 'blog/test.html',content)