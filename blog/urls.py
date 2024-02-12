from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomerUserViewSet)
router.register(r'blog', views.BlogViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'like', views.LikeViewSet)

urlpatterns = [
]

urlpatterns += router.urls
