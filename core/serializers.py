from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from core.models import KeyUrlMap


class RedirectionSerializer(Serializer):
    pass


class CreateMappingSerializer(ModelSerializer):
    potato_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = KeyUrlMap
        fields = ('url', 'potato_url')

    @staticmethod
    def get_potato_url(obj):
        return obj.get_potato_url()
