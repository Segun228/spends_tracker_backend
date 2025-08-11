from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

class TelegramAuthentication(BaseAuthentication):
    def authenticate(self, request):
        telegram_id = request.headers.get('Authorization')
        if not telegram_id:
            return None
        User = get_user_model()
        try:
            user = User.objects.get(telegram_id=telegram_id)
        except User.DoesNotExist:
            raise AuthenticationFailed('Пользователь с таким Telegram ID не найден.')
        return (user, None)