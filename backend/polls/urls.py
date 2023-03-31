from django.urls import path

from .views import user_viewset, index_viewset

urlpatterns = [
    path('register', user_viewset.register, name='register'),
    path('login', user_viewset.login, name='login'),
    path('', index_viewset.index, name='index'),
]
