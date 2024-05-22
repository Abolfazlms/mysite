from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('mysite/latest-post.html')
def latestPosts():
    # posts = Post.objects.filter(status = 1).order_by('published_date')
    posts = Post.objects.filter(published_date__lte=timezone.datetime.now(),status = 1).order_by('-published_date')[:6]
    return {'posts':posts}