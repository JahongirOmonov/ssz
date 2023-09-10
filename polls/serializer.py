from .models import todoModel
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todoModel
        fields=('__all__')