from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import Post


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)