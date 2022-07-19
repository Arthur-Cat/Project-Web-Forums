"""Все импорты библиотек смотри в интернете..."""
from django.shortcuts import redirect, render
from appFox.models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import FormPost, FormComit, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages #Для функций
from django.contrib.messages.views import SuccessMessageMixin #Для классов

"""Методы для возврата значений, передаваемых в URL 'Нужно что бы сгенерировать страницу - (Контроллеры)'"""
def index(req):
    return render(req, 'index.html')

"""login_required - выдает ошибку если не авторизированный пользователь пытается зайти на страницу под ним"""
""" permission_required - так же как логин, является декоратором. Выполняет те же функции по пирмишинам. Обязательно нужно передовать значения, так же может выводить ошибку"""
"""permission - это доступы и права. Их можно предоставить пользователям через админ панель"""
#@login_required
#@permission_required('appFox.view_post')
def about(req):
    return render(req, 'about.html')


"""Класс для создания и инициализации формы регистрации"""
""" SuccessMessageMixin = окно для отображение сообщения для пользователя. В офиц документаации есть информация о изменении движка"""
class RegisterForm(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_message = "%(username)s успешно зарегестрирован"
    template_name = 'register.html'
    success_url = reverse_lazy('login')

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
# class CrtPostView(LoginRequiredMixin, CreateView):
#     login_url = 'login'
#     model = Post
#     template_name = 'postCrt.html'
#     form_class = FormPost

@login_required
def create_post(request):
    form = FormPost
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            if title != 'POST':
                messages.error(request, f"Все очень плохо у тебя")
                return redirect('index')
            messages.success(request, f"Публикация {title} опубликована.")
            return redirect('index')
            
    return render(request, "postCrt.html", {'form': form})


#Класс для изменения поста
"""LoginRequiredMixin используеться для  проверки авторизации пользователя и предоставление прав просмотра """

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