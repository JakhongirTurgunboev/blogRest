from django.http import Http404
from django.shortcuts import render

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import CustomUser, Blog, Comment, Like
from .permissions import IsAdmin
from .serializers import CustomUserSerializer, CommentSerializer, LikeSerializer, BlogSerializer


class CustomerUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)
    #permission_classes = [IsAuthenticated]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

@swagger_auto_schema(
    method='get',
    #manual_parameters=[
    #    openapi.Parameter(
    #        name='search',
    #        in_=openapi.IN_QUERY,
    #        type=openapi.TYPE_STRING,
    #        description='Search query',
    #        required=False,
    #    ),
    #],
    responses={200: openapi.Response('Like view', serializer_name='Like serializer')},
)
@api_view(['GET'])
def get_likes(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    number_of_likes = Like.objects.filter(blog=blog).count()

    return Response({'likes': number_of_likes})


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            name='blog_id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description='Blog ID',
            required=True,
        ),
    ],
    responses={200: openapi.Response('Comment view', serializer_name='comment serializer')},
)
@api_view(['GET'])
def get_comment(request):
    blog_id = request.GET.get('blog_id')
    try:
        comment = Comment.objects.get(blog=blog_id)
    except Comment.DoesNotExist:
        return Response([])
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
