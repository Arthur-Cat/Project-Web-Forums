from django.shortcuts import render, redirect
from appFox.models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import FormPost, FormComit
from django.urls import reverse_lazy


"""Методы для возврата значений, передаваемых в URL 'Нужно что бы сгенерировать страницу - (Контроллеры)'"""
def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

"""Спец класс контролер, ограниченый в применении. Нужен для простоты работы"""
class PostsView(ListView):
    model = Post
    template_name = 'index.html'
    """Данный параметр отвечает за сортировку """
    ordering = ['-created_at']

#Класс для открытия поста и его содержания
class DetailPostView(DetailView):
    model = Post
    template_name = 'detail_post.html'

#Класс для создания поста
class CrtPostView(CreateView):
    model = Post
    template_name = 'postCrt.html'
    form_class = FormPost

#Класс для изменения поста
class UpdPostView(UpdateView):
    model = Post
    template_name = 'postCrt.html'
    form_class = FormPost

#Класс для удаления поста
class DelPostView(DeleteView):
    model = Post
    template_name = 'postDel.html'
    success_url = reverse_lazy('index')

#Класс для добавления комментария
class AddComitView(CreateView):
    model = Comment
    template_name = 'add_comit.html'
    form_class = FormComit
    #Метод для автоматического присвоения комментария к посту
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)