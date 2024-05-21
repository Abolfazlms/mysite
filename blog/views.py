from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
#from django.http import HttpResponse, JsonResponse

# Create your views here.
def blog_view(request):
    #'blog/blog-home.html' or 'blog\\blog-home.html'
    post = Post.objects.filter(published_date__lte=timezone.now(),status=1)#if postTime < now, post published.    
    content = {'posts':post}
    return render(request, 'blog/blog-home.html',content)

def blog_single(request,pid):    
    post = get_object_or_404(Post,id=pid,status=1,published_date__lte=timezone.now(),)# check if publish status = 1 and postTime < now time, then publish that
    prevPost = Post.objects.filter(id__lt = pid,published_date__lte=timezone.now(),status=1).last()
    nextPost = Post.objects.filter(id__gt = pid,published_date__lte=timezone.now(),status=1).first()
    
    post.counted_views = post.counted_views+1
    post.save()    
    content = {'post':post,'prev':prevPost,'next':nextPost}
    return render(request, 'blog/blog-single.html',content,)

def test(request):
    # post = Post.objects.get(id=pid)
    # post = get_object_or_404(Post,id=pid)
    # content = {'post':post}
    # return render(request, 'blog/test.html',content)
    return render(request, 'blog/test.html')

