from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from main.models import Department
from main.serializers import CustomUserCreationModelSerializer, DepartmentModelSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class AuthApiView(APIView):
    # register
    def get(self, request):
        user_serializer = CustomUserCreationModelSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.validated_data['password'] = make_password(user_serializer.validated_data['password'])
            user_serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(user_serializer.errors)

    # login
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            context = {
                'Error': 'username or password is missing'
            }
            return Response(context)
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            context = {
                'token': token.key,
                'user_id': user.id,
                'user': user.username
            }
            return Response(context)
        context = {
            'Error': 'username or password is incorrect'
        }
        return Response(context)
