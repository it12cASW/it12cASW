from django.urls import path
from .views import user_viewset, index_viewset, issue_viewset, equipo_viewset
from allauth.account.views import LoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    # Principal
    path('', index_viewset.index, name='index'),

    # Usuario
    path('register/', user_viewset.register, name='register'),
    path('login/', user_viewset.logintest, name='logintest'),
    path('login/auth', user_viewset.login_with_google, name='login_with_google'),
    path('is', user_viewset.aux, name='aux'),
    path('logout', user_viewset.logoutTest, name='logoutTest'),
    path('editarPerfil', user_viewset.pantallaEditarPerfil, name='pantallaEditarPerfil'),
    path('editarPerfil/actualizar', user_viewset.actualizarPerfil, name='actualizarPerfil'),
    path('verPerfil/<str:username>/', user_viewset.verPerfil, name='verPerfil'),

    # Issue
    path('pantallaCrearIssue', issue_viewset.pantallaCrearIssue, name='pantallaCrearIssue'),
    path('crearIssue', issue_viewset.crearIssue, name='crearIssue'),
    path('mostrarIssue/<int:idIssue>/', issue_viewset.mostrarIssue, name='mostrarIssue'),
    path('eliminarIssue/<int:idIssue>/', issue_viewset.eliminarIssue, name='eliminarIssue'),
    path('mostrarPantallaEditarIssue/<int:idIssue>/', issue_viewset.mostrarPantallaEditarIssue, name='mostrarPantallaEditarIssue'),
    path('editarIssue/<int:idIssue>/', issue_viewset.editarIssue, name='editarIssue'),
    path('addComment/<int:idIssue>/', issue_viewset.addComment, name='añadirComments'),
    path('bulkInsertView', issue_viewset.bulkInsertView, name='bulkInsertView'),
    path('bulkInsert', issue_viewset.bulkInsert, name='bulkInsert'),
    path('quieroBloquear/<int:idIssue>/', issue_viewset.quieroBloquear, name='quieroBloquear'),
    path('bloquearIssue/<int:idIssue>/', issue_viewset.bloquearIssue, name='bloquearIssue'),
    path('desbloquearIssue/<int:idIssue>/', issue_viewset.desbloquearIssue, name='desbloquearIssue'),
    path('pantallaAddDeadline/<int:idIssue>/', issue_viewset.pantallaAddDeadline, name='pantallaAñadirDeadline'),
    path('addDeadline/<int:idIssue>/', issue_viewset.addDeadline, name='añadirDeadline'),
    path('eliminarDeadline/<int:idIssue>/', issue_viewset.eliminarDeadline, name='eliminarDeadline'),
    path('addAttachments', issue_viewset.upload_file, name='addAttachments'),
    #Eliminar vigilante de la issue
    path('eliminar-vigilante/<int:idIssue>/<int:idWatcher>/', issue_viewset.eliminarVigilante, name='eliminar_vigilante'),
    path('pantalla-agregar-vigilante/<int:idIssue>/', issue_viewset.mostrarUsuariosParaAñadir, name='mostrar-pantalla-vigilante'),
    path('agregar-vigilante/<int:idIssue>/', issue_viewset.agregarVigilante, name='agregar_vigilante'),
    # Equipo
    path('pantallaCrearEquipo', equipo_viewset.pantallaCrearEquipo, name='pantallaCrearEquipo'),
    path('crearEquipo/', equipo_viewset.crearEquipo, name='crearEquipo'),
    path('seleccionarEquipo/', user_viewset.seleccionarEquipo, name='seleccionarEquipo'),

    # Filtros
    path('filtrar-issues/', issue_viewset.filtrar_issues, name='filtrar-issues'),

    #Ordenar
    path('ordenar-issues/', issue_viewset.ordenar_issues, name='ordenar-issues'),

    #Busqueda
    path('search/', issue_viewset.search_issues, name='search_issues'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


