from django.contrib import admin
from django.urls import path, include
from social_django.urls import urlpatterns as social_django_urls
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('polls.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += social_django_urls 