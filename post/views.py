from django.shortcuts import render
from .models import *


def post_open_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/PostDetail.html', {'post':post})
def post_views(request):

    posts = Post.objects.order_by('-created_at')[:10]
    return render(request, 'post/PostHomePage.html', {'post':posts})
