from django.shortcuts import render
from .models import Post

def post_list(request):
    # Your view logic here
    return render(request, 'blog/post_list.html', {})


# Create your views here.
