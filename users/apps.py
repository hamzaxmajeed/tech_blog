from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """
        imports the signals method
        """
        import users.signals
