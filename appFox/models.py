import imp
from turtle import back, update
from django.db import models
from django.urls import reverse


"""Модель поста, что он должен иметь в себе"""
class Post(models.Model):

    title = models.CharField(verbose_name='Название', max_length=70)
    description = models.TextField(
        verbose_name='Контент', 
        null=True, 
        blank=True
        )
    image = models.ImageField(verbose_name='Арт', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Создание', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Изменение', auto_now=True)

    """Метод для отображения своих значений в админке"""
    def __str__(self):
        return self.title

    """Метод что бы при создании нового поста, возвращаться на глав страницу"""
    def get_absolute_url(self):
        return reverse('index')



"""Модель коммента к посту, что он должен иметь в себе"""
class Comment(models.Model):
    description = models.TextField(
        verbose_name='Контент', 
        null=True, 
        blank=True
        )
    created_at = models.DateTimeField(verbose_name='Создание', auto_now_add=True)
    """Тип связки комментария с постом"""
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse("index")

