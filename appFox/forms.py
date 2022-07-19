from dataclasses import field
from django.forms import ModelForm
from .models import Post, Comment
from django import forms


"""Задаешь форму нужный стилей через библиотеку в Джанге forms, для более красивого отображения"""
class FormPost(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            }

class FormComit(ModelForm):

    class Meta:
        model = Comment
        fields = ['description']
        widgets = {
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            
            }