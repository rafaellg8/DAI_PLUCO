from django import forms
from .models import Comment,User,Forum

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userName','name','firstName','secondName','email','password','birthday',)

class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('theme','title','commentText','url',)

class Forum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title','theme','asignature',)
