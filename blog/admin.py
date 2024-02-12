from django.contrib import admin

# Register your models here.
from blog.models import CustomUser, Blog

admin.site.register(CustomUser)
admin.site.register(Blog)
