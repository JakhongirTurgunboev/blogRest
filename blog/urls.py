from django.urls import path, include
from rest_framework import routers

from blog import views
from blog.views import get_likes, get_comment

router = routers.DefaultRouter()
router.register(r'users', views.CustomerUserViewSet)
router.register(r'blog', views.BlogViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'like', views.LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like-count/<int:blog_id>/', get_likes, name='like-count'),
    path('get-comment/', get_comment, name='get_comment'),
]