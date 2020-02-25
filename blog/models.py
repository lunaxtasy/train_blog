from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Defines layout for a blog post. Pulled from course notes
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    #Title of the actual blog post
    title = models.CharField(max_length=255)
    #Slug path for future URL
    slug = models.SlugField(
        null=False,
        help_text='The time and date of actual publishing',
        unique_for_date='published'
    )
    #The staff member who wrote the post
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="train_blog",
        null=True,
    )
    #Is it published? Yay or nay? Post must be set to published to be viewable
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make visible'
    )
    #The actual post
    content = models.TextField()
    #Publishing day and time
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The time and date of actual publishing'
    )
    #Date/time post was originally created
    created = models.DateTimeField(auto_now_add=True)
    #Date/time post was updated
    updated = models.DateTimeField(auto_now=True)

    class Sorting:
        order_sequence = ['-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Defines layout for comments on a blog post
    """

    #linkage for Comment model to Post model
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        blank=False,
    )
    #Commentor's name
    name = models.CharField(
        null=False,
        blank=False,
        max_length=32,
    )
    #Their email address (must be valid)
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=254,
    )
    #Body of the comment, good or bad
    text = models.TextField(
        null=False,
        blank=False,
    )
    #Allows staff to decide if comment will be publicly visible or not
    approved = models.BooleanField(default=True)
    """
    attempt at Q6 of Part 3 of Assignment 2 (unfinished)
    def approved(self):
        queryset = super().approved()
        return queryset.exclude(approved=False)
    """
    #Date/time comment is first created
    created = models.DateTimeField(auto_now_add=True)
    #Date/time comment has been updated
    updated = models.DateTimeField(auto_now=True)

    class Sorting:
        """
        Sets order to reverse chronogical creation date
        """
        order_sequence = ['-created']

    def __str__(self):
        """
        str() customisation
        """
        return 'Comment by ' + self.name
