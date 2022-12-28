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



from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from accounts.forms import User

USER = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    link = models.CharField(max_length=300, default='', unique = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    meta_description = models.CharField(default="توضیحات پست", max_length=150)
    thumbnail = models.ImageField(upload_to="posts", null=True)
    


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    @property
    def likes_amount(self):
        return self.like_set.all().count()
    @property
    def comments_amount(self):
        return self.comment_set.all().count()
    @property
    def liked_users(self):
        likes = self.like_set.all()
        return [like.user for like in likes]
        

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.text
 
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


