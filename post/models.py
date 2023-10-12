from django.db import models
from django.conf import settings

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField()
    image = models.ImageField(upload_to="post")
    dateCreated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    active = models.BooleanField(default=False)
    other = models.ImageField(upload_to="post", default="")
