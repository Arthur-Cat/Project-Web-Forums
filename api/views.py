from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework import viewsets
from api import serializers
from api.models import CheckBox
from api.serializers import CheckBoxSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class CheckBoxViewSet(viewsets.ModelViewSet):
#     queryset = CheckBox.objects.all()
#     serializer_class = CheckBoxSerializer

@api_view(['GET'])
def checkbox_list(req):
    checkboxes = CheckBox.objects.all()
    serializers = CheckBoxSerializer(checkboxes, many=True)           
    return Response(serializers.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)   
        serializers = CheckBoxSerializer(checkbox)
    except CheckBox.DoesNotExist:
        return Response(("Error:", "checkbox_list is not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializers.data)


@api_view(['POST'])
def checkbox_create(req):   
    serializers = CheckBoxSerializer(data=req.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)   
        serializers = CheckBoxSerializer(instance=checkbox, data=req.data)
        if serializers.is_valid():
            serializers.save()
    except CheckBox.DoesNotExist:
        return Response(("Error:", "checkbox_list is not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializers.data)


@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = CheckBox.objects.get(id=pk) 
    checkbox.delete()  
    return Response(status=status.HTTP_204_NO_CONTENT)