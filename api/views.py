from django.shortcuts import render
from rest_framework import viewsets
from api.models import CheckBox
from api.serializers import CheckBoxSerializer

class CheckBoxViewSet(viewsets.ModelViewSet):
    queryset = CheckBox.objects.all()
    serializer_class = CheckBoxSerializer


