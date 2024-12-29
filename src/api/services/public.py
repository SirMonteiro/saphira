from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *

@api_view(['GET'])
def index(request):
    return Response({"message": "Bem-vinde à API Saphira!"}, status = status.HTTP_200_OK)


@api_view(['GET'])
def admin_index(request):
    return Response({"message": "Credenciais incorretas!! Brincadeirinha... o login deu bom =)"}, status=200)


class AdminLogin(APIView):
    serializer_class = AdminSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)

            return Response({'detail': 'Logado como admin... utilize seus poderes com moderação ;)'}, status = status.HTTP_200_OK)
        else:
            return Response({'detail': 'Você não é da CO-SSI...'}, status = status.HTTP_401_UNAUTHORIZADE)


