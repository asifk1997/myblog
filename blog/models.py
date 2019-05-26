from django.db import models
from django.contrib.auth.models import Permission, User



class Blogpost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default=None)
    content=models.CharField(max_length=1000,default=None)

    def __str__(self):
        return self.title