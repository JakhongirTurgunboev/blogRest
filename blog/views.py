from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from .models import CustomUser, Blog, Comment, Like
from .serializers import CustomUserSerializer, CommentSerializer, LikeSerializer, BlogSerializer


class CustomerUserViewSet(ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class BlogViewSet(ViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewSet(ViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(ViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

