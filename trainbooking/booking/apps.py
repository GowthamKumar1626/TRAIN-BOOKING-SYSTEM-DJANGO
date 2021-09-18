from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

    def ready(self) -> None:
        from booking import signals
        return super().ready()
