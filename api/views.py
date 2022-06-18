from blog.models import Post, Like, Comment
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_exempt
@login_required
def add_like(request, pk):
    status = {}
    try:
        post = Post.objects.get(pk=pk)
        if Like.objects.filter(post=post, user=request.user).exists():
            status['status'] = 'already_liked'
            return HttpResponse(json.dumps(status), content_type='application/json', status=456)
        like = Like(post=post, user=request.user)
        like.save()
        status['status'] = "OK"
        return HttpResponse(json.dumps(status), content_type="application/json")
    except Exception as e:
        status['status'] = "Error"
        status['message'] = str(e)
        return HttpResponse(json.dumps(status), content_type="application/json", status=500)
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
            return HttpResponse(json.dumps(status), content_type="application/json", status=400)
    except Exception as e:
        status['status'] = "Error"
        status['message'] = str(e)
        return HttpResponse(json.dumps(status), content_type="application/json", status=500)
@login_required
@csrf_exempt
def remove_like(request, pk):
    status = {}
    try:
        post = Post.objects.get(pk=pk)
        if not Like.objects.filter(post=post, user=request.user).exists():
            status['status'] = 'not_liked'
            return HttpResponse(json.dumps(status), content_type='application/json', status=456)
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        status['status'] = "OK"
        return HttpResponse(json.dumps(status), content_type="application/json")
    except Exception as e:
        status['status'] = "Error"
        status['message'] = str(e)
        return HttpResponse(json.dumps(status), content_type="application/json", status=500)