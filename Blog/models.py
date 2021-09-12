from django.db import models
from Dashboard.models import Blog


# Create your models here.
class Comment(models.Model):
    Names = models.CharField(max_length=200)
    Feedback = models.TextField()
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    Commented_on = models.DateTimeField(auto_now_add=True)
