from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=150,
        min_length=1,
        help_text='Required. 150 characters or fewer. '
                  'Letters, digits and @/./+/-/_ only.')
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    is_active = serializers.BooleanField(
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.'
    )
    last_login = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(
        help_text='Designates that this user has all permissions '
                  'without explicitly assigning them.')

    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name',
                  'is_active', 'last_login', 'is_superuser')
        model = User


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        min_length=1,
        help_text='Required. 150 characters or fewer. '
                  'Letters, digits and @/./+/-/_ only.')
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, min_length=1)

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'password')
        model = User

    def validate_username(self, data):
        if User.objects.filter(username=data).exists():
            raise serializers.ValidationError(
                'Имя уже занято')
        return data
