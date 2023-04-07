from django.urls import path
from .views import user_viewset, index_viewset, issue_viewset
from allauth.account.views import LoginView


urlpatterns = [

    # Principal
    path('', index_viewset.index, name='index'),

    # Usuario
    path('register/', user_viewset.register, name='register'),
    path('login/', user_viewset.logintest, name='logintest'),
    path('login/auth', user_viewset.login_with_google, name='login_with_google'),
    path('is', user_viewset.aux, name='aux'),
    path('logout', user_viewset.logoutTest, name='logoutTest'),
    path('editarPerfil', user_viewset.editarPerfil, name='editarPerfil'),
    path('editarPerfil/actualizar', user_viewset.actualizarPerfil, name='actualizarPerfil'),

    # Issue
    path('pantallaCrearIssue', issue_viewset.pantallaCrearIssue, name='pantallaCrearIssue'),
    path('crearIssue', issue_viewset.crearIssue, name='crearIssue'),
    path('mostrarIssue/<int:idIssue>/', issue_viewset.mostrarIssue, name='mostrarIssue'),
    path('eliminarIssue/<int:idIssue>/', issue_viewset.eliminarIssue, name='eliminarIssue'),
    path('mostrarPantallaEditarIssue/<int:idIssue>/', issue_viewset.mostrarPantallaEditarIssue, name='mostrarPantallaEditarIssue'),
    path('editarIssue/<int:idIssue>/', issue_viewset.editarIssue, name='editarIssue'),
    

]


