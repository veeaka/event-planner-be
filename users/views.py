from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers import UserSignupSerializer, UserLoginSerializer


class SignupView(generics.CreateAPIView):
    """
    API view to handle user signup.
    """

    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=response.data["email"])
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "message": "Signup successful",
                "user_id": user.id,
                "email": user.email,
                "token": token.key,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    """
    API view to handle user login and return an authentication token.
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": "Login successful",
                    "user_id": user.id,
                    "email": user.email,
                    "token": token.key,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
