from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor, Patient

User = get_user_model()


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "doctor_name", "doctor_hospital_name", "speciality", "gender", "experience", "phone", "address", "email",]
        
        def get_gender(self, obj):
            return User.GENDER_CHOICES[obj.gender - 1][1]
        extra_kwargs = {
            "password": {"write_only": True},
        }


class DoctorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("doctor_name", "doctor_hospital_name", "speciality", "gender", "experience", "phone", "address", "email", "password", "re_password")

    def validate_gender(self, value):
        gender_mapping = {
            "female": 1,
            "male": 2,
            "other": 3,
        }
        gender_value = gender_mapping.get(value.lower())
        if gender_value is None:
            raise serializers.ValidationError("Invalid gender input")
        return gender_value

    def create(self, validated_data):
        user_data = validated_data.pop('user_profile', None)
        if user_data:
            user = Doctor.objects.create(**validated_data)
            user.set_password(user_data['password'])
            user.save()
            return user
        return None

class DoctorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password")
        return user

    def save1(self):
        user = self.validated_data
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }