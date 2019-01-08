from django.shortcuts import render
from django.http import Http404

#from .mocks import Post
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def showpost(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404('sorry')
    return render(request, 'blog/showpost.html', {'post': post})



