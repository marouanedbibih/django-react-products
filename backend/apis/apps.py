from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'apis'

    def ready(self):
        import apis.signals
