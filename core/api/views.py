from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
# Create your views here.


class BlogPostCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, * args, **kwargs):
        BlogPost.objects.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BlogPostRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    lookup_fields = 'pk'

