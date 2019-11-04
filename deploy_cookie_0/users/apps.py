from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "deploy_cookie_0.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import deploy_cookie_0.users.signals  # noqa F401
        except ImportError:
            pass
