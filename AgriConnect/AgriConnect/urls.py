"""
URL configuration for AgriConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from api.views import WeatherViewSet, FarmerViewSet, ask_chatgpt, weather, market_prices

# Configuration du routeur pour les vues ViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'farmers', FarmerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Inclut les routes du routeur
    path('api/weather/', WeatherViewSet.as_view({'get': 'get_weather'}), name='weather'),
    path('api/market-prices/', market_prices, name='market-prices'),
    path('api/chatgpt/', ask_chatgpt, name='ask_chatgpt'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]