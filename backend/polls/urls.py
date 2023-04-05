from django.urls import path
from .views import user_viewset, index_viewset
from allauth.account.views import LoginView

urlpatterns = [
    path('', index_viewset.index, name='index'),
    path('register/', user_viewset.register, name='register'),
    path('is', user_viewset.aux, name='aux'),
    path('login/', user_viewset.logintest, name='logintest'),
    path('login/auth', user_viewset.login_with_google, name='login_with_google'),
    
]


