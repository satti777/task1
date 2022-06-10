from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = get_random_string(length=10)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        send_mail('subject', 'Wellcom your password is ' + password, 'qamar.satti5@gmail.com',
                  [email])
        return user

    def validate_email(self, value):
        norml_email = value.lower()
        if User.objects.filter(email=norml_email).exists():
            raise serializers.ValidationError("email already exists")
        return norml_email
