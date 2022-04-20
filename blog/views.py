from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Like
from django.http import HttpResponse
import json
# Create your views here.
def post_list(request):
    posts=Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
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
@csrf_exempt
@login_required
def add_like(request, pk):
    status = {}
    try:
        post = Post.objects.get(pk=pk)
        like = Like(post=post, user=request.user)
        like.save()
        status['status'] = "OK"
        return HttpResponse(json.dumps(status), content_type="application/json")
    except Exception as e:
        status['status'] = "Error"
        status['message'] = str(e)
        return HttpResponse(json.dumps(status), content_type="application/json")
@login_required
@require_POST
def add_comment(request):
    status = {}
    try:
        post = Post.objects.get(pk=request.POST.get('post_id'))
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            status['status'] = "OK"
            return HttpResponse(json.dumps(status), content_type="application/json")
        else:
            status['status'] = "Error"
            status['message'] = "Invalid form"
            return HttpResponse(json.dumps(status), content_type="application/json")
    except Exception as e:
        status['status'] = "Error"
        status['message'] = str(e)
        return HttpResponse(json.dumps(status), content_type="application/json")

        
