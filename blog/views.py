# Neveshtar
# Copyright (C) 2022  Nima Ghasemi Por
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



from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q 
from django.http import HttpResponseRedirect
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
    if not request.user.groups.filter(name="Writers").exists():
        return HttpResponseRedirect('/accounts/login')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', url=post.link)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    if not request.user.groups.filter(name="Writers").exists():
        return HttpResponseRedirect('/accounts/login')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', url=post.link)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def search(request):
    q = request.GET["q"]
    page = 1
    try:
        page = request.GET["page"]
    except:
        pass
    if q != None:
        posts = Post.objects.filter(Q(title__icontains=q) | Q(text__icontains=q) | Q(meta_description__icontains=q))
        if not posts:
            return render(request, "blog/search_results.html")
        posts = posts[(page-1)*10:page*10]
        pages_amount=len(Post.objects.all())//10
        return render(request, 'blog/post_list.html', {'posts':posts, 'pages_amount':range(1, pages_amount+2), 'page':page})
    else:
        raise Http404

        
