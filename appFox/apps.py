from django.apps import AppConfig

"""Регистрация приложений (appFox) в системе Django для корректной работы"""
"""Класс передается в настройки в разделе  settings.py forum_data"""
class AppfoxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appFox'
