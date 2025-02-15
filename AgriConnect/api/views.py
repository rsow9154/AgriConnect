from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Farmer
from .serializers import FarmerSerializer

# Vue pour les agriculteurs
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

# Vue pour la météo
class WeatherViewSet(viewsets.ViewSet):
    def get_weather(self, request):
        return Response({"message": "Weather data"})

# Vue pour ChatGPT
@api_view(['POST'])
def ask_chatgpt(request):
    prompt = request.data.get('prompt')
    # Logique pour interagir avec ChatGPT
    return Response({"response": "Réponse de ChatGPT"})

# Vue pour les prix du marché
@api_view(['GET'])
def market_prices(request):
    return Response({"message": "Market prices data"})

# Vue pour la météo (alternative)
@api_view(['GET'])
def weather(request):
    return Response({"message": "Weather data"})