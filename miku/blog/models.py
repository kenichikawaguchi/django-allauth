from django.db import models


class BlogPost(models.Model):
    ''' Model Class
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

