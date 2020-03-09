from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView

# Create your views here.
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.views import APIView

from core.models import KeyUrlMap
from core.serializers import RedirectionSerializer, CreateMappingSerializer
from keygen.utils.key_fetch import fetch_key


class BaseGenericViewMixin(GenericAPIView):
    def _get_serialized_data(self, data):
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class Redirection(GenericAPIView):
    serializer_class = RedirectionSerializer

    def get(self, request, *args, **kwargs):
        response = redirect('https://www.google.com')
        return response


class CreateMapping(BaseGenericViewMixin):
    serializer_class = CreateMappingSerializer

    def post(self, request, *args, **kwargs):
        data = self._get_serialized_data(request.data)
        key = fetch_key()
        print(key)
        kum = KeyUrlMap.objects.create(key=key, url=data.get('url'))
        serializer = self.get_serializer(kum)
        return Response(serializer.data)
