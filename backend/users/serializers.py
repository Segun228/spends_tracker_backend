from rest_framework.serializers import ModelSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "telegram_id", "created_at", "is_admin", "updated_at"]
        read_only_fields = ["created_at", "is_admin", "updated_at"]
