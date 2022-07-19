"""Все импорты библиотек смотри в интернете..."""
from django.shortcuts import render
from appFox.models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import FormPost, FormComit, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


"""Методы для возврата значений, передаваемых в URL 'Нужно что бы сгенерировать страницу - (Контроллеры)'"""
def index(req):
    return render(req, 'index.html')

"""login_required - выдает ошибку если не авторизированный пользователь пытается зайти на страницу под ним"""
@login_required
def about(req):
    return render(req, 'about.html')
"""Класс для создания и инициализации формы регистрации"""
class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

"""Спец класс контролер, ограниченый в применении. Нужен для простоты работы"""
"""LoginRequiredMixin """
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
class CrtPostView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Post
    template_name = 'postCrt.html'
    form_class = FormPost

#Класс для изменения поста
class UpdPostView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Post
    template_name = 'postCrt.html'
    form_class = FormPost

#Класс для удаления поста
class DelPostView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Post
    template_name = 'postDel.html'
    success_url = reverse_lazy('index')

#Класс для добавления комментария
class AddComitView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Comment
    template_name = 'add_comit.html'
    form_class = FormComit
    #Метод для автоматического присвоения комментария к посту
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)