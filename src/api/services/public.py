from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    return Response({"message": "Bem-vinde à API Saphira!"}, status = status.HTTP_200_OK)


@api_view(['GET'])
def admin_index(request):
    return Response({"message": "Credenciais incorretas!! Brincadeirinha... o login deu bom =)"}, status=200)
