from django.urls import path, include
from rest_framework import routers
# from api.views import  CheckBoxViewSet
from api import views
# router = routers.DefaultRouter()
# router.register('checkbox', CheckBoxViewSet)

urlpatterns = [
    path('checkbox_list', views.checkbox_list, name='list'),
    path('checkbox_list/<int:pk>', views.checkbox_detail, name='checkbox_detail'),
    path('checkbox_create', views.checkbox_create, name='checkbox_create'),
    path('checkbox_update/<int:pk>', views.checkbox_update, name='checkbox_update'),
    path('checkbox_delete/<int:pk>', views.checkbox_delete, name='checkbox_delete'),
    # path('', include(router.urls)),    
]
