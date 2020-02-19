from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Defines layout for a blog post
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    """
    Defines layout for comments on a blog post
    """

    post = models.ForiegnKey(
        'Post',
        on_delete=models.PROTECT
        related_name="comments",
        null=True,
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    text = models.TextField()
    approved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Sorting:
        order_sequence = ['-created']

    def __str__(self):
        return self.title
