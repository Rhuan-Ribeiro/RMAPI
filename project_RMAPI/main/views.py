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
            characterFound = ''
            # se passarem o filtro de 'name' 
            if ('name' in request.GET and 'species' in request.GET):
                nameToFilter = request.GET['name']
                speciesToFilter = request.GET['species']
                # LÓGICA AND
                characterFound = Character.objects.filter(name__contains=nameToFilter).filter(species__contains=speciesToFilter)
                # LÓGICA OR
                # characterFound = Character.objects.filter(name__contains=nameToFilter) | Character.objects.filter(species__contains=speciesToFilter)

            elif ('name' in request.GET):
                # pegando o parametro que foi informado!
                nameToFilter = request.GET['name']
                # criando um filtro para a busca
                characterFound = Character.objects.filter(name__contains=nameToFilter)
                    # __contains é reservado no Django, é o equivalente ao like do mySQL
                    # name__startWith=nameToFilter
                    # name__endWith=nameToFilter
            elif ('species' in request.GET):
                speciesToFilter = request.GET['species']
                characterFound = Character.objects.filter(species__contains=speciesToFilter)
            else:
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
    
    def post(self, request):
        locationJson = request.data
        locationSerialized = LocationSerializer(data=locationJson, many=False)
        if (locationSerialized.is_valid()):
            locationSerialized.save()
            return Response(status=201, data=locationSerialized.data)
        return Response(status=400, data="error")
    
    def delete(self, request, locationId = ''):
        if (locationId != ''):
            locationFound = Location.objects.get(id=locationId)
            locationFound.delete()
            return Response(status=200, data='Character sucessfully deleted!')
        return Response(status=400, data='characterid must be given!')
    
    def put(self, request, locationId = ''):
        if(locationId != ''):
            locationFound = Location.objects.get(id=locationId)
            locationToUpdateJSON = request.data
            serializedLocation = CharacterSerializer(locationFound, data=locationToUpdateJSON)
            if (serializedLocation.is_valid()):
                serializedLocation.save()
                return Response(status=200, data=serializedLocation.data)
            return Response(status=400, data='Invalid Data!')
        return Response(status=400, data='characterId must be given!')
    
class EpisodeAPIView(APIView):
    def get(self, request, epId = ''):
        if (epId == ''):
            epFound = Episode.objects.all()
            serializer = EpisodeSerializer(epFound, many=True)
            return Response(serializer.data)
        epFound = Episode.objects.get(id=epId)
        serializer = LocationSerializer(epFound, many=False)
        return Response(serializer.data)
    
    def post(self, request):
        epJson = request.data
        epSerialized = EpisodeSerializer(data=epJson, many=False)
        if (epSerialized.is_valid()):
            epSerialized.save()
            return Response(status=201, data=epSerialized.data)
        return Response(status=400, data="error")
    
    def delete(self, request, epId = ''):
        if (epId != ''):
            epFound = Episode.objects.get(id=epId)
            epFound.delete()
            return Response(status=200, data='Character sucessfully deleted!')
        return Response(status=400, data='characterid must be given!')
    
    def put(self, request, epId = ''):
        if(epId != ''):
            epFound = Episode.objects.get(id=epId)
            epToUpdateJSON = request.data
            serializedEpisode = EpisodeSerializer(epFound, data=epToUpdateJSON)
            if (serializedEpisode.is_valid()):
                serializedEpisode.save()
                return Response(status=200, data=serializedEpisode.data)
            return Response(status=400, data='Invalid Data!')
        return Response(status=400, data='characterId must be given!')
    
class Character_EpisodeAPIView(APIView):
    def get(self, request, chracter_epId = ''):
        if (chracter_epId == ''):
            chracter_epFound = Characters_Episode.objects.all()
            serializer = Characters_EpisodeSerializer(chracter_epFound, many=True)
            return Response(serializer.data)
        chracter_epFound = Characters_Episode.objects.get(id=chracter_epId)
        serializer = Characters_EpisodeSerializer(chracter_epFound, many=False)
        return Response(serializer.data)
    
    