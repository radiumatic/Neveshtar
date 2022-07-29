# Copyright (c) 2022 radiumatic
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



from django.utils import timezone
from blog.models import Post, Like
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
            return HttpResponse(json.dumps(status), content_type='application/json', status=400)
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
            comment.created_date = timezone.now()
            comment.save()
            status['status'] = "OK"
            status["comment"] = {
                "username": comment.user.username,
                "comment": comment.text,
                "created_date": comment.created_date.strftime("%b %d, %Y, %I:%M %p")
            }
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
            return HttpResponse(json.dumps(status), content_type='application/json', status=400)
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        status['status'] = "OK"
        return HttpResponse(json.dumps(status), content_type="application/json")
    except Exception as e:
        status['status'] = "Error"
        status['message'] = str(e)
        return HttpResponse(json.dumps(status), content_type="application/json", status=500)