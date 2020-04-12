from django.contrib import admin
from . import models

class CommentAdmin(admin.ModelAdmin):
    """
    Admin model for controlling visible fields in Django Admin
    """
    #Visible fields
    list_display = (
        'name',
        'email',
        'text',
        'approved',
    )
    #searchable fields
    search_fields = (
        'name',
        'email',
        'created',
        'updated',
    )
    #Yay or nay on approved
    list_filter = (
        'approved',
    )

class CommentInline(admin.TabularInline):
    """
    Inline model for Django interfacing for Comment model through PostAdmin.
    """
    model = models.Comment
    #visible fields in Django
    fields = (
        'name',
        'email',
        'text',
        'approved',
    )
    #Can't edit these ones though. No touchy touchy
    readonly_fields = (
        'name',
        'email',
        'text',
    )

class PostAdmin(admin.ModelAdmin):
    """
    Does for the Post model what CommentAdmin does for the Comment model
    """
    #visible fields
    list_display = (
        'title',
        'author',
        'status',
        'created',
        'updated',
        'published',
    )
    #searchable fields
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
        'published',
    )
    #filter for draft/published status
    list_filter = (
        'status',
        'topics',
        'published',
    )
    prepopulated_fields = {'slug':('title',)}
    #brings in Comment model for each post
    inlines = [CommentInline]

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Does for the Topic model what CommentAdmin does for the Comment model
    """
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Does for the Contact model what CommentAdmin does for the Comment model
    """
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    #Making everything listed in list_display read-only
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted'
    )

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
