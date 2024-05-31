from django import template
from blog.models import Post,Category, Comments
from django.utils import timezone

register = template.Library()

@register.simple_tag(name = 'totalPost')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name = 'posts')
def function():
    posts = Post.objects.filter(status = 1)
    return posts

@register.filter
def snippets(value, args = 30):
    return value[:args] + ' ...'

@register.inclusion_tag('popular_posts.html')
def popularPosts():
    # posts = Post.objects.filter(status = 1).order_by('published_date')
    posts = Post.objects.filter(status = 1).order_by('-published_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestPosts(arg=3):
    # posts = Post.objects.filter(status = 1).order_by('published_date')
    posts = Post.objects.filter(status = 1,published_date__lte=timezone.now(),).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postCategories():
    posts = Post.objects.filter(status = 1,)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
        cat_dict[name] = posts.filter(category = name).count()
    return{'categories':cat_dict}

@register.simple_tag(name = 'comments_count')
def function(pid):
    return Comments.objects.filter(post = pid, approved = True).count()
