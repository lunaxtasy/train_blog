#api/urls.py

from django.urls import path
from . import views

#API app's namespace
app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
]
