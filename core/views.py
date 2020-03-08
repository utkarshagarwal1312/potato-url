from django.shortcuts import render
from rest_framework.generics import GenericAPIView

# Create your views here.
from rest_framework.response import Response

from core.serializers import RedirectionSerializer


class Redirection(GenericAPIView):
    serializer_class = RedirectionSerializer

    def get(self, request):
        return Response(status=301)

