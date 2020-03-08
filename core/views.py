from django.shortcuts import render
from rest_framework.generics import GenericAPIView

# Create your views here.
from rest_framework.response import Response
from django.shortcuts import redirect

from core.serializers import RedirectionSerializer


class Redirection(GenericAPIView):
    serializer_class = RedirectionSerializer

    def get(self, request, *args, **kwargs):
        response = redirect('https://www.google.com')
        return response

