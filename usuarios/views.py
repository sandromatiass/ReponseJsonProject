from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json

def home_page(request):
    # Dados dos usuários
    usuarios_data = {
        "usuarios": [
            {
                "nome": "Carlos",
                "email": "carlos@email.com"
            },
            {
                "nome": "João",
                "email": "joão@email.com"
            }
        ]
    }
    
    # Formata o JSON para exibição bonita
    json_formatado = json.dumps(usuarios_data, indent=2, ensure_ascii=False)
    
    return render(request, 'home.html', {
        'usuarios': usuarios_data['usuarios'],
        'json_data': json_formatado
    })

class UsuarioJSONAPI(APIView):
    def get(self, request):
        # API que retorna apenas JSON puro
        dados_usuarios = {
            "usuarios": [
                {
                    "nome": "Carlos",
                    "email": "carlos@email.com"
                },
                {
                    "nome": "João",
                    "email": "joão@email.com"
                }
            ]
        }
        return Response(dados_usuarios)