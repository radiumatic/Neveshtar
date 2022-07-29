# Neveshtar
# Copyright (C) 2022  radiumatic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



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