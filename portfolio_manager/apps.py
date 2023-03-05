from django.apps import AppConfig


class PortfolioManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_manager'

    def ready(self):
        import portfolio_manager.management.commands
