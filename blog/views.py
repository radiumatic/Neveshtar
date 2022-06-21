from django.shortcuts import render, get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_list(request, page=1):
    posts=Post.objects.all().order_by('-published_date')
    posts = posts[(page-1)*10:page*10]
    pages_amount=len(Post.objects.all())//10
    return render(request, 'blog/post_list.html', {'posts':posts, 'pages_amount':range(1, pages_amount+2), 'page':page})
def post_detail(request, url):
    post=get_object_or_404(Post, link=url)
    comments = post.comment_set.all().order_by('-created_date')
    return render(request, 'blog/post_detail.html', {'post':post, 'comments':comments})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog/post_detail', url=post.link)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

        
