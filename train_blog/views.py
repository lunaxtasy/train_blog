"""
train_blog/views.py

The visible bits
"""

from django.http import HttpResponse

def index(Response):
    """
    returns text string to browser when HTTP request is received
    """
    return HttpResponse("Welcome to British Model Trains Ltd!")
