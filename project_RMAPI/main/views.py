from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CharacterAPIView(APIView):
    def get(self, request, characterId = ''):
        # se o get não tiver filtro de id:
        # retorna todos os characters
        if (characterId == ''):
            characterFound = Character.objects.all()
            serializer = CharacterSerializer(characterFound, many=True)
            return Response(serializer.data)
        # se tiver, vai tentar buscar pelo id:
        # retorna um id
        try:
            characterFound = Character.objects.get(id=characterId)
            serializer = CharacterSerializer(characterFound, many=False)
            return Response(serializer.data)
        # não encontrou o character
        # retorna um 
        except Character.DoesNotExist:
            return Response(status=404, data="Character not found.")
        
    def post(self, request):
        #pega o Json do cliente e guardando a variavel
        characterJson = request.data
        # converte JSON para python
        characterSerialized = CharacterSerializer(data=characterJson, many=False)
        #verifica se os dados estão coerentes
        if (characterSerialized.is_valid()):
            # salva os dados no banco de dados
            characterSerialized.save()
            # retorna o status do protocolo de códigos http 201
            # 200 está na faixa do 200, responsáveis por retornar algo positivo
            # 201 significa "Created"(criado)
            return Response(status=201, data=characterSerialized.data)
        # se os dados não são coerentes ele retorna um código de erro
        # junto com a mensagem
        return Response(status=400, data="error")
    
    def delete(self, request, characterId = ''):
        if (characterId != ''):
            # procura o character pelo Id
            characterFound = Character.objects.get(id=characterId)
            # Deleta o character encontrado
            characterFound.delete()
            # Retorna o status OK, com a mensagem que diz que deu certo
            return Response(status=200, data='Character sucessfully deleted!')
        # cliente da API não passou o characterId para deletar!
        return Response(status=400, data='characterid must be given!')
    
    def put(self, request, characterId = ''):
        if(characterId != ''):
            # procurar o antigo no banco de dados
            characterFound = Character.objects.get(id=characterId)
            # coletar o novo que veio em JSON
            characterToUpdateJSON = request.data
            # Faça o serializer substituir o antigo pelo novo e converter em python
            serializedCharacter = CharacterSerializer(characterFound, data=characterToUpdateJSON)
            # verificar se a conversão é válida
            if (serializedCharacter.is_valid()):
                # salva no banco de dados
                serializedCharacter.save()
                return Response(status=200, data=serializedCharacter.data)
            return Response(status=400, data='Invalid Data!')
        # cliente da API não passou o peopleId para editar
        return Response(status=400, data='characterId must be given!')
        

class LocationAPIView(APIView):
    def get(self, request, locationId = ''):
        if (locationId == ''):
            locationFound = Location.objects.all()
            serializer = LocationSerializer(locationFound, many=True)
            return Response(serializer.data)
        locationFound = Location.objects.get(id=locationId)
        serializer = LocationSerializer(locationFound, many=False)
        return Response(serializer.data)
    
class EpisodeAPIView(APIView):
    def get(self, request, epId = ''):
        if (epId == ''):
            epFound = Episode.objects.all()
            serializer = EpisodeSerializer(epFound, many=True)
            return Response(serializer.data)
        epFound = Episode.objects.get(id=epId)
        serializer = LocationSerializer(epFound, many=False)
        return Response(serializer.data)
    
class Character_EpisodeAPIView(APIView):
    def get(self, request, chracter_epId = ''):
        if (chracter_epId == ''):
            chracter_epFound = Characters_Episode.objects.all()
            serializer = Characters_EpisodeSerializer(chracter_epFound, many=True)
            return Response(serializer.data)
        chracter_epFound = Characters_Episode.objects.get(id=chracter_epId)
        serializer = Characters_EpisodeSerializer(chracter_epFound, many=False)
        return Response(serializer.data)