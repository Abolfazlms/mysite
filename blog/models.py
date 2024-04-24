from django.db import models

# Create your models here.
class Post(models.Model):
    #author
    #image
    title = models.CharField(max_length = 255)
    content = models.TextField()
    #tags
    #category
    counted_views = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.title} - {self.id}'
    

