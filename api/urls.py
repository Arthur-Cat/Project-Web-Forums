from django.urls import path, include
from rest_framework import routers
from api.views import  CheckBoxViewSet

router = routers.DefaultRouter()
router.register('checkbox', CheckBoxViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]
