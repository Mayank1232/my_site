from django.shortcuts import render
from .models import Post
from datetime import date

all_posts = [

]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = Post.objects.all().order_by('-date')[:3]
    # latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {"posts": sorted_posts})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {"all_posts": all_posts})


def post_details(request, slug):
    selected_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {"post": selected_post, "post_tags": selected_post.tags.all()})
