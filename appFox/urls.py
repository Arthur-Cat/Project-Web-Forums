from django.urls import path
from appFox import views


"""Предоставление для html страниц, собственных URL адресов"""
"""Для классов контролерров, обязательно нужно указывать .as_view() - в них можно передать POST & GET запросы"""
"""<int:pk> = с помощью данного поля, ты ссылаешься на нужную запись в БД"""
urlpatterns = [
    path('', views.PostsView.as_view(), name='index'),
    path('post<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
    path('postCrt', views.CrtPostView.as_view(), name='crt_post'),
    path('postUpd<int:pk>', views.UpdPostView.as_view(), name='upd_post'),
    path('del<int:pk>', views.DelPostView.as_view(), name='del_post'),
    path('post<int:pk>add_comit', views.AddComitView.as_view(), name='add_comit'),
    path('about/', views.about, name='about'),
]