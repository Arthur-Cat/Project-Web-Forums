from rest_framework import serializers
from api.models import CheckBox

class CheckBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckBox
        fields = '__all__'