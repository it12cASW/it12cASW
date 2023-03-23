from django.apps import AppConfig


# la ruta es polls.apps.PollsConfig
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
