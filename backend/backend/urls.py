from django.contrib import admin
from django.urls import path, include
from social_django.urls import urlpatterns as social_django_urls
from django.contrib.auth import views as auth_views
from polls.open_api.router import router

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('polls.open_api.router')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += social_django_urls