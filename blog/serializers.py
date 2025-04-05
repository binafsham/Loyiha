from rest_framework import serializers
from .models import User, Reyting, MockTest, Universitet, Sozlamalar, Yutuq
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'ism', 'familya', 'phone_number', 'date', 'password', 'email')


class ReytingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reyting
        fields = ('id', 'user', 'ball', 'yangilangan_vaqt', 'daraja')


class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest
        fields = ('id', 'user', 'test_nomi', 'natija', 'topshirilgan_vaqt')


class UniversitetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universitet
        fields = ('id', 'nomi', 'joylashuvi', 'reytingi')


class SozlamalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sozlamalar
        fields = ('id', 'user', 'til', 'bildirishnoma_yoqilgan')


class YutuqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yutuq
        fields = ('id', 'user', 'sarlavha', 'tavsif', 'erishilgan_sana')



