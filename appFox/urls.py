from django.urls import path, include
from appFox import views
from django.contrib.auth import views as auth_vie

"""Предоставление для html страниц, собственных URL адресов"""
"""Для классов контролерров, обязательно нужно указывать .as_view() - в них можно передать POST & GET запросы"""
"""<int:pk> = с помощью данного поля, ты ссылаешься на нужную запись в БД"""
urlpatterns = [
    # Форма авторизации взятая из стандартной библиотеки джанго
    #path('', include('django.contrib.auth.urls')),    
    #Форма авторизации логику которой и отображение можно прописывать самостоятельно
    path('login', auth_vie.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_vie.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register', views.RegisterForm.as_view(), name='register'),
    path('', views.PostsView.as_view(), name='index'),
    path('post<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
    #path('postCrt', views.CrtPostView.as_view(), name='crt_post'),
    path('postCrt', views.create_post, name='crt_post'),
    path('postUpd<int:pk>', views.UpdPostView.as_view(), name='upd_post'),
    path('del<int:pk>', views.DelPostView.as_view(), name='del_post'),
    path('post<int:pk>add_comit', views.AddComitView.as_view(), name='add_comit'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download'),
]
