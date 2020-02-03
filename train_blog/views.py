"""
train_blog/views.py
"""

from django.http import HttpResponse

def index(Response):
    return HttpResponse("Welcome to British Model Trains Ltd!")
