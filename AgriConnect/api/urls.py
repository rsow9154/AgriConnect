from django.urls import path
from .views import WeatherViewSet  # Importez WeatherViewSet

urlpatterns = [
    path('weather/', WeatherViewSet.as_view({'get': 'get_weather'})),
]


from django.urls import path
from .views import weather, market_prices

urlpatterns = [
    path('weather/', weather, name='weather'),
    path('market-prices/', market_prices, name='market-prices'),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet

router = DefaultRouter()
router.register(r'farmers', FarmerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import ask_chatgpt

urlpatterns = [
    path('chatgpt/', ask_chatgpt, name='ask_chatgpt'),
]

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    ...
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]