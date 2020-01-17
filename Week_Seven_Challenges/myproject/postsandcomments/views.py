from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Post
from .models import Comment

def index(request):
    post_text = Post.objects.order_by('-pub_date')
    data = { 'post_text': post_text}
    return render(request, 'posts/index.html', data)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    data = { 'post': post, 'comments': comments}
    return render(request, 'posts/detail.html', data)

