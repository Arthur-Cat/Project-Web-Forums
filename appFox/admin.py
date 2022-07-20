from django.contrib import admin
from appFox.models import Post, Comment

"""Регистрация в админ панеле моделей"""
admin.site.register(Post)
admin.site.register(Comment)

