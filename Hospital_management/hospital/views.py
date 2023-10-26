from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor
from .serializers import DoctorSerializer, DoctorRegisterSerializer, DoctorLoginSerializer
from rest_framework.exceptions import ValidationError, APIException, AuthenticationFailed, NotFound
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import logout

class DoctorRegisterView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorRegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DoctorLoginView(APIView):
    serializer_class = DoctorLoginSerializer
    print("serializer: ", serializer_class)
    permission_classes = (AllowAny,)

    def post(self, request):
        print(request.data)
        try:
            serializer = self.serializer_class(data=request.data)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            tokens = serializer.save1()
            return Response({'message': 'Doctor Logged in Successfully', 'tokens': tokens}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class DoctorLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            logout(request)
            return Response({"message": " Doctor successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "An error occurred while logging out."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DoctorProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user = request.user
            serializer = DoctorSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({"error": "Doctor not found."}, status=status.HTTP_404_NOT_FOUND)
        except APIException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)