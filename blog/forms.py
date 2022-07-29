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



from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','meta_description', 'link',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'text': forms.Textarea(attrs={'class': 'text'}),
            'meta_description': forms.TextInput(attrs={'class': 'meta_description'}),
            'link': forms.TextInput(attrs={'class': 'link'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = { 'text': forms.Textarea(attrs={'class': 'comment-text'})}
