from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    def snippet(self):
        return f"{self.body[:100]} ..."
