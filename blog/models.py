from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
    name =   models.CharField(max_length=255)
    def __str__(self):
        return self.name 

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(max_length = 255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category) # it's equal to category = models.ManyToManyField(Category,null=True)
    counted_views = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['created_date']
        # verbose_name = 'cosidered post'
        # verbose_name_plural = 'daily_posts'

    def __str__(self):
        return self.title
    
    # def snippets(self):
    #     return self.content [:30] + '...'

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})