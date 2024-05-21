from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
#from django.http import HttpResponse, JsonResponse

# Create your views here.
# def blog_view(request,cat_name = None,  author_username = None):
#     #'blog/blog-home.html' or 'blog\\blog-home.html'
#     post = Post.objects.filter(published_date__lte=timezone.now(),status=1)#if postTime < now, post published.   
#     #if cat_name: 
#     if cat_name != None:
#         post = post.filter(category__name=cat_name)
#     if author_username:
#         post = post.filter(author__username= author_username)
#     content = {'posts':post}
#     return render(request, 'blog/blog-home.html',content)

def blog_view(request,**kwargs):
    #'blog/blog-home.html' or 'blog\\blog-home.html'
    post = Post.objects.filter(published_date__lte=timezone.now(),status=1)#if postTime < now, post published.   
    #if cat_name: 
    if kwargs.get('cat_name') != None:
        post = post.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        post = post.filter(author__username= kwargs['author_username'])
    content = {'posts':post}
    return render(request, 'blog/blog-home.html',content)

def blog_single(request,pid):    
    posts = get_object_or_404(Post,id=pid,status=1,published_date__lte=timezone.now(),)# check if publish status = 1 and postTime < now time, then publish that
    prevPost = Post.objects.filter(id__lt = pid,published_date__lte=timezone.now(),status=1).last()
    nextPost = Post.objects.filter(id__gt = pid,published_date__lte=timezone.now(),status=1).first()
    
    posts.counted_views = posts.counted_views+1
    posts.save()    
    content = {'post':posts,'prev':prevPost,'next':nextPost}
    return render(request, 'blog/blog-single.html',content,)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now(),)
    posts = posts.filter(category__name=cat_name)
    content = {'posts':posts}

    return render(request,'blog/blog-home.html',content)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    
    if request.method == 'GET':
        # print(request.GET.get('s'))
        posts = posts.filter(content__contains=request.GET.get('s') )
        # if s := request.GET.get('s'): 
        #     posts = posts.filter(content__contains=s)
    content = {'posts':posts}    
    return render(request, 'blog/blog-home.html',content)
    


def test(request):
    # post = Post.objects.get(id=pid)
    # post = get_object_or_404(Post,id=pid)
    # content = {'post':post}
    # return render(request, 'blog/test.html',content)
    return render(request, 'blog/test.html')

