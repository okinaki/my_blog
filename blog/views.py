from django.shortcuts import render, get_object_or_404
from .models import Post


def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]  # the last 3 posts will be on top
    # it will be translated for SQL query
    return render(request, "blog/index.html", {
        "posts": latest_posts  # define a context
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all_posts.html', {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    # identified_post = Post.objects.get(slug=slug) # this in try-except block or with using get_object_or_404
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {
        "post": identified_post,
        "post_tags": identified_post.tags.all()  # we will loop through this in post_detail.html
    })
